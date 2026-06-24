#!/usr/bin/env python3
# -----------------------------------------------------------
# YAML to JSON Converter - plugins-and-themes.yml
# -----------------------------------------------------------
#
# Converts the validated YAML to JSON format.
#
# Input:
#   data/plugins-and-themes.yml
#
# Output:
#   generated/json/plugins-and-themes.json
#
# Usage:
#   python scripts/yml-to-json.py
#
# Created by: GarlicRot
# -----------------------------------------------------------

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml

INPUT_YML_PATH = Path("data/plugins-and-themes.yml")
OUTPUT_JSON_DIR = Path("generated/json")
OUTPUT_JSON_PATH = OUTPUT_JSON_DIR / "plugins-and-themes.json"


def load_yaml(path: Path) -> Any:
    if not path.exists():
        raise FileNotFoundError(f"Input YAML file does not exist: {path}")

    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def json_text(data: Any) -> str:
    return (
        json.dumps(
            data,
            indent=2,
            ensure_ascii=False,
        )
        + "\n"
    )


def write_if_changed(path: Path, content: str) -> bool:
    old_content = path.read_text(encoding="utf-8") if path.exists() else ""

    if old_content == content:
        return False

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return True


def main() -> None:
    try:
        data = load_yaml(INPUT_YML_PATH)
        output = json_text(data)
        changed = write_if_changed(OUTPUT_JSON_PATH, output)
    except Exception as exc:
        print(f"❌ Failed to convert YAML to JSON: {exc}")
        sys.exit(1)

    if changed:
        print(f"✅ JSON updated: {OUTPUT_JSON_PATH}")
    else:
        print(f"✅ JSON already up-to-date: {OUTPUT_JSON_PATH}")


if __name__ == "__main__":
    main()
