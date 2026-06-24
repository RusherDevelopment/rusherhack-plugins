#!/usr/bin/env python3
# -----------------------------------------------------------
# Static API Emitter
# -----------------------------------------------------------
#
# Builds static JSON API files from:
#   generated/json/plugins-and-themes.json
#
# Optional module feature source:
#   generated/json/plugin-modules.json
#
# Output:
#   public/api/v1/**
#
# Usage:
#   python scripts/API/emit_static_api.py
#
# -----------------------------------------------------------

from __future__ import annotations

import hashlib
import json
import os
import pathlib
import re
import shutil
import sys
import urllib.parse
from datetime import datetime, timezone
from typing import Any, Dict, Iterable, List, Tuple

# -----------------------------------------------------------
# Paths
# -----------------------------------------------------------

def find_repo_root() -> pathlib.Path:
    """
    Find repo root by walking upward until data/plugins-and-themes.yml exists.
    Works whether this script lives in scripts/API/ or somewhere else.
    """
    here = pathlib.Path(__file__).resolve()

    for parent in [here.parent, *here.parents]:
        if (parent / "data" / "plugins-and-themes.yml").exists():
            return parent

    raise RuntimeError("Could not find repo root containing data/plugins-and-themes.yml")


ROOT = find_repo_root()

SRC = ROOT / "generated" / "json" / "plugins-and-themes.json"
MODULES_SRC = ROOT / "generated" / "json" / "plugin-modules.json"

# API output is generated into the temporary GitHub Pages deploy artifact.
# The deploy workflow copies public_html/ into public/ before this script runs.
API = ROOT / "public" / "api" / "v1"

WRITTEN: List[pathlib.Path] = []

# -----------------------------------------------------------
# Canonical Minecraft versions
# -----------------------------------------------------------

CANON_VERSIONS: List[str] = [
    "1.20.1",
    "1.20.2",
    "1.20.3",
    "1.20.4",
    "1.20.5",
    "1.20.6",
    "1.21",
    "1.21.1",
    "1.21.2",
    "1.21.3",
    "1.21.4",
    "1.21.5",
    "1.21.6",
    "1.21.7",
    "1.21.8",
    "1.21.11",
]

CANON_INDEX = {version: index for index, version in enumerate(CANON_VERSIONS)}
CANON_SET = set(CANON_VERSIONS)

# Accept only Minecraft-looking tokens.
VERSION_TOKEN_RE = re.compile(r"^\d+(?:\.\d+){1,2}$")


# -----------------------------------------------------------
# General helpers
# -----------------------------------------------------------

def log(message: str) -> None:
    print(f"[emit_static_api] {message}")


def fail(message: str) -> None:
    sys.stderr.write(f"[emit_static_api] ERROR: {message}\n")
    sys.exit(1)


def ensure_src() -> None:
    if not SRC.exists():
        fail(f"Source JSON missing: {SRC}")


def read_json(path: pathlib.Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"Failed to read JSON from {path}: {exc}")


def json_text(obj: Any) -> str:
    return json.dumps(
        obj,
        indent=2,
        ensure_ascii=False,
        sort_keys=True,
    ) + "\n"


def write_json(path: pathlib.Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json_text(obj), encoding="utf-8")
    WRITTEN.append(path)
    log(f"wrote {path.relative_to(ROOT)} ({path.stat().st_size} bytes)")


def clean_api_dir() -> None:
    """
    Remove the old generated API folder so stale per-item/bucket JSON files
    disappear when plugins/themes are renamed or removed.
    """
    if API.exists():
        shutil.rmtree(API)

    API.mkdir(parents=True, exist_ok=True)
    log(f"cleaned {API.relative_to(ROOT)}")


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()

    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            h.update(chunk)

    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalize_path(path: pathlib.Path) -> str:
    return str(path).replace(os.sep, "/")


def natural_key(value: Any) -> list[Any]:
    return [
        int(token) if token.isdigit() else token.lower()
        for token in re.split(r"(\d+)", str(value))
    ]


# -----------------------------------------------------------
# Dataset helpers
# -----------------------------------------------------------

