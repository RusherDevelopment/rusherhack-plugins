import pathlib, shutil, json, sys, os, re, urllib.parse, hashlib
from typing import Iterable, Dict, Any, List

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC  = ROOT / "generated" / "json" / "plugins-and-themes.json"
API  = ROOT / "public" / "api" / "v1"

# ---- Canonical Minecraft versions (order matters) ----
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
    """Natural sort for versions, e.g. '1.21.10' > '1.21.4'."""
    return [int(t) if t.isdigit() else str(s).lower() for t in re.split(r'(\d+)', str(s))]

def ensure_src():
    if not SRC.exists():
        sys.stderr.write(f"[emit_static_api] SOURCE MISSING: {SRC}\n")
        sys.exit(1)

def write_json(path: pathlib.Path, obj: Any):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2))
    print(f"[emit_static_api] wrote {path} ({os.path.getsize(path)} bytes)")

def copy_index() -> pathlib.Path:
    API.mkdir(parents=True, exist_ok=True)
    dst = API / "index.json"
    shutil.copyfile(SRC, dst)
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
        # keep 1.21 as "1.21" (no rounding)
        s = str(v)
        return s
    return str(v)

def _expand_range_token(tok: str) -> List[str]:
    """
    Expand 'a-b' where both are in CANON_VERSIONS. If not valid, return [].
    """
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
    """
    Normalize a single token into canonical versions:
    - '1.21.1-1.21.4' -> ['1.21.1','1.21.2','1.21.3','1.21.4']
    - '1.21' -> ['1.21'] if in canonical list
    - 'N/A' -> []
    - unknown values -> [] (ignored)
    """
    if not tok:
        return []
    s = tok.strip()
    if s.upper() == "N/A":
        return []

    if "-" in s:
        expanded = _expand_range_token(s)
        if expanded:
            return expanded
        return []  # unknown/unsupported range format

    # Single version (string that looks like a version OR numeric)
    # Only include if it's in the canonical set
    if s in CANON_INDEX:
        return [s]

    # Sometimes source may have numbers like 1.21 without quotes (handled above),
    # or versions outside our canonical set -> ignore.
    if _vers_token_re.match(s) and s in CANON_INDEX:
        return [s]

    return []

def item_versions(item: Dict[str, Any]) -> List[str]:
    """
    Return a normalized list of canonical versions for this item,
    expanding any ranges and ignoring N/A or unknown tokens.
    Accepts:
      - ["1.21.4", "1.21.1"]
      - "1.21.4"
      - 1.21
      - "1.20.1-1.21.4"
      - None / []
    """
    raw = item.get("mc_versions", None)
    if raw is None:
        raw = item.get("versions", [])

    out: List[str] = []

    # List case
    if isinstance(raw, list):
        for v in raw:
            s = _to_str(v)
            out.extend(_normalize_token(s))
        # de-dup while preserving order relative to canonical list
        out = sorted(set(out), key=lambda x: CANON_INDEX[x])
        return out

    # Scalar case: number or string
    s = _to_str(raw)
    out.extend(_normalize_token(s))
    out = sorted(set(out), key=lambda x: CANON_INDEX[x])
    return out

# ---------- Creators, slugs, etc. ----------

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

def item_slug(item: Dict[str, Any]) -> str:
    repo = item.get("repo") or item.get("repository")
    if repo:
        try:
            path = urllib.parse.urlparse(repo).path
            parts = [p for p in path.split("/") if p]
            if len(parts) >= 2:
                return f"{parts[0].lower()}/{parts[1].lower()}"
        except Exception:
            pass
    base = (item.get("id") or item.get("name") or "").strip().lower()
    base = re.sub(r"\s+", "-", base)
    if base:
        return base
    return stable_unknown_slug(item)

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
    # Sort by canonical order for keys we have; others won't be present.
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

    # 7) Per-item docs: /items/{owner}/{repo}.json (or fallback slug)
    for it in enriched:
        slug = it["_slug"]
        # Strip helper keys from the output (preserve original fields)
        doc = {k: v for k, v in it.items() if not k.startswith("_")}
        write_json(API / "items" / f"{slugify(slug)}.json", doc)

    # 8) Buckets (serverless filters) using normalized versions
    # by-version/{v}.json
    for v in versions_list:
        bucket = [{k: val for k, val in it.items() if not k.startswith("_")}
                  for it in enriched if v in it["_versions"]]
        write_json(API / "by-version" / f"{slugify(v)}.json", bucket)

    # by-creator/{name}.json
    for c in creators_count.keys():
        bucket = [{k: val for k, val in it.items() if not k.startswith("_")}
                  for it in enriched if c in it["_creators"]]
        write_json(API / "by-creator" / f"{slugify(c)}.json", bucket)

if __name__ == "__main__":
    main()
