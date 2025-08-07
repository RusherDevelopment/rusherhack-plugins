# -----------------------------------------------------------
# YAML to JSON Converter - plugins-and-themes.yml
# -----------------------------------------------------------
#
# Converts the validated YAML to JSON format.
# Output: generated/json/plugins-and-themes.json
#
# Usage:
#   python scripts/yml-to-json.py
#
# Created by: GarlicRot
# -----------------------------------------------------------

import yaml
import json
import os

INPUT_YML_PATH = 'data/plugins-and-themes.yml'
OUTPUT_JSON_DIR = 'generated/json'
OUTPUT_JSON_PATH = os.path.join(OUTPUT_JSON_DIR, 'plugins-and-themes.json')

# Ensure output folder exists
os.makedirs(OUTPUT_JSON_DIR, exist_ok=True)

# Load YAML
with open(INPUT_YML_PATH, 'r') as f:
    data = yaml.safe_load(f)

# Dump JSON
with open(OUTPUT_JSON_PATH, 'w') as f:
    json.dump(data, f, indent=2)

print(f"✅ JSON saved to {OUTPUT_JSON_PATH}")