def with_type(items: Iterable[Dict[str, Any]], item_type: str) -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []

    for item in items:
        if not isinstance(item, dict):
            continue

        doc = dict(item)
        doc["type"] = item_type
        out.append(doc)

    return out


def get_items(full: Dict[str, Any]) -> List[Dict[str, Any]]:
    return list(full.get("plugins", [])) + list(full.get("themes", []))


def _to_str(value: Any) -> str:
    if value is None:
        return ""
    return str(value)


# -----------------------------------------------------------
# Version parsing
# -----------------------------------------------------------

def normalize_mc_versions(raw: Any, *, item_name: str = "<unknown>") -> List[str]:
    """
    Convert registry mc_versions into canonical API version list.

    Current expected registry format is:
      - "1.21.4"
      - "1.20.1, 1.20.2, 1.21, 1.21.1"
      - "N/A"

    Dash ranges are intentionally rejected here because the validator now
    requires explicit comma-separated versions.
    """
    if raw is None:
        return []

    if isinstance(raw, list):
        parts = [_to_str(value).strip() for value in raw]
    else:
        text = _to_str(raw).strip()

        if not text or text.upper() == "N/A":
            return []

        if "-" in text:
            fail(
                f"{item_name}: mc_versions must be comma-separated, not a dash range. "
                f"Found: {text}"
            )

        parts = [part.strip() for part in text.split(",")]

    versions: List[str] = []

    for part in parts:
        if not part:
            fail(f"{item_name}: mc_versions contains an empty version.")

        if part.upper() == "N/A":
            continue

        if not VERSION_TOKEN_RE.match(part):
            fail(f"{item_name}: invalid Minecraft version token: {part}")

        if part not in CANON_SET:
            fail(
                f"{item_name}: unknown Minecraft version: {part}. "
                "Update CANON_VERSIONS if this version is officially supported."
            )

        versions.append(part)

    return sorted(set(versions), key=lambda version: CANON_INDEX[version])


def item_versions(item: Dict[str, Any]) -> List[str]:
    raw = item.get("mc_versions", item.get("versions", None))
    return normalize_mc_versions(
        raw,
        item_name=str(item.get("name") or item.get("repo") or "<unknown>"),
    )


# -----------------------------------------------------------
# Creators, slugs, repo parsing
# -----------------------------------------------------------

def item_creators(item: Dict[str, Any]) -> List[str]:
    out: List[str] = []

    creator = item.get("creator", {})
    if isinstance(creator, dict):
        name = creator.get("name")
        if isinstance(name, str) and name.strip():
            out.append(name.strip())

    creators = item.get("creators") or []
    if isinstance(creators, list):
        for creator_name in creators:
            if isinstance(creator_name, str) and creator_name.strip():
                out.append(creator_name.strip())

    # Preserve order but remove duplicates.
    seen: set[str] = set()
    unique: List[str] = []

    for creator_name in out:
        key = creator_name.lower()

        if key in seen:
            continue

        seen.add(key)
        unique.append(creator_name)

    return unique


def slugify(value: Any) -> str:
    return urllib.parse.quote(str(value).strip().lower(), safe="-._~/")


def stable_unknown_slug(item: Dict[str, Any]) -> str:
    raw = json.dumps(item, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    digest = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:10]
    return f"unknown-{digest}"


def parse_repo_fields(repo_value: Any) -> Tuple[str, str, str]:
    """
    Accepts owner/repo or full GitHub URL.

    Returns:
      (owner, repo_name, repo_url)

    Returns ("", "", "") if repo cannot be parsed.
    """
    if not repo_value:
        return "", "", ""

    text = str(repo_value).strip()

    if "://" in text:
        try:
            parsed = urllib.parse.urlparse(text)
            parts = [part for part in parsed.path.split("/") if part]

            if len(parts) >= 2:
                owner, repo_name = parts[0], parts[1]
                repo_name = repo_name.removesuffix(".git")
                return owner, repo_name, f"https://github.com/{owner}/{repo_name}"
        except Exception:
            return "", "", ""

        return "", "", ""

    if "/" in text:
        owner, repo_name = text.split("/", 1)
        repo_name = repo_name.removesuffix(".git")

        if owner and repo_name:
            return owner, repo_name, f"https://github.com/{owner}/{repo_name}"

    return "", "", ""


