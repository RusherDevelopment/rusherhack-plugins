import pathlib, shutil

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "generated" / "json" / "plugins-and-themes.json"
DST = ROOT / "public" / "api" / "v1" / "index.json"

DST.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, DST)
print(f"Copied {SRC} -> {DST}")
