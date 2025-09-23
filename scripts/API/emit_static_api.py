import pathlib, shutil, json, sys, os, re, urllib.parse, hashlib
from typing import Iterable, Dict, Any, List

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC  = ROOT / "generated" / "json" / "plugins-and-themes.json"
API  = ROOT / "public" / "api" / "v1"

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

def item_versions(item: Dict[str, Any]) -> List[str]:
    """
    Coerce mc_versions/versions into a list[str].
    Accepts: ["1.21.4", "1.21.1"], "1.21.4", 1.21, None, [].
    """
    vs = item.get("mc_versions", None)
    if vs is None:
        vs = item.get("versions", [])

    if isinstance(vs, (int, float)):
        return [str(vs)]
    if isinstance(vs, str):
        v = vs.strip()
        return [v] if v else []
    if isinstance(vs, list):
        out = []
        for v in vs:
            if v is None:
                continue
            if isinstance(v, (int, float)):
                out.append(str(v))
            elif isinstance(v, str) and v.strip():
                out.append(v.strip())
        return out
    return []

def item_creators(item: Dict[str, Any]) -> List[str]:
    """
    Extract creator names.
    Canonical shape: "creator": {"name": "..."}.
    Also supports optional "creators": ["..."].
    """
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
    """Deterministic fallback slug so we never emit /items/unknown.json."""
    raw = json.dumps(item, sort_keys=True, separators=(",", ":"))
    h = hashlib.sha1(raw.encode("utf-8")).hexdigest()[:10]
    return f"unknown-{h}"

def item_slug(item: Dict[str, Any]) -> str:
    """
    Prefer owner/repo from repo URL. Fallback to a name-based slug.
    If both are missing/empty, return a deterministic 'unknown-<sha1>'.
    """
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

    # 3) Aggregate stats
    items = get_items(data_full)

    byType = {
        "plugin": len(plugins),
        "theme":  len(themes),
    }

    byVersion: Dict[str, int] = {}
    versions_set = set()
    creators_count: Dict[str, int] = {}

    # Precompute per-item slugs and normalized fields we’ll reuse
    enriched: List[Dict[str, Any]] = []
    for it in items:
        versions = item_versions(it)
        creators = item_creators(it)
        slug = item_slug(it)

        for v in versions:
            versions_set.add(v)
            byVersion[v] = byVersion.get(v, 0) + 1
        for c in creators:
            creators_count[c] = creators_count.get(c, 0) + 1

        enriched.append({**it, "_slug": slug, "_versions": versions, "_creators": creators})

    # 4) stats.json
    stats = {
        "count": len(items),
        "byType": byType,
        "byVersion": dict(sorted(byVersion.items(), key=lambda kv: natural_key(kv[0]))),
        "creators": creators_count
    }
    write_json(API / "stats.json", stats)

    # 5) versions.json
    versions_list = sorted(versions_set, key=natural_key)
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
        # Strip the helper keys from the output (preserve source fields for schema flexibility)
        doc = {k: v for k, v in it.items() if not k.startswith("_")}
        write_json(API / "items" / f"{slugify(slug)}.json", doc)

    # 8) Buckets (serverless filters)
    # by-version/{v}.json
    for v in versions_list:
        bucket = [{k: val for k, val in it.items() if not k.startswith("_")}
                  for it in enriched if v in it["_versions"]]
        write_json(API / "by-version" / f"{slugify(v)}.json", bucket)

    # by-creator/{name}.json  (deduplicated: single loop using creators_count keys)
    for c in creators_count.keys():
        bucket = [{k: val for k, val in it.items() if not k.startswith("_")}
                  for it in enriched if c in it["_creators"]]
        write_json(API / "by-creator" / f"{slugify(c)}.json", bucket)

if __name__ == "__main__":
    main()