def normalize_repo_key(repo_value: Any) -> str:
    owner, repo_name, _ = parse_repo_fields(repo_value)

    if owner and repo_name:
        return f"{owner.lower()}/{repo_name.lower()}"

    return str(repo_value or "").strip().lower()


def item_slug(item: Dict[str, Any]) -> str:
    repo_value = item.get("repo") or item.get("repository")

    if repo_value:
        owner, repo_name, _ = parse_repo_fields(repo_value)

        if owner and repo_name:
            return f"{owner.lower()}/{repo_name.lower()}"

    base = str(item.get("id") or item.get("name") or "").strip().lower()
    base = re.sub(r"\s+", "-", base)

    if base:
        return base

    return stable_unknown_slug(item)


# -----------------------------------------------------------
# Module feature merge
# -----------------------------------------------------------

def load_plugin_modules() -> Dict[str, Dict[str, Any]]:
    if not MODULES_SRC.exists():
        log(f"plugin modules source missing, continuing without merge: {MODULES_SRC.relative_to(ROOT)}")
        return {}

    try:
        payload = json.loads(MODULES_SRC.read_text(encoding="utf-8"))
    except Exception as exc:
        log(f"failed to parse {MODULES_SRC.relative_to(ROOT)}: {exc}")
        return {}

    plugins = payload.get("plugins", [])
    if not isinstance(plugins, list):
        return {}

    out: Dict[str, Dict[str, Any]] = {}

    for entry in plugins:
        if not isinstance(entry, dict):
            continue

        repo_key = normalize_repo_key(entry.get("repo"))
        if not repo_key:
            continue

        features = entry.get("features", [])
        if not isinstance(features, list):
            features = []

        clean_features: List[Dict[str, Any]] = []
        module_count = 0
        hud_count = 0

        for feature in features:
            if not isinstance(feature, dict):
                continue

            feature_type = str(feature.get("feature_type") or "").strip().lower()

            if feature_type == "module":
                module_count += 1
            elif feature_type == "hud":
                hud_count += 1

            clean_features.append(
                {
                    "name": feature.get("name"),
                    "class_name": feature.get("class_name"),
                    "feature_type": feature.get("feature_type"),
                    "description": feature.get("description"),
                    "settings": feature.get("settings") or [],
                }
            )

        out[repo_key] = {
            "features": clean_features,
            "feature_counts": {
                "total": len(clean_features),
                "modules": module_count,
                "hud_elements": hud_count,
            },
        }

    return out


def merge_plugin_modules(
    plugins: List[Dict[str, Any]],
    modules_map: Dict[str, Dict[str, Any]],
) -> List[Dict[str, Any]]:
    merged: List[Dict[str, Any]] = []

    for plugin in plugins:
        doc = dict(plugin)
        repo_key = normalize_repo_key(doc.get("repo"))
        feature_info = modules_map.get(repo_key)

        if feature_info:
            doc["features"] = feature_info["features"]
            doc["feature_counts"] = feature_info["feature_counts"]
            doc["has_features"] = feature_info["feature_counts"]["total"] > 0
        else:
            doc["features"] = []
            doc["feature_counts"] = {
                "total": 0,
                "modules": 0,
                "hud_elements": 0,
            }
            doc["has_features"] = False

        merged.append(doc)

    return merged


# -----------------------------------------------------------
# Date helpers
# -----------------------------------------------------------

def parse_iso_date(value: Any) -> datetime | None:
    if not value:
        return None

    text = str(value).strip()

    if not text:
        return None

    try:
        parsed = datetime.fromisoformat(text)
    except ValueError:
        if text.endswith("Z"):
            try:
                parsed = datetime.fromisoformat(text[:-1] + "+00:00")
            except ValueError:
                return None
        else:
            return None

    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)

    return parsed


def latest_dataset_datetime(docs: Iterable[Dict[str, Any]]) -> datetime | None:
    latest: datetime | None = None

    for doc in docs:
        for key in ("updated_at", "added_at"):
            parsed = parse_iso_date(doc.get(key))
            if parsed is None:
                continue

            if latest is None or parsed > latest:
                latest = parsed

    return latest


