# -----------------------------------------------------------
# YAML Validator - plugins-and-themes.yml (Colored Output)
# -----------------------------------------------------------
#
# This script checks for missing or invalid fields in the
# plugins-and-themes.yml file and provides clear, helpful
# messages with colored output for GitHub Actions.
#
# Created by: GarlicRot
# -----------------------------------------------------------

import yaml
import re
import sys

# ANSI escape codes for colors (GitHub Actions supports these)
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BOLD = "\033[1m"
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

def colored_error(msg):
    return f"{RED}❌ {msg}{RESET}"

def validate_entry(entry, is_plugin=True, index=0):
    name = entry.get('name', f'<Unnamed {index}>')
    errors = []

    for field, field_type in REQUIRED_FIELDS.items():
        if field not in entry:
            errors.append(colored_error(f"Missing `{field}` — Add a `{field}` to the entry for {BOLD}{name}{RESET}."))
        elif not isinstance(entry[field], field_type):
            errors.append(colored_error(f"`{field}` must be a {field_type.__name__} in {BOLD}{name}{RESET}."))

    repo = entry.get('repo')
    if repo and not REPO_REGEX.match(repo):
        errors.append(colored_error(f"Invalid `repo` in {BOLD}{name}{RESET} — must be `owner/repo` format (e.g., GarlicRot/AutoBucket)."))

    creator = entry.get('creator', {})
    if not isinstance(creator, dict):
        errors.append(colored_error(f"`creator` must be a dictionary in {BOLD}{name}{RESET}."))
    else:
        for cfield, ctype in REQUIRED_CREATOR_FIELDS.items():
            if cfield not in creator:
                errors.append(colored_error(f"Missing `creator.{cfield}` in {BOLD}{name}{RESET}."))
            elif not isinstance(creator[cfield], ctype):
                errors.append(colored_error(f"`creator.{cfield}` must be a {ctype.__name__} in {BOLD}{name}{RESET}."))
            elif cfield in ['url', 'avatar'] and not creator[cfield].startswith("https://"):
                errors.append(colored_error(f"`creator.{cfield}` must start with https:// in {BOLD}{name}{RESET}."))

    for ss in entry.get('screenshots', []):
        if not isinstance(ss, dict):
            errors.append(colored_error(f"Screenshot in {BOLD}{name}{RESET} must be a dictionary."))
            continue
        if 'url' not in ss or not isinstance(ss['url'], str):
            errors.append(colored_error(f"Screenshot in {BOLD}{name}{RESET} is missing a `url`, or it's not a string."))
        elif not is_valid_screenshot_url(ss['url']):
            errors.append(colored_error(f"Screenshot `url` must start with `https://` or `./Assets/` in {BOLD}{name}{RESET}."))
        elif ss['url'].startswith("https://img.youtube.com/") and not YOUTUBE_REGEX.match(ss['url']):
            errors.append(colored_error(f"Invalid YouTube thumbnail URL in {BOLD}{name}{RESET} — must follow `https://img.youtube.com/vi/VIDEO_ID/0.jpg` format."))

        if 'alt' in ss and not isinstance(ss['alt'], str):
            errors.append(colored_error(f"Screenshot `alt` in {BOLD}{name}{RESET} must be a string."))
        if 'width' in ss and not isinstance(ss['width'], int):
            errors.append(colored_error(f"Screenshot `width` in {BOLD}{name}{RESET} must be an integer."))

    if is_plugin:
        if 'mc_versions' not in entry:
            errors.append(colored_error(f"Missing `mc_versions` in {BOLD}{name}{RESET} — e.g., '1.21.1-1.21.4'"))
        elif not isinstance(entry['mc_versions'], str):
            errors.append(colored_error(f"`mc_versions` must be a string in {BOLD}{name}{RESET}."))

        if 'is_core' in entry and not isinstance(entry['is_core'], bool):
            errors.append(colored_error(f"`is_core` must be true or false (boolean) in {BOLD}{name}{RESET}."))

    return errors

def main():
    try:
        with open('data/plugins-and-themes.yml', 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(colored_error(f"Failed to load YAML: {e}"))
        sys.exit(1)

    if not isinstance(data, dict):
        print(colored_error("Top-level YAML must be a dictionary with `plugins` and `themes`."))
        sys.exit(1)

    all_errors = []

    for i, plugin in enumerate(data.get("plugins", [])):
        all_errors.extend(validate_entry(plugin, is_plugin=True, index=i))

    for i, theme in enumerate(data.get("themes", [])):
        all_errors.extend(validate_entry(theme, is_plugin=False, index=i))

    if all_errors:
        print(f"\n{YELLOW}--- VALIDATION ERRORS ---{RESET}\n")
        for err in all_errors:
            print(err)
        print(f"\n{RED}Found {len(all_errors)} issue(s). Fix the above problems to continue.{RESET}")
        sys.exit(1)
    else:
        print(f"{GREEN}✅ plugins-and-themes.yml validation passed with no issues.{RESET}")

if __name__ == "__main__":
    main()
