import pathlib, shutil, sys, os

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC  = ROOT / "generated" / "json" / "plugins-and-themes.json"
DST  = ROOT / "public" / "api" / "v1" / "index.json"

if not SRC.exists():
    sys.stderr.write(f"[emit_static_api] SOURCE MISSING: {SRC}\n")
    # Show tree for debugging
    for p in [ROOT, ROOT/"generated", ROOT/"generated/json"]:
        try:
            print(f"[ls] {p}")
            for child in sorted(p.iterdir()):
                print("  -", child)
        except Exception as e:
            print(f"[ls error] {p}: {e}")
    sys.exit(1)

DST.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, DST)

size = os.path.getsize(DST)
print(f"[emit_static_api] Copied {SRC} -> {DST} ({size} bytes)")