def stable_generated_at(docs: Iterable[Dict[str, Any]]) -> str | None:
    """
    Return a stable timestamp based on dataset dates.

    This avoids meta.json changing every time the script is rerun with the
    same source data.
    """
    latest = latest_dataset_datetime(docs)

    if latest is None:
        return None

    return latest.astimezone(timezone.utc).isoformat(timespec="seconds")


# -----------------------------------------------------------
# API document building
# -----------------------------------------------------------

def build_data_full(raw: Dict[str, Any]) -> Dict[str, Any]:
    plugins = with_type(raw.get("plugins", []) or [], "plugin")
    themes = with_type(raw.get("themes", []) or [], "theme")

    modules_map = load_plugin_modules()
    plugins = merge_plugin_modules(plugins, modules_map)

    return {
        **raw,
        "plugins": plugins,
        "themes": themes,
    }


def clean_doc(item: Dict[str, Any]) -> Dict[str, Any]:
    return {
        key: value
        for key, value in item.items()
        if not key.startswith("_")
    }


def doc_for_item(item: Dict[str, Any]) -> Dict[str, Any]:
    doc = clean_doc(item)

    versions = item.get("_versions") or []
    creators = item.get("_creators") or []

    doc["versions_canonical"] = versions

    owner, repo_name, repo_url = parse_repo_fields(doc.get("repo", ""))

    if owner:
        doc["owner"] = owner

    if repo_name:
        doc["repo_name"] = repo_name

    if repo_url:
        doc["repo_url"] = repo_url

    if creators:
        doc["creator_slug"] = creators[0].lower()

    return doc


def search_index_doc(doc: Dict[str, Any], slug: str) -> Dict[str, Any]:
    features = doc.get("features") or []

    feature_names = [
        feature.get("name")
        for feature in features
        if isinstance(feature, dict) and feature.get("name")
    ]

    return {
        "name": doc.get("name"),
        "slug": slug,
        "description": doc.get("description", ""),
        "creator": (doc.get("creator") or {}).get("name"),
        "creator_slug": doc.get("creator_slug"),
        "tags": doc.get("tags") or [],
        "versions": doc.get("versions_canonical") or [],
        "repo": doc.get("repo"),
        "type": doc.get("type"),
        "has_features": doc.get("has_features", False),
        "feature_counts": doc.get(
            "feature_counts",
            {
                "total": 0,
                "modules": 0,
                "hud_elements": 0,
            },
        ),
        "feature_names": feature_names,
    }


# -----------------------------------------------------------
# Main
# -----------------------------------------------------------

