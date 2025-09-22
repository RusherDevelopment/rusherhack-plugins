import pathlib, shutil, json, sys, os, re
from typing import Iterable, Dict, Any

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC  = ROOT / "generated" / "json" / "plugins-and-themes.json"
API  = ROOT / "public" / "api" / "v1"

def natural_key(s: str):
    # e.g., "1.20.1" > "1.21.4"
    return [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', s)]

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

def get_items(full: Dict[str, Any]) -> Iterable[Dict[str, Any]]:
    return list(full.get("plugins", [])) + list(full.get("themes", []))

def item_versions(item: Dict[str, Any]) -> Iterable[str]:
    vs = item.get("mc_versions") or item.get("versions") or []
    return [v for v in vs if isinstance(v, str) and v.strip()]

def item_creators(item: Dict[str, Any]) -> Iterable[str]:
    # Current shape: "creator": {"name": "..."}
    out = []
    creator = item.get("creator", {})
    if isinstance(creator, dict):
        name = creator.get("name")
        if isinstance(name, str) and name.strip():
            out.append(name.strip())
    # Support optional "creators": ["..."]
    creators = item.get("creators") or []
    for c in creators:
        if isinstance(c, str) and c.strip():
            out.append(c.strip())
    return out

def main():
    ensure_src()

    # 1) Full dataset passthrough
    dst_index = copy_index()
    data_full = json.loads(dst_index.read_text())

    # 2) Simple splits
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

    for it in items:
        for v in item_versions(it):
            versions_set.add(v)
            byVersion[v] = byVersion.get(v, 0) + 1
        for c in item_creators(it):
            creators_count[c] = creators_count.get(c, 0) + 1

    # 4) Emit stats.json
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

if __name__ == "__main__":
    main()
