import pathlib, shutil, json, sys, os

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC  = ROOT / "generated" / "json" / "plugins-and-themes.json"
API  = ROOT / "public" / "api" / "v1"

def ensure_src():
    if not SRC.exists():
        sys.stderr.write(f"[emit_static_api] SOURCE MISSING: {SRC}\n")
        sys.exit(1)

def copy_index():
    API.mkdir(parents=True, exist_ok=True)
    dst = API / "index.json"
    shutil.copyfile(SRC, dst)
    print(f"[emit_static_api] wrote {dst} ({os.path.getsize(dst)} bytes)")
    return dst

def write(path: pathlib.Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2))
    print(f"[emit_static_api] wrote {path} ({os.path.getsize(path)} bytes)")

def main():
    ensure_src()

    # 1) index.json (full)
    dst_index = copy_index()

    # 2) plugins.json & themes.json (simple split from index.json)
    data = json.loads(dst_index.read_text())

    plugins = data.get("plugins", [])
    themes  = data.get("themes",  [])

    write(API / "plugins.json", plugins)
    write(API / "themes.json",  themes)

if __name__ == "__main__":
    main()