def main() -> None:
    ensure_src()
    clean_api_dir()

    raw = read_json(SRC)
    if not isinstance(raw, dict):
        fail(f"Source JSON must be an object: {SRC}")

    data_full = build_data_full(raw)

    plugins = data_full.get("plugins", [])
    themes = data_full.get("themes", [])
    items = get_items(data_full)

    # 1) Full dataset passthrough
    write_json(API / "index.json", data_full)

    # 2) Simple splits
    write_json(API / "plugins.json", plugins)
    write_json(API / "themes.json", themes)

    # 3) Aggregate stats and enrichment
    by_type = {
        "plugin": len(plugins),
        "theme": len(themes),
    }

    by_version: Dict[str, int] = {}
    versions_present: set[str] = set()
    creators_count: Dict[str, int] = {}

    plugins_with_features = 0
    total_feature_count = 0
    total_module_count = 0
    total_hud_count = 0

    enriched: List[Dict[str, Any]] = []

    for item in items:
        versions = item_versions(item)
        creators = item_creators(item)
        slug = item_slug(item)

        for version in versions:
            versions_present.add(version)
            by_version[version] = by_version.get(version, 0) + 1

        for creator in creators:
            creators_count[creator] = creators_count.get(creator, 0) + 1

        if item.get("type") == "plugin":
            counts = item.get("feature_counts") or {}
            total = int(counts.get("total") or 0)
            modules = int(counts.get("modules") or 0)
            huds = int(counts.get("hud_elements") or 0)

            total_feature_count += total
            total_module_count += modules
            total_hud_count += huds

            if total > 0:
                plugins_with_features += 1

        enriched.append(
            {
                **item,
                "_slug": slug,
                "_versions": versions,
                "_creators": creators,
            }
        )

    stats = {
        "count": len(items),
        "byType": by_type,
        "byVersion": {
            version: by_version[version]
            for version in CANON_VERSIONS
            if version in by_version
        },
        "creators": dict(
            sorted(
                creators_count.items(),
                key=lambda pair: (-pair[1], pair[0].lower()),
            )
        ),
        "features": {
            "plugins_with_features": plugins_with_features,
            "plugins_without_features": len(plugins) - plugins_with_features,
            "total_features": total_feature_count,
            "total_modules": total_module_count,
            "total_hud_elements": total_hud_count,
        },
    }

    write_json(API / "stats.json", stats)

    # 4) versions.json
    versions_list = [
        version
        for version in CANON_VERSIONS
        if version in versions_present
    ]
    write_json(API / "versions.json", {"versions": versions_list})

    # 5) creators.json
    creators_list = [
        {"name": name, "count": count}
        for name, count in sorted(
            creators_count.items(),
            key=lambda pair: (-pair[1], pair[0].lower()),
        )
    ]
    write_json(API / "creators.json", {"creators": creators_list})

    # 6) Per-item docs and search index
    search_index: List[Dict[str, Any]] = []
    all_docs: List[Dict[str, Any]] = []

    for item in enriched:
        slug = item["_slug"]
        doc = doc_for_item(item)
        all_docs.append(doc)

        item_path = API / "items" / f"{slugify(slug)}.json"
        write_json(item_path, doc)

        search_index.append(search_index_doc(doc, slug))

    # 7) Buckets by version
    for version in versions_list:
        bucket = [
            clean_doc(item)
            for item in enriched
            if version in item["_versions"]
        ]
        write_json(API / "by-version" / f"{slugify(version)}.json", bucket)

    # 8) Buckets by creator
    for creator in sorted(creators_count.keys(), key=lambda value: value.lower()):
        bucket = [
            clean_doc(item)
            for item in enriched
            if creator in item["_creators"]
        ]
        write_json(API / "by-creator" / f"{slugify(creator)}.json", bucket)

    # 9) new.json / recent.json
    new_candidates: List[Tuple[datetime, Dict[str, Any]]] = []
    recent_candidates: List[Tuple[datetime, Dict[str, Any]]] = []

    for doc in all_docs:
        added_dt = parse_iso_date(doc.get("added_at"))
        updated_dt = parse_iso_date(doc.get("updated_at"))

        if added_dt is not None:
            new_candidates.append((added_dt, doc))

        key_dt = updated_dt or added_dt
        if key_dt is not None:
            recent_candidates.append((key_dt, doc))

    new_candidates.sort(key=lambda pair: pair[0], reverse=True)
    recent_candidates.sort(key=lambda pair: pair[0], reverse=True)

    write_json(API / "new.json", [doc for _, doc in new_candidates])
    write_json(API / "recent.json", [doc for _, doc in recent_candidates])

    # 10) search-index.json
    write_json(API / "search-index.json", search_index)

    # 11) meta.json
    source_text = SRC.read_text(encoding="utf-8")
    source_sha256 = sha256_text(source_text)

    meta = {
        "generated_at": stable_generated_at(all_docs),
        "source": "generated/json/plugins-and-themes.json",
        "source_sha256": source_sha256,
        "plugin_modules_source": "generated/json/plugin-modules.json" if MODULES_SRC.exists() else None,
        "counts": {
            "plugins": len(plugins),
            "themes": len(themes),
            "items_total": len(items),
        },
        "versions_canonical": versions_list,
    }
    write_json(API / "meta.json", meta)

    # 12) manifest.json
    manifest_entries = []

    for path in WRITTEN:
        try:
            rel = path.relative_to(API)
        except ValueError:
            continue

        manifest_entries.append(
            {
                "path": normalize_path(rel),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )

    write_json(
        API / "manifest.json",
        {
            "files": sorted(
                manifest_entries,
                key=lambda entry: entry["path"],
            )
        },
    )

    log(f"done: wrote {len(WRITTEN)} files to {API.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
