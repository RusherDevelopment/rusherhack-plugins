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
# - Contributor PRs may change:
#   - data/plugins-and-themes.yml
#   - Assets/**
#   - public_html/**
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
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Iterable

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

REGISTRY_ALLOWED = [
    "data/plugins-and-themes.yml",
    "Assets/**",
]

# Contributor website changes are allowed.
# Keep generated markdown/json/API output out of this list.
WEBSITE_ALLOWED = [
    "public_html/**",
]

# Generated output should only be changed by approved automation branches.
GENERATED_OUTPUT_ALLOWED = [
    "README.md",
    "PLUGINS.md",
    "THEMES.md",
    "generated/json/**",
    "public_html/api/v1/**",
]

CONTRIBUTOR_ALLOWED = [
    *REGISTRY_ALLOWED,
    *WEBSITE_ALLOWED,
]

AUTOMATION_ALLOWED = [
    *REGISTRY_ALLOWED,
    *WEBSITE_ALLOWED,
    *GENERATED_OUTPUT_ALLOWED,
]

AUTOMATION_BRANCHES = {
    "automation/repo-sync",
    "automation/top6-refresh",
}

AUTOMATION_BRANCH_PREFIXES = (
    "automation/",
)

AUTOMATION_ACTORS = {
    "github-actions[bot]",
    "dependabot[bot]",
}


def info(msg: str) -> str:
    return f"{BLUE}ℹ️ {msg}{RESET}"


def warn(msg: str) -> str:
    return f"{YELLOW}⚠️ {msg}{RESET}"


def err(msg: str) -> str:
    return f"{RED}❌ {msg}{RESET}"


def ok(msg: str) -> str:
    return f"{GREEN}✅ {msg}{RESET}"


def run_git(args: list[str], *, check: bool = True) -> str:
    result = subprocess.run(
        ["git", *args],
        capture_output=True,
        text=True,
    )

    if check and result.returncode != 0:
        print(err(f"Git command failed: git {' '.join(args)}"))

        if result.stdout.strip():
            print(result.stdout.strip())

        if result.stderr.strip():
            print(result.stderr.strip())

        sys.exit(1)

    return result.stdout.strip()


def normalize_path(path: str) -> str:
    return path.strip().replace("\\", "/")


def load_event_payload() -> dict:
    event_path = os.environ.get("GITHUB_EVENT_PATH", "").strip()

    if not event_path:
        return {}

    path = Path(event_path)

    if not path.exists():
        return {}

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(warn(f"Could not parse GITHUB_EVENT_PATH payload: {exc}"))
        return {}


def get_event_value(payload: dict, *keys: str) -> str:
    value = payload

    for key in keys:
        if not isinstance(value, dict) or key not in value:
            return ""
        value = value[key]

    return value if isinstance(value, str) else ""


def get_base_ref(payload: dict) -> str:
    return (
        os.environ.get("GITHUB_BASE_REF", "").strip()
        or get_event_value(payload, "pull_request", "base", "ref").strip()
    )


def get_head_ref(payload: dict) -> str:
    return (
        os.environ.get("GITHUB_HEAD_REF", "").strip()
        or get_event_value(payload, "pull_request", "head", "ref").strip()
    )


def get_actor(payload: dict) -> str:
    return (
        os.environ.get("GITHUB_ACTOR", "").strip()
        or get_event_value(payload, "sender", "login").strip()
    )


def fetch_base_branch(base_ref: str) -> None:
    """
    Ensure origin/<base_ref> exists locally.

    This makes the script reliable with checkout fetch-depth: 1.
    """
    run_git(
        [
            "fetch",
            "--no-tags",
            "--prune",
            "--depth=1",
            "origin",
            f"{base_ref}:refs/remotes/origin/{base_ref}",
        ]
    )


def get_changed_files(base_ref: str) -> list[str]:
    output = run_git(
        [
            "diff",
            "--name-only",
            "--diff-filter=ACMRDTUXB",
            f"origin/{base_ref}...HEAD",
        ]
    )

    if not output:
        return []

    return sorted(
        {
            normalize_path(line)
            for line in output.splitlines()
            if normalize_path(line)
        }
    )


def matches_any(path: str, patterns: Iterable[str]) -> bool:
    normalized = normalize_path(path)

    for pattern in patterns:
        normalized_pattern = normalize_path(pattern)

        if fnmatch.fnmatch(normalized, normalized_pattern):
            return True

    return False


def detect_pr_mode(head_ref: str, actor: str) -> str:
    if head_ref in AUTOMATION_BRANCHES:
        return "automation"

    if any(head_ref.startswith(prefix) for prefix in AUTOMATION_BRANCH_PREFIXES):
        return "automation"

    if actor in AUTOMATION_ACTORS and any(
        head_ref.startswith(prefix) for prefix in AUTOMATION_BRANCH_PREFIXES
    ):
        return "automation"

    return "contributor"


def print_allowed_files(mode: str, allowed: list[str]) -> None:
    label = "Automation" if mode == "automation" else "Contributor"

    print(f"\n{RED}{label} PRs may only change:{RESET}")
    for pattern in allowed:
        print(f"  - {pattern}")


def main() -> None:
    event_name = os.environ.get("GITHUB_EVENT_NAME", "").strip()
    payload = load_event_payload()

    if event_name and event_name != "pull_request":
        print(info(f"Skipping PR validation for non-PR event: {event_name}"))
        print(ok("PR validation skipped."))
        return

    base_ref = get_base_ref(payload)
    head_ref = get_head_ref(payload)
    actor = get_actor(payload)

    if not base_ref:
        print(err("Could not determine PR base branch. GITHUB_BASE_REF is not set."))
        sys.exit(1)

    mode = detect_pr_mode(head_ref=head_ref, actor=actor)
    allowed = AUTOMATION_ALLOWED if mode == "automation" else CONTRIBUTOR_ALLOWED

    print(info(f"PR mode: {mode}"))
    print(info(f"Base branch: {base_ref}"))
    print(info(f"Head branch: {head_ref or '<unknown>'}"))
    print(info(f"Actor: {actor or '<unknown>'}"))

    fetch_base_branch(base_ref)
    changed_files = get_changed_files(base_ref)

    if not changed_files:
        print(warn("No changed files detected in PR diff."))
        print(ok("PR file validation passed."))
        return

    print(info(f"Changed files ({len(changed_files)}):"))
    for path in changed_files:
        print(f"  - {path}")

    disallowed = [
        path
        for path in changed_files
        if not matches_any(path, allowed)
    ]

    if disallowed:
        print(f"\n{YELLOW}--- DISALLOWED FILE CHANGES ---{RESET}\n")

        for path in disallowed:
            print(err(path))

        print_allowed_files(mode, allowed)

        print(
            f"\n{RED}Fix this by moving unrelated changes to a separate PR, "
            f"or by using an approved automation branch if this is an automation update.{RESET}"
        )

        sys.exit(1)

    print(ok("PR file validation passed."))


if __name__ == "__main__":
    main()
