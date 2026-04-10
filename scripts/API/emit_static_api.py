#!/usr/bin/env python3
import pathlib, shutil, json, sys, os, re, urllib.parse, hashlib
from datetime import datetime, timezone
from typing import Dict, Any, List, Tuple

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "generated" / "json" / "plugins-and-themes.json"
MODULES_SRC = ROOT / "generated" / "json" / "plugin-modules.json"
API = ROOT / "public" / "api" / "v1"

# Track written files for manifest
WRITTEN: List[pathlib.Path] = []

# ---- Canonical Minecraft versions ----
CANON_VERSIONS: List[str] = [
    "1.20.1",
    "1.20.2",
    "1.20.4",
    "1.20.6",
    "1.21",
    "1.21.1",
    "1.21.2",
    "1.21.3",
    "1.21.4",
]
CANON_INDEX = {v: i for i, v in enumerate(CANON_VERSIONS)}


def natural_key(s: str):
    return [int(t) if t.isdigit() else str(s).lower() for t in re.split(r"(\d+)", str(s))]


def ensure_src():
    if not SRC.exists():
        sys.stderr.write(f"[emit_static_api] SOURCE MISSING: {SRC}\n")
        sys.exit(1)


def write_json(path: pathlib.Path, obj: Any):
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(obj, indent=2, ensure_ascii=False)
    path.write_text(data + "\n", encoding="utf-8")
    WRITTEN.append(path)
    print(f"[emit_static_api] wrote {path} ({os.path.getsize(path)} bytes)")


def get_items(full: Dict[str, Any]) -> List[Dict[str, Any]]:
    return list(full.get("plugins", [])) + list(full.get("themes", []))


# ---------- Version parsing & normalization helpers ----------

_vers_token_re = re.compile(r"^\s*\d+(?:\.\d+){0,2}\s*$")  # 1 / 1.21 / 1.21.4


def _to_str(v: Any) -> str:
    if v is None:
        return ""
    if isinstance(v, (int, float)):
        return str(v)
    return str(v)


def _expand_range_token(tok: str) -> List[str]:
    a, b = tok.split("-", 1)
    a, b = a.strip(), b.strip()
    if a in CANON_INDEX and b in CANON_INDEX:
        i, j = CANON_INDEX[a], CANON_INDEX[b]
        if i <= j:
            return CANON_VERSIONS[i : j + 1]
        return CANON_VERSIONS[j : i + 1]
    return []


def _normalize_token(tok: str) -> List[str]:
    if not tok:
        return []
    s = tok.strip()
    if s.upper() == "N/A":
        return []
    if "-" in s:
        return _expand_range_token(s) or []
    if s in CANON_INDEX:
        return [s]
    if _vers_token_re.match(s) and s in CANON_INDEX:
        return [s]
    return []


def item_versions(item: Dict[str, Any]) -> List[str]:
    raw = item.get("mc_versions", None)
    if raw is None:
        raw = item.get("versions", [])

    out: List[str] = []

    if isinstance(raw, list):
        for v in raw:
            out.extend(_normalize_token(_to_str(v)))
    else:
        out.extend(_normalize_token(_to_str(raw)))

    return sorted(set(out), key=lambda x: CANON_INDEX[x])


# ---------- Creators, slugs, repo parsing ----------

def item_creators(item: Dict[str, Any]) -> List[str]:
    out: List[str] = []
    creator = item.get("creator", {})
    if isinstance(creator, dict):
        name = creator.get("name")
        if isinstance(name, str) and name.strip():
            out.append(name.strip())
    creators = item.get("creators") or []
    if isinstance(creators, list):
        for c in creators:
            if isinstance(c, str) and c.strip():
                out.append(c.strip())
    return out


def slugify(s: str) -> str:
    return urllib.parse.quote(s.strip().lower(), safe="-._~/")


def stable_unknown_slug(item: Dict[str, Any]) -> str:
    raw = json.dumps(item, sort_keys=True, separators=(",", ":"))
    h = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:10]
    return f"unknown-{h}"


