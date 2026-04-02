#!/usr/bin/env python3
# -----------------------------------------------------------
# YAML Validator - plugins-and-themes.yml
# -----------------------------------------------------------
#
# Validates the structure and format of:
#   data/plugins-and-themes.yml
#
# It checks:
# - top-level structure
# - required fields and types
# - duplicate names / repos
# - unknown fields
# - empty strings
# - URL/date formatting
# - screenshot structure
# - plugin-only fields like mc_versions / is_core
#
# Usage:
#   python scripts/validate-yml.py
#
# Created by: GarlicRot
# -----------------------------------------------------------

from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path
from typing import Any

import yaml

# ANSI color codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

YML_PATH = Path("data/plugins-and-themes.yml")

COMMON_REQUIRED_FIELDS = {
    "name": str,
    "repo": str,
    "description": str,
    "creator": dict,
    "screenshots": list,
}

PLUGIN_REQUIRED_FIELDS = {
    "mc_versions": str,
}

COMMON_OPTIONAL_FIELDS = {
    "latest_release_tag": str,
    "jar_url": str,
    "added_at": str,
    "updated_at": str,
    "mc_versions": str,
}

PLUGIN_OPTIONAL_FIELDS = {
    "is_core": bool,
}

REQUIRED_CREATOR_FIELDS = {
    "name": str,
    "url": str,
    "avatar": str,
}

ALLOWED_TOP_LEVEL_KEYS = {"plugins", "themes"}

REPO_REGEX = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
YOUTUBE_REGEX = re.compile(r"^https://img\.youtube\.com/vi/[^/]+/[^/]+\.jpg$")
DATE_REGEX = re.compile(r"^\d{4}-\d{2}-\d{2}$")
HTTPS_URL_REGEX = re.compile(r"^https://[^\s]+$")
ASSET_PATH_REGEX = re.compile(r"^\./Assets/.+")


def error(msg: str) -> str:
    return f"{RED}❌ {msg}{RESET}"


def warning(msg: str) -> str:
    return f"{YELLOW}⚠️ {msg}{RESET}"


def is_nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and value.strip() != ""


def is_valid_https_url(value: str) -> bool:
    return bool(HTTPS_URL_REGEX.match(value))


def is_valid_screenshot_url(value: str) -> bool:
    return bool(HTTPS_URL_REGEX.match(value)) or bool(ASSET_PATH_REGEX.match(value))


