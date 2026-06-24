#!/usr/bin/env python3
import json
import os
import time
from pathlib import Path

import requests

JSON_PATH = Path("generated/json/plugins-and-themes.json")
TOKEN = os.getenv("GITHUB_TOKEN", "").strip()

HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "rusherhack-plugins-stats",
}

if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


def get_json(url):
    try:
        res = requests.get(url, headers=HEADERS, timeout=15)
        if res.status_code == 200:
            return res.json()
        print(f"[fetch-stats] GitHub returned {res.status_code}: {url}")
    except Exception as exc:
        print(f"[fetch-stats] Error fetching {url}: {exc}")
    return None


def get_github_stats(repo):
    stats = {
        "stars": 0,
        "downloads": 0,
    }

    repo_data = get_json(f"https://api.github.com/repos/{repo}")
    if isinstance(repo_data, dict):
        stats["stars"] = repo_data.get("stargazers_count", 0) or 0

    releases = get_json(f"https://api.github.com/repos/{repo}/releases?per_page=100")
    if isinstance(releases, list):
        stats["downloads"] = sum(
            asset.get("download_count", 0) or 0
            for release in releases
            for asset in release.get("assets", [])
        )

    return stats


def main():
    if not JSON_PATH.exists():
        print(f"[fetch-stats] JSON file not found: {JSON_PATH}")
        return

    data = json.loads(JSON_PATH.read_text(encoding="utf-8"))

    print("[fetch-stats] Fetching GitHub stats...")

    cache = {}

    for category in ("plugins", "themes"):
        for item in data.get(category, []):
            repo = item.get("repo", "").strip()

            if not repo or "/" not in repo:
                continue

            if repo not in cache:
                print(f"[fetch-stats] {repo}")
                cache[repo] = get_github_stats(repo)
                time.sleep(0.05)

            item["stars"] = cache[repo]["stars"]
            item["downloads"] = cache[repo]["downloads"]

    JSON_PATH.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    print("[fetch-stats] Stats updated successfully.")


if __name__ == "__main__":
    main()