def parse_repo_fields(repo_value: str) -> Tuple[str, str, str]:
    """
    Accepts owner/repo or full URL; returns (owner, repo_name, repo_url) or ("","","")
    """
    if not repo_value:
        return "", "", ""
    s = str(repo_value).strip()

    if "://" in s:
        try:
            path = urllib.parse.urlparse(s).path
            parts = [p for p in path.split("/") if p]
            if len(parts) >= 2:
                owner, repo = parts[0], parts[1]
                return owner, repo, f"https://github.com/{owner}/{repo}"
        except Exception:
            return "", "", ""
        return "", "", ""

    if "/" in s:
        owner, repo = s.split("/", 1)
        if owner and repo:
            return owner, repo, f"https://github.com/{owner}/{repo}"

    return "", "", ""


def normalize_repo_key(repo_value: Any) -> str:
    owner, repo_name, _ = parse_repo_fields(str(repo_value or ""))
    if owner and repo_name:
        return f"{owner.lower()}/{repo_name.lower()}"
    return str(repo_value or "").strip().lower()


def item_slug(item: Dict[str, Any]) -> str:
    repo_val = item.get("repo") or item.get("repository")
    if repo_val:
        owner, repo_name, _ = parse_repo_fields(str(repo_val))
        if owner and repo_name:
            return f"{owner.lower()}/{repo_name.lower()}"
    base = (item.get("id") or item.get("name") or "").strip().lower()
    base = re.sub(r"\s+", "-", base)
    if base:
        return base
    return stable_unknown_slug(item)


# ---------- Module feature helpers ----------

