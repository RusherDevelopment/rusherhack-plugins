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

# ANSI color codes (used sparingly)
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

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

REPO_REGEX = re.compile(r'^[\w\-]+/[\w\-\.]+$')
YOUTUBE_REGEX = re.compile(r'https://img\.youtube\.com/vi/([^/]+)/[^/]+\.jpg')

def is_valid_screenshot_url(url: str) -> bool:
    return url.startswith("https://") or url.startswith("./Assets/")

def validate_entry(entry, is_plugin=True, index=0):
    name = entry.get('name', f'<Unnamed {index}>')
    errors = []

    for field, field_type in REQUIRED_FIELDS.items():
        if field not in entry:
            errors.append(
                f"{RED}❌ Missing field `{field}` in plugin '{name}'\n   ➤ Example: {field}: {field_type.__name__}{RESET}"
            )
        elif not isinstance(entry[field], field_type):
            example = "\"1.20.4-1.21.1\"" if field == "mc_versions" else f"{field_type.__name__}"
            errors.append(
                f"{RED}❌ `{field}` must be {field_type.__name__} in plugin '{name}'\n   ➤ Example: {field}: {example}{RESET}"
            )

    repo = entry.get('repo')
    if repo and not REPO_REGEX.match(repo):
        errors.append(f"{RED}❌ `repo` must be in 'owner/repo' format in plugin '{name}'\n   ➤ Example: repo: \"GarlicRot/AutoBucket\"{RESET}")

    creator = entry.get('creator', {})
    if not isinstance(creator, dict):
        errors.append(f"{RED}❌ `creator` must be a dictionary in plugin '{name}'{RESET}")
    else:
        for field, field_type in REQUIRED_CREATOR_FIELDS.items():
            if field not in creator:
                errors.append(
                    f"{RED}❌ Missing `creator.{field}` in plugin '{name}'\n   ➤ Example: creator.{field}: \"https://github.com/user.png\"{RESET}"
                )
            elif not isinstance(creator[field], field_type):
                errors.append(f"{RED}❌ `creator.{field}` must be {field_type.__name__} in plugin '{name}'{RESET}")
            elif field in ['url', 'avatar'] and not creator[field].startswith("https://"):
                errors.append(f"{RED}❌ `creator.{field}` must start with https:// in plugin '{name}'{RESET}")

    for screenshot in entry.get("screenshots", []):
        if not isinstance(screenshot, dict):
            errors.append(f"{RED}❌ Screenshot must be a dictionary in plugin '{name}'{RESET}")
            continue
        if "url" not in screenshot or not isinstance(screenshot["url"], str):
            errors.append(f"{RED}❌ Screenshot missing valid `url` in plugin '{name}'{RESET}")
        elif not is_valid_screenshot_url(screenshot["url"]):
            errors.append(f"{RED}❌ Screenshot `url` must start with https:// or ./Assets/ in plugin '{name}'{RESET}")
        elif screenshot["url"].startswith("https://img.youtube.com/") and not YOUTUBE_REGEX.match(screenshot["url"]):
            errors.append(f"{RED}❌ YouTube screenshot URL must match https://img.youtube.com/vi/<id>/hqdefault.jpg in plugin '{name}'{RESET}")
        if "alt" in screenshot and not isinstance(screenshot["alt"], str):
            errors.append(f"{RED}❌ Screenshot `alt` must be a string in plugin '{name}'{RESET}")
        if "width" in screenshot and not isinstance(screenshot["width"], int):
            errors.append(f"{RED}❌ Screenshot `width` must be an integer in plugin '{name}'{RESET}")

    if is_plugin:
        if "mc_versions" not in entry:
            errors.append(f"{RED}❌ Missing `mc_versions` in plugin '{name}'\n   ➤ Example: mc_versions: \"1.20.4-1.21.1\"{RESET}")
        elif not isinstance(entry["mc_versions"], str):
            errors.append(f"{RED}❌ `mc_versions` must be a string in plugin '{name}'\n   ➤ Example: mc_versions: \"1.20.4-1.21.1\"{RESET}")

        if "is_core" in entry and not isinstance(entry["is_core"], bool):
            errors.append(f"{RED}❌ `is_core` must be a boolean in plugin '{name}'{RESET}")

    return errors

def main():
    try:
        with open("data/plugins-and-themes.yml", "r") as f:
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
        print(f"\n{YELLOW}--- VALIDATION ERRORS ---{RESET}\n")
        for error in all_errors:
            print(error)
        print(f"\n{RED}❌ {len(all_errors)} issue(s) found. Fix the above problems to continue.{RESET}")
        sys.exit(1)
    else:
        print(f"{GREEN}✅ plugins-and-themes.yml validation passed with no issues.{RESET}")

if __name__ == "__main__":
    main()
