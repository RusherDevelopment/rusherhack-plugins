import pathlib, shutil, json, sys, os, re, urllib.parse, hashlib
from datetime import datetime, timezone
from typing import Dict, Any, List, Tuple

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC  = ROOT / "generated" / "json" / "plugins-and-themes.json"
API  = ROOT / "public" / "api" / "v1"

# Track written files for manifest
WRITTEN: List[pathlib.Path] = []

# ---- Canonical Minecraft versions  ----
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
    return [int(t) if t.isdigit() else str(s).lower() for t in re.split(r'(\d+)', str(s))]

def ensure_src():
    if not SRC.exists():
        sys.stderr.write(f"[emit_static_api] SOURCE MISSING: {SRC}\n")
        sys.exit(1)

def write_json(path: pathlib.Path, obj: Any):
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(obj, indent=2)
    path.write_text(data)
    WRITTEN.append(path)
    print(f"[emit_static_api] wrote {path} ({os.path.getsize(path)} bytes)")

def copy_index() -> pathlib.Path:
    API.mkdir(parents=True, exist_ok=True)
    dst = API / "index.json"
    shutil.copyfile(SRC, dst)
    WRITTEN.append(dst)
    print(f"[emit_static_api] wrote {dst} ({os.path.getsize(dst)} bytes)")
    return dst

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
            return CANON_VERSIONS[i:j+1]
        else:
            return CANON_VERSIONS[j:i+1]
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

    # de-dup & canonical order
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
    # Full URL path case
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
    # owner/repo case
    if "/" in s:
        owner, repo = s.split("/", 1)
        if owner and repo:
            return owner, repo, f"https://github.com/{owner}/{repo}"
    return "", "", ""

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

# ---------- Hashing for manifest ----------

def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def _parse_iso_date(val: Any) -> datetime | None:
    """
    Accepts 'YYYY-MM-DD' or ISO datetime; returns datetime or None.
    """
    if not val:
        return None
    s = str(val).strip()
    try:
        return datetime.fromisoformat(s)
    except ValueError:
        # Support "2024-10-23T12:34:56Z" style if it ever shows up
        if s.endswith("Z"):
            try:
                return datetime.fromisoformat(s[:-1] + "+00:00")
            except ValueError:
                return None
        return None

# ========================= main =========================

def main():
    ensure_src()

    # 1) Full dataset passthrough
    dst_index = copy_index()
    data_full = json.loads(dst_index.read_text())

    # 2) Simple splits (plugins/themes)
    plugins = data_full.get("plugins", [])
    themes  = data_full.get("themes", [])
    write_json(API / "plugins.json", plugins)
    write_json(API / "themes.json",  themes)

    # 3) Aggregate stats (using normalized, expanded versions)
    items = get_items(data_full)

    byType = {
        "plugin": len(plugins),
        "theme":  len(themes),
    }

    byVersion: Dict[str, int] = {}
    versions_present = set()
    creators_count: Dict[str, int] = {}

    # Precompute per-item slugs and normalized fields we’ll reuse
    enriched: List[Dict[str, Any]] = []
    for it in items:
        versions = item_versions(it)            # normalized to canonical list
        creators = item_creators(it)
        slug = item_slug(it)

        for v in versions:
            versions_present.add(v)
            byVersion[v] = byVersion.get(v, 0) + 1
        for c in creators:
            creators_count[c] = creators_count.get(c, 0) + 1

        enriched.append({**it, "_slug": slug, "_versions": versions, "_creators": creators})

    # 4) stats.json
    stats = {
        "count": len(items),
        "byType": byType,
        "byVersion": {v: byVersion[v] for v in CANON_VERSIONS if v in byVersion},
        "creators": creators_count
    }
    write_json(API / "stats.json", stats)

    # 5) versions.json (only the ones present)
    versions_list = [v for v in CANON_VERSIONS if v in versions_present]
    write_json(API / "versions.json", {"versions": versions_list})

    # 6) creators.json
    creators_list = sorted(
        [{"name": k, "count": v} for k, v in creators_count.items()],
        key=lambda x: (-x["count"], x["name"].lower())
    )
    write_json(API / "creators.json", {"creators": creators_list})

    # 7) Per-item docs + expose normalized fields to make consumption easier
    search_index: List[Dict[str, Any]] = []
    all_docs: List[Dict[str, Any]] = []

    for it in enriched:
        slug = it["_slug"]
        doc = {k: v for k, v in it.items() if not k.startswith("_")}  # preserve original shape
        # add normalized fields
        doc["versions_canonical"] = it["_versions"]
        owner, repo_name, repo_url = parse_repo_fields(str(doc.get("repo","")))
        if owner:
            doc["owner"] = owner
        if repo_name:
            doc["repo_name"] = repo_name
        if repo_url:
            doc["repo_url"] = repo_url
        if it["_creators"]:
            doc["creator_slug"] = it["_creators"][0].lower()

        all_docs.append(doc)

        # write per-item
        item_path = API / "items" / f"{slugify(slug)}.json"
        write_json(item_path, doc)

        # add to search index (compact)
        search_index.append({
            "name": doc.get("name"),
            "slug": slug,
            "description": doc.get("description", ""),
            "creator": (doc.get("creator") or {}).get("name"),
            "creator_slug": doc.get("creator_slug"),
            "tags": doc.get("tags") or [],
            "versions": doc.get("versions_canonical") or [],
            "repo": doc.get("repo"),
            "type": doc.get("type")
        })

    # 8) Buckets (serverless filters)
    for v in versions_list:
        bucket = [{k: val for k, val in it.items() if not k.startswith("_")}
                  for it in enriched if v in it["_versions"]]
        write_json(API / "by-version" / f"{slugify(v)}.json", bucket)

    for c in creators_count.keys():
        bucket = [{k: val for k, val in it.items() if not k.startswith("_")}
                  for it in enriched if c in it["_creators"]]
        write_json(API / "by-creator" / f"{slugify(c)}.json", bucket)

    # 9) meta.json
    meta = {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "generated/json/plugins-and-themes.json",
        "counts": {"plugins": len(plugins), "themes": len(themes), "items_total": len(items)},
        "versions_canonical": versions_list
    }
    write_json(API / "meta.json", meta)

    # 10) search-index.json (compact for client-side search)
    write_json(API / "search-index.json", search_index)

    # 11) new.json / recent.json based on added_at / updated_at
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

    # 12) manifest.json (sizes + sha256)
    manifest_entries = []
    for p in WRITTEN:
        # Only include files under API dir
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