def load_plugin_modules() -> Dict[str, Dict[str, Any]]:
    if not MODULES_SRC.exists():
        print(f"[emit_static_api] plugin modules source missing, continuing without merge: {MODULES_SRC}")
        return {}

    try:
        payload = json.loads(MODULES_SRC.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[emit_static_api] failed to parse {MODULES_SRC}: {e}")
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

            ftype = str(feature.get("feature_type") or "").strip().lower()
            if ftype == "module":
                module_count += 1
            elif ftype == "hud":
                hud_count += 1

            clean_features.append({
                "name": feature.get("name"),
                "class_name": feature.get("class_name"),
                "feature_type": feature.get("feature_type"),
                "description": feature.get("description"),
                "settings": feature.get("settings") or [],
            })

        out[repo_key] = {
            "features": clean_features,
            "feature_counts": {
                "total": len(clean_features),
                "modules": module_count,
                "hud_elements": hud_count,
            },
        }

    return out


def merge_plugin_modules(full: Dict[str, Any], modules_map: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    merged = {
        **full,
        "plugins": [],
        "themes": list(full.get("themes", [])),
    }

    for plugin in full.get("plugins", []):
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

        merged["plugins"].append(doc)

    return merged


# ---------- Hashing for manifest ----------

def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _parse_iso_date(val: Any) -> datetime | None:
    if not val:
        return None
    s = str(val).strip()
    try:
        return datetime.fromisoformat(s)
    except ValueError:
        if s.endswith("Z"):
            try:
                return datetime.fromisoformat(s[:-1] + "+00:00")
            except ValueError:
                return None
        return None


# ========================= main =========================

def main():
    ensure_src()

    data_full = json.loads(SRC.read_text(encoding="utf-8"))
    modules_map = load_plugin_modules()
    data_full = merge_plugin_modules(data_full, modules_map)

    # 1) Full dataset passthrough
    write_json(API / "index.json", data_full)

    # 2) Simple splits (plugins/themes)
    plugins = data_full.get("plugins", [])
    themes = data_full.get("themes", [])
    write_json(API / "plugins.json", plugins)
    write_json(API / "themes.json", themes)

    # 3) Aggregate stats
    items = get_items(data_full)

    byType = {
        "plugin": len(plugins),
        "theme": len(themes),
    }

    byVersion: Dict[str, int] = {}
    versions_present = set()
    creators_count: Dict[str, int] = {}

    plugins_with_features = 0
    total_feature_count = 0
    total_module_count = 0
    total_hud_count = 0

    enriched: List[Dict[str, Any]] = []
    for it in items:
        versions = item_versions(it)
        creators = item_creators(it)
        slug = item_slug(it)

        for v in versions:
            versions_present.add(v)
            byVersion[v] = byVersion.get(v, 0) + 1

        for c in creators:
            creators_count[c] = creators_count.get(c, 0) + 1

        if it.get("type") == "plugin":
            counts = it.get("feature_counts") or {}
            total = int(counts.get("total") or 0)
            modules = int(counts.get("modules") or 0)
            huds = int(counts.get("hud_elements") or 0)
            total_feature_count += total
            total_module_count += modules
            total_hud_count += huds
            if total > 0:
                plugins_with_features += 1

        enriched.append({**it, "_slug": slug, "_versions": versions, "_creators": creators})

    stats = {
        "count": len(items),
        "byType": byType,
        "byVersion": {v: byVersion[v] for v in CANON_VERSIONS if v in byVersion},
        "creators": creators_count,
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
    versions_list = [v for v in CANON_VERSIONS if v in versions_present]
    write_json(API / "versions.json", {"versions": versions_list})

    # 5) creators.json
    creators_list = sorted(
        [{"name": k, "count": v} for k, v in creators_count.items()],
        key=lambda x: (-x["count"], x["name"].lower()),
    )
    write_json(API / "creators.json", {"creators": creators_list})

    # 6) Per-item docs
    search_index: List[Dict[str, Any]] = []
    all_docs: List[Dict[str, Any]] = []

    for it in enriched:
        slug = it["_slug"]
        doc = {k: v for k, v in it.items() if not k.startswith("_")}

        doc["versions_canonical"] = it["_versions"]

        owner, repo_name, repo_url = parse_repo_fields(str(doc.get("repo", "")))
        if owner:
            doc["owner"] = owner
        if repo_name:
            doc["repo_name"] = repo_name
        if repo_url:
            doc["repo_url"] = repo_url
        if it["_creators"]:
            doc["creator_slug"] = it["_creators"][0].lower()

        all_docs.append(doc)

        item_path = API / "items" / f"{slugify(slug)}.json"
        write_json(item_path, doc)

        search_index.append({
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
            "feature_counts": doc.get("feature_counts", {"total": 0, "modules": 0, "hud_elements": 0}),
            "feature_names": [f.get("name") for f in (doc.get("features") or []) if isinstance(f, dict) and f.get("name")],
        })

    # 7) Buckets
    for v in versions_list:
        bucket = [{k: val for k, val in it.items() if not k.startswith("_")} for it in enriched if v in it["_versions"]]
        write_json(API / "by-version" / f"{slugify(v)}.json", bucket)

    for c in creators_count.keys():
        bucket = [{k: val for k, val in it.items() if not k.startswith("_")} for it in enriched if c in it["_creators"]]
        write_json(API / "by-creator" / f"{slugify(c)}.json", bucket)

    # 8) meta.json
    meta = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "generated/json/plugins-and-themes.json",
        "plugin_modules_source": "generated/json/plugin-modules.json" if MODULES_SRC.exists() else None,
        "counts": {
            "plugins": len(plugins),
            "themes": len(themes),
            "items_total": len(items),
        },
        "versions_canonical": versions_list,
    }
    write_json(API / "meta.json", meta)

    # 9) search-index.json
    write_json(API / "search-index.json", search_index)

    # 10) new.json / recent.json
    new_candidates: List[Tuple[datetime, Dict[str, Any]]] = []
    recent_candidates: List[Tuple[datetime, Dict[str, Any]]] = []

    for doc in all_docs:
        added_dt = _parse_iso_date(doc.get("added_at"))
        updated_dt = _parse_iso_date(doc.get("updated_at"))

        if added_dt is not None:
            new_candidates.append((added_dt, doc))

        key_dt = updated_dt or added_dt
        if key_dt is not None:
            recent_candidates.append((key_dt, doc))

    new_candidates.sort(key=lambda pair: pair[0], reverse=True)
    recent_candidates.sort(key=lambda pair: pair[0], reverse=True)

    new_docs = [doc for _, doc in new_candidates]
    recent_docs = [doc for _, doc in recent_candidates]

    write_json(API / "new.json", new_docs)
    write_json(API / "recent.json", recent_docs)

    # 11) manifest.json
    manifest_entries = []
    for p in WRITTEN:
        try:
            rel = p.relative_to(API)
        except ValueError:
            continue
        manifest_entries.append({
            "path": str(rel).replace(os.sep, "/"),
            "bytes": os.path.getsize(p),
            "sha256": sha256_file(p),
        })
    write_json(API / "manifest.json", {"files": sorted(manifest_entries, key=lambda x: x["path"])})


if __name__ == "__main__":
    main()
