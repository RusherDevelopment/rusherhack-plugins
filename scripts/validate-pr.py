#!/usr/bin/env python3
# -----------------------------------------------------------
# PR Validator
# -----------------------------------------------------------
#
# Validates which files were changed in a pull request.
#
# Intended for GitHub Actions on pull_request events.
#
# Rules:
# - Contributor PRs may only change:
#   - data/plugins-and-themes.yml
#   - Assets/**
#
# - Automation PRs may also change generated outputs:
#   - README.md
#   - PLUGINS.md
#   - THEMES.md
#   - generated/json/**
#   - api/v1/**
#
# Usage:
#   python scripts/validate-pr.py
#
# -----------------------------------------------------------

from __future__ import annotations

import fnmatch
import os
import subprocess
import sys
from typing import Iterable

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

CONTRIBUTOR_ALLOWED = [
    "data/plugins-and-themes.yml",
    "Assets/**",
]

AUTOMATION_ALLOWED = [
    "data/plugins-and-themes.yml",
    "Assets/**",
    "README.md",
    "PLUGINS.md",
    "THEMES.md",
    "generated/json/**",
    "api/v1/**",
]

AUTOMATION_BRANCHES = {
    "automation/repo-sync",
    "automation/top6-refresh",
}


def info(msg: str) -> str:
    return f"{BLUE}ℹ️ {msg}{RESET}"


def warn(msg: str) -> str:
    return f"{YELLOW}⚠️ {msg}{RESET}"


def err(msg: str) -> str:
    return f"{RED}❌ {msg}{RESET}"


def ok(msg: str) -> str:
    return f"{GREEN}✅ {msg}{RESET}"


def run_git(args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(err(f"Git command failed: git {' '.join(args)}"))
        if e.stderr:
            print(e.stderr.strip())
        sys.exit(1)


def get_changed_files(base_ref: str) -> list[str]:
    output = run_git(["diff", "--name-only", f"origin/{base_ref}...HEAD"])
    if not output:
        return []
    return [line.strip() for line in output.splitlines() if line.strip()]


def matches_any(path: str, patterns: Iterable[str]) -> bool:
    for pattern in patterns:
        if fnmatch.fnmatch(path, pattern):
            return True
    return False


def detect_pr_mode() -> str:
    head_ref = os.environ.get("GITHUB_HEAD_REF", "").strip()
    if head_ref in AUTOMATION_BRANCHES:
        return "automation"
    return "contributor"


def main() -> None:
    event_name = os.environ.get("GITHUB_EVENT_NAME", "").strip()
    base_ref = os.environ.get("GITHUB_BASE_REF", "").strip()

    if event_name and event_name != "pull_request":
        print(info(f"Skipping PR validation for non-PR event: {event_name}"))
        print(ok("PR validation skipped."))
        return

    if not base_ref:
        print(err("GITHUB_BASE_REF is not set. This script should run on pull_request events."))
        sys.exit(1)

    mode = detect_pr_mode()
    allowed = AUTOMATION_ALLOWED if mode == "automation" else CONTRIBUTOR_ALLOWED

    print(info(f"PR mode: {mode}"))
    print(info(f"Base branch: {base_ref}"))

    changed_files = get_changed_files(base_ref)

    if not changed_files:
        print(warn("No changed files detected in PR diff."))
        print(ok("PR file validation passed."))
        return

    print(info("Changed files:"))
    for path in changed_files:
        print(f"  - {path}")

    disallowed = [path for path in changed_files if not matches_any(path, allowed)]

    if disallowed:
        print(f"\n{YELLOW}--- DISALLOWED FILE CHANGES ---{RESET}\n")
        for path in disallowed:
            print(err(path))

        if mode == "contributor":
            print(
                f"\n{RED}Contributor PRs may only change:{RESET}\n"
                f"  - data/plugins-and-themes.yml\n"
                f"  - Assets/**"
            )
        else:
            print(
                f"\n{RED}Automation PRs may only change:{RESET}\n"
                f"  - data/plugins-and-themes.yml\n"
                f"  - Assets/**\n"
                f"  - README.md\n"
                f"  - PLUGINS.md\n"
                f"  - THEMES.md\n"
                f"  - generated/json/**\n"
                f"  - api/v1/**"
            )

        sys.exit(1)

    print(ok("PR file validation passed."))


if __name__ == "__main__":
    main()