def is_valid_iso_date(value: str) -> bool:
    if not DATE_REGEX.match(value):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def validate_creator(creator: Any, kind: str, name: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(creator, dict):
        errors.append(error(f"`creator` must be a dictionary in {kind} '{name}'."))
        return errors, warnings

    unknown_keys = sorted(set(creator.keys()) - set(REQUIRED_CREATOR_FIELDS.keys()))
    if unknown_keys:
        errors.append(error(f"Unknown `creator` field(s) in {kind} '{name}': {', '.join(unknown_keys)}"))

    for field, expected_type in REQUIRED_CREATOR_FIELDS.items():
        if field not in creator:
            errors.append(error(f"Missing `creator.{field}` in {kind} '{name}'."))
            continue

        value = creator[field]
        if not isinstance(value, expected_type):
            errors.append(error(f"`creator.{field}` must be {expected_type.__name__} in {kind} '{name}'."))
            continue

        if not is_nonempty_string(value):
            errors.append(error(f"`creator.{field}` cannot be empty in {kind} '{name}'."))
            continue

        if field in {"url", "avatar"} and not is_valid_https_url(value):
            errors.append(error(f"`creator.{field}` must be a valid https:// URL in {kind} '{name}'."))

    return errors, warnings


def validate_screenshots(screenshots: Any, kind: str, name: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if not isinstance(screenshots, list):
        errors.append(error(f"`screenshots` must be a list in {kind} '{name}'."))
        return errors, warnings

    if len(screenshots) == 0:
        warnings.append(warning(f"`screenshots` is empty in {kind} '{name}'."))

    for idx, screenshot in enumerate(screenshots):
        label = f"{kind} '{name}' screenshot #{idx + 1}"

        if not isinstance(screenshot, dict):
            errors.append(error(f"{label} must be a dictionary."))
            continue

        unknown_keys = sorted(set(screenshot.keys()) - {"url", "alt", "width"})
        if unknown_keys:
            errors.append(error(f"{label} has unknown field(s): {', '.join(unknown_keys)}"))

        url = screenshot.get("url")
        if not isinstance(url, str) or not url.strip():
            errors.append(error(f"{label} is missing a valid `url`."))
        elif not is_valid_screenshot_url(url):
            errors.append(error(f"{label} `url` must start with https:// or ./Assets/."))
        elif url.startswith("https://img.youtube.com/") and not YOUTUBE_REGEX.match(url):
            errors.append(error(f"{label} YouTube thumbnail URL must match https://img.youtube.com/vi/<id>/<file>.jpg"))

        if "alt" in screenshot:
            if not isinstance(screenshot["alt"], str):
                errors.append(error(f"{label} `alt` must be a string."))
            elif not screenshot["alt"].strip():
                warnings.append(warning(f"{label} has an empty `alt` value."))

        if "width" in screenshot:
            if not isinstance(screenshot["width"], int):
                errors.append(error(f"{label} `width` must be an integer."))
            elif screenshot["width"] <= 0:
                errors.append(error(f"{label} `width` must be greater than 0."))

    return errors, warnings


def validate_dates(entry: dict[str, Any], kind: str, name: str) -> list[str]:
    errors: list[str] = []

    for field in ("added_at", "updated_at"):
        if field not in entry:
            continue

        value = entry[field]
        if not isinstance(value, str):
            errors.append(error(f"`{field}` must be a string in {kind} '{name}'."))
        elif not is_valid_iso_date(value):
            errors.append(error(f"`{field}` must be a valid ISO date (YYYY-MM-DD) in {kind} '{name}'."))

    return errors


def validate_unknown_fields(entry: dict[str, Any], kind: str, name: str, is_plugin: bool) -> list[str]:
    allowed = set(COMMON_REQUIRED_FIELDS.keys()) | set(COMMON_OPTIONAL_FIELDS.keys())
    if is_plugin:
        allowed |= set(PLUGIN_REQUIRED_FIELDS.keys()) | set(PLUGIN_OPTIONAL_FIELDS.keys())

    unknown = sorted(set(entry.keys()) - allowed)
    if not unknown:
        return []

    return [error(f"Unknown field(s) in {kind} '{name}': {', '.join(unknown)}")]


def validate_common_fields(entry: dict[str, Any], kind: str, name: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for field, expected_type in COMMON_REQUIRED_FIELDS.items():
        if field not in entry:
            errors.append(error(f"Missing field `{field}` in {kind} '{name}'."))
            continue

        value = entry[field]
        if not isinstance(value, expected_type):
            errors.append(error(f"`{field}` must be {expected_type.__name__} in {kind} '{name}'."))
            continue

        if expected_type is str and not is_nonempty_string(value):
            errors.append(error(f"`{field}` cannot be empty in {kind} '{name}'."))

    repo = entry.get("repo")
    if isinstance(repo, str) and repo.strip() and not REPO_REGEX.match(repo):
        errors.append(error(f"`repo` must be in 'owner/repo' format in {kind} '{name}'."))

    description = entry.get("description")
    if isinstance(description, str) and description.strip() and len(description.strip()) < 10:
        warnings.append(warning(f"`description` is very short in {kind} '{name}'."))

    if "latest_release_tag" in entry:
        latest_release_tag = entry["latest_release_tag"]
        if not isinstance(latest_release_tag, str):
            errors.append(error(f"`latest_release_tag` must be a string in {kind} '{name}'."))

    if "jar_url" in entry:
        jar_url = entry["jar_url"]
        if not isinstance(jar_url, str):
            errors.append(error(f"`jar_url` must be a string in {kind} '{name}'."))
        elif not is_valid_https_url(jar_url):
            errors.append(error(f"`jar_url` must be a valid https:// URL in {kind} '{name}'."))

    creator_errors, creator_warnings = validate_creator(entry.get("creator"), kind, name)
    shot_errors, shot_warnings = validate_screenshots(entry.get("screenshots"), kind, name)

    errors.extend(creator_errors)
    errors.extend(shot_errors)
    errors.extend(validate_dates(entry, kind, name))
    warnings.extend(creator_warnings)
    warnings.extend(shot_warnings)

    return errors, warnings


def validate_plugin_fields(entry: dict[str, Any], name: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    if "mc_versions" not in entry:
        errors.append(error(f"Missing `mc_versions` in plugin '{name}'."))
    elif not isinstance(entry["mc_versions"], str):
        errors.append(error(f"`mc_versions` must be a string in plugin '{name}'."))
    elif not entry["mc_versions"].strip():
        errors.append(error(f"`mc_versions` cannot be empty in plugin '{name}'."))
    elif "," in entry["mc_versions"] and "-" in entry["mc_versions"]:
        warnings.append(warning(f"`mc_versions` mixes ranges and lists in plugin '{name}'. Make sure this is intentional."))

    if "is_core" in entry and not isinstance(entry["is_core"], bool):
        errors.append(error(f"`is_core` must be a boolean in plugin '{name}'."))

    return errors, warnings


def validate_entry(entry: Any, is_plugin: bool, index: int) -> tuple[list[str], list[str], str, str | None]:
    kind = "plugin" if is_plugin else "theme"

    if not isinstance(entry, dict):
        return [error(f"Entry #{index + 1} in `{kind}s` must be a dictionary.")], [], f"<Invalid {index}>", None

    name = entry.get("name", f"<Unnamed {index}>")
    repo = entry.get("repo") if isinstance(entry.get("repo"), str) else None

    errors: list[str] = []
    warnings: list[str] = []

    errors.extend(validate_unknown_fields(entry, kind, name, is_plugin))

    common_errors, common_warnings = validate_common_fields(entry, kind, name)
    errors.extend(common_errors)
    warnings.extend(common_warnings)

    if is_plugin:
        plugin_errors, plugin_warnings = validate_plugin_fields(entry, name)
        errors.extend(plugin_errors)
        warnings.extend(plugin_warnings)

    return errors, warnings, name, repo


def main() -> None:
    try:
        with YML_PATH.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(error(f"Failed to load YAML: {e}"))
        sys.exit(1)

    if not isinstance(data, dict):
        print(error("Top-level YAML must be a dictionary with `plugins` and `themes`."))
        sys.exit(1)

    unknown_top_keys = sorted(set(data.keys()) - ALLOWED_TOP_LEVEL_KEYS)
    if unknown_top_keys:
        print(error(f"Unknown top-level key(s): {', '.join(unknown_top_keys)}"))
        sys.exit(1)

    plugins = data.get("plugins", [])
    themes = data.get("themes", [])

    if not isinstance(plugins, list):
        print(error("Top-level `plugins` must be a list."))
        sys.exit(1)

    if not isinstance(themes, list):
        print(error("Top-level `themes` must be a list."))
        sys.exit(1)

    all_errors: list[str] = []
    all_warnings: list[str] = []

    seen_plugin_names: set[str] = set()
    seen_plugin_repos: set[str] = set()
    seen_theme_names: set[str] = set()
    seen_theme_repos: set[str] = set()

    for i, plugin in enumerate(plugins):
        errors, warnings, name, repo = validate_entry(plugin, is_plugin=True, index=i)
        all_errors.extend(errors)
        all_warnings.extend(warnings)

        if name in seen_plugin_names:
            all_errors.append(error(f"Duplicate plugin name: '{name}'"))
        else:
            seen_plugin_names.add(name)

        if repo:
            if repo in seen_plugin_repos:
                all_errors.append(error(f"Duplicate plugin repo: '{repo}'"))
            else:
                seen_plugin_repos.add(repo)

    for i, theme in enumerate(themes):
        errors, warnings, name, repo = validate_entry(theme, is_plugin=False, index=i)
        all_errors.extend(errors)
        all_warnings.extend(warnings)

        if name in seen_theme_names:
            all_errors.append(error(f"Duplicate theme name: '{name}'"))
        else:
            seen_theme_names.add(name)

        if repo:
            if repo in seen_theme_repos:
                all_errors.append(error(f"Duplicate theme repo: '{repo}'"))
            else:
                seen_theme_repos.add(repo)

    if all_warnings:
        print(f"\n{BLUE}--- VALIDATION WARNINGS ---{RESET}\n")
        for msg in all_warnings:
            print(msg)

    if all_errors:
        print(f"\n{YELLOW}--- VALIDATION ERRORS ---{RESET}\n")
        for msg in all_errors:
            print(msg)
        print(f"\n{RED}❌ {len(all_errors)} issue(s) found. Fix the above problems to continue.{RESET}")
        sys.exit(1)

    print(f"{GREEN}✅ plugins-and-themes.yml validation passed with no issues.{RESET}")
    if all_warnings:
        print(f"{YELLOW}⚠️ Validation passed with {len(all_warnings)} warning(s).{RESET}")


if __name__ == "__main__":
    main()
