# -----------------------------------------------------------
# YAML Validator - plugins-and-themes.yml
# -----------------------------------------------------------
#
# This script validates the structure and format of the
# plugins-and-themes.yml file used to generate the markdown
# documentation files for plugins and themes.
#
# Ensures all required fields are present, properly typed,
# and correctly formatted. If validation fails, generation
# is aborted.
#
# Usage:
#   python scripts/validate-yml.py
#
# Created by: GarlicRot
# -----------------------------------------------------------

import yaml
import re
import sys

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# -----------------------
# Required field definitions
# -----------------------

REQUIRED_FIELDS = {
    'name': str,
    'repo': str,
    'description': str,
    'creator': dict,
    'latest_release_tag': str,
    'screenshots': list,
}

REQUIRED_CREATOR_FIELDS = {
    'name': str,
    'url': str,
    'avatar': str,
}

# -----------------------
# Regex patterns for validation
# -----------------------

REPO_REGEX = re.compile(r'^[\w\-]+/[\w\-\.]+$')
YOUTUBE_REGEX = re.compile(r'https://img\.youtube\.com/vi/([^/]+)/[^/]+\.jpg')

# -----------------------
# Screenshot helper
# -----------------------

def is_valid_screenshot_url(url: str) -> bool:
    return url.startswith("https://") or url.startswith("./Assets/")

# -----------------------
# Entry validation logic
# -----------------------

def validate_entry(entry, is_plugin=True, index=0):
    name = entry.get('name', f'<Unnamed {index}>')
    errors = []

    for field, field_type in REQUIRED_FIELDS.items():
        if field not in entry:
            errors.append(f"❌ Missing field `{field}` in '{name}'\n   ➤ Example: {field}: {field_type.__name__}")
        elif not isinstance(entry[field], field_type):
            example_value = "\"1.20.1-1.21.4\"" if field == "mc_versions" else field_type.__name__
            errors.append(f"❌ `{field}` must be {field_type.__name__} in '{name}'\n   ➤ Example: {field}: {example_value}")

    # Repo format check
    repo = entry.get('repo')
    if repo and not REPO_REGEX.match(repo):
        errors.append(f"❌ `repo` in '{name}' must follow format 'owner/repo'\n   ➤ Example: repo: \"GarlicRot/AutoBucket\"")

    # Creator block checks
    creator = entry.get('creator', {})
    if not isinstance(creator, dict):
        errors.append(f"❌ `creator` must be a dictionary in '{name}'")
    else:
        for cfield, ctype in REQUIRED_CREATOR_FIELDS.items():
            if cfield not in creator:
                errors.append(f"❌ Missing `creator.{cfield}` in '{name}'\n   ➤ Example: creator.{cfield}: \"https://github.com/user.png\"")
            elif not isinstance(creator[cfield], ctype):
                errors.append(f"❌ `creator.{cfield}` must be {ctype.__name__} in '{name}'")
            elif cfield in ['url', 'avatar'] and not creator[cfield].startswith("https://"):
                errors.append(f"❌ `creator.{cfield}` must start with https:// in '{name}'")

    # Screenshot block checks
    for ss in entry.get('screenshots', []):
        if not isinstance(ss, dict):
            errors.append(f"❌ Each screenshot must be a dictionary in '{name}'")
            continue

        if 'url' not in ss or not isinstance(ss['url'], str):
            errors.append(f"❌ Missing or invalid `url` in a screenshot of '{name}'")
        elif not is_valid_screenshot_url(ss['url']):
            errors.append(f"❌ Screenshot `url` in '{name}' must start with https:// or ./Assets/")
        elif ss['url'].startswith("https://img.youtube.com/") and not YOUTUBE_REGEX.match(ss['url']):
            errors.append(f"❌ YouTube thumbnail `url` in '{name}' must match: https://img.youtube.com/vi/<video-id>/0.jpg")

        if 'alt' in ss and not isinstance(ss['alt'], str):
            errors.append(f"❌ `alt` must be a string in screenshot of '{name}'")
        if 'width' in ss and not isinstance(ss['width'], int):
            errors.append(f"❌ `width` must be an integer in screenshot of '{name}'")

    # Plugin-only checks
    if is_plugin:
        if 'mc_versions' not in entry:
            errors.append(f"❌ Missing `mc_versions` in plugin '{name}'\n   ➤ Example: mc_versions: \"1.20.4-1.21.1\"")
        elif not isinstance(entry['mc_versions'], str):
            errors.append(f"❌ `mc_versions` must be a string in plugin '{name}'")

        if 'is_core' in entry and not isinstance(entry['is_core'], bool):
            errors.append(f"❌ `is_core` must be a boolean in plugin '{name}'")

    return errors

# -----------------------
# Entrypoint
# -----------------------

def main():
    try:
        with open('data/plugins-and-themes.yml', 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"{RED}❌ Failed to load YAML: {e}{RESET}")
        sys.exit(1)

    if not isinstance(data, dict):
        print(f"{RED}❌ Top-level YAML must be a dictionary with 'plugins' and 'themes'{RESET}")
        sys.exit(1)

    all_errors = []

    for i, plugin in enumerate(data.get("plugins", [])):
        all_errors.extend(validate_entry(plugin, is_plugin=True, index=i))

    for i, theme in enumerate(data.get("themes", [])):
        all_errors.extend(validate_entry(theme, is_plugin=False, index=i))

    if all_errors:
        print(f"{YELLOW}\n--- VALIDATION ERRORS ---{RESET}\n")
        for err in all_errors:
            print(err)
        print(f"\n{RED}❌ {len(all_errors)} issue(s) found. Fix the above problems to continue.{RESET}")
        sys.exit(1)
    else:
        print(f"{GREEN}✅ plugins-and-themes.yml validation passed with no issues.{RESET}")

if __name__ == "__main__":
    main()
