# -----------------------------------------------------------
# Markdown Generator - plugins-and-themes.yml
# -----------------------------------------------------------
#
# This script generates the following markdown files:
#   - PLUGINS.md
#   - THEMES.md
#   - README.md (badges section only)
#
# Relies on the validated data from plugins-and-themes.yml.
# Should only be run after validate-yml.py passes.
#
# Usage:
#   python scripts/generate.py
#
# Created by: GarlicRot
# -----------------------------------------------------------

import yaml
import re
import os
from datetime import datetime
from typing import Any, Dict, List

# -----------------------
# Load YAML data
# -----------------------

with open("data/plugins-and-themes.yml", "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

# -----------------------
# Helpers
# -----------------------

def _parse_date_safe(s: str | None) -> datetime:
    """
    Parse ISO-ish date strings for added_at/updated_at.
    Falls back to datetime.min if missing/invalid so items without dates
    naturally sink to the bottom when sorting by "most recent".
    """
    if not s or not isinstance(s, str):
        return datetime.min
    s = s.strip()
    if not s:
        return datetime.min

    # Try a few common formats first
    for fmt in (
        "%Y-%m-%d",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%fZ",
    ):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue

    # Fallback: fromisoformat for other variants
    try:
        return datetime.fromisoformat(s)
    except Exception:
        return datetime.min


def _recent_plugins(entries: List[Dict[str, Any]], limit: int = 6) -> List[Dict[str, Any]]:
    """
    Return up to `limit` most recently added plugins by `added_at` (desc).
    If `added_at` is missing/invalid, that entry will sort as very old.
    """
    plugins_only = [e for e in entries if isinstance(e, dict)]
    plugins_only.sort(
        key=lambda e: _parse_date_safe(e.get("added_at")),
        reverse=True,
    )
    return plugins_only[:limit]


def _escape_inline(text: Any) -> str:
    """
    Light inline escaping/sanitizing for markdown text.
    Not for tables – just make sure we have a clean string.
    """
    if not isinstance(text, str):
        return ""
    return text.strip()


def md_escape(s: Any) -> str:
    """
    Match the Top 6 helper: escape < and > so HTML isn't broken.
    """
    s = s or ""
    if not isinstance(s, str):
        s = str(s)
    return s.replace("<", "&lt;").replace(">", "&gt;")


# ---------- Avatar helpers (same logic as Top 6 script) ----------

def _is_github_avatar(url: str) -> bool:
    if not url:
        return False
    return ("avatars.githubusercontent.com" in url) or bool(
        re.search(r"github\.com/.+\.png$", url)
    )


def _sharp_github_avatar(url: str, px: int = 400) -> str:
    """Force a crisp GitHub avatar by requesting a larger size, displayed at 100x100."""
    if not url:
        return url
    if "avatars.githubusercontent.com" in url:
        return url + (f"&s={px}" if "?" in url else f"?s={px}")
    if re.search(r"github\.com/.+\.png$", url):
        return url + (f"&size={px}" if "?" in url else f"?size={px}")
    return url


# ---------- Recently-added cards (Top-6 style) ----------

def _recent_items_for_cards(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Normalize YAML plugin entries into the mini dicts that our card
    renderer expects, mirroring the Top 6 structure:
      - repo, name, desc
      - creatorAvatar (hi-res GitHub if possible)
      - ownerAvatar fallback (GitHub owner avatar)
      - addedUnix: unix timestamp from added_at
    """
    items: List[Dict[str, Any]] = []
    for e in entries:
        repo = (e.get("repo") or "").strip()
        if not repo or "/" not in repo:
            continue

        creator = e.get("creator") or {}
        creator_avatar = creator.get("avatar")

        # Only keep creator avatar if it's GitHub-hosted (can request hi-res)
        if _is_github_avatar(creator_avatar):
            creator_avatar = _sharp_github_avatar(creator_avatar, 400)
        else:
            creator_avatar = None  # force fallback to owner avatar for sharpness

        owner = repo.split("/", 1)[0]
        owner_avatar = f"https://avatars.githubusercontent.com/{owner}?s=400"

        # Date -> unix for "added" badge
        added_at_raw = e.get("added_at")
        dt = _parse_date_safe(added_at_raw) if added_at_raw else datetime.min
        added_unix = int(dt.timestamp()) if dt != datetime.min else None

        items.append(
            {
                "repo": repo,
                "name": e.get("name"),
                "desc": e.get("description", ""),
                "creatorAvatar": creator_avatar,
                "ownerAvatar": owner_avatar,
                "addedUnix": added_unix,
            }
        )
    return items


def _render_recent_cards(items: List[Dict[str, Any]]) -> str:
    """
    Render a list of items using the exact same layout as the Top 6
    cards in README (avatar, title + `plugin`, description, badges),
    but using `addedUnix` for a green 'added' date badge.
    """
    if not items:
        return ""

    TWO_COL_WIDTH = "50%"
    cells: List[str] = []

    for t in items:
        # Prefer creator avatar only if it's GitHub-hosted (sharp). Otherwise use owner avatar (400px).
        img = t.get("creatorAvatar") or t.get("ownerAvatar")
        repo = t["repo"]
        name = md_escape(t.get("name") or repo.split("/")[1])
        desc = md_escape(t.get("desc") or "")

        added_unix = t.get("addedUnix")

        cell = f"""
<td align="left" valign="top" width="{TWO_COL_WIDTH}">
  <a href="https://github.com/{repo}"><img src="{img}" alt="{name}" width="100" height="100" style="border-radius:12px;"></a>
  <div><strong><a href="https://github.com/{repo}">{name}</a></strong>&nbsp;<code>plugin</code></div>
  <div style="margin:4px 0 6px 0;">{(desc or "&nbsp;")}</div>
  <div>
    <img alt="stars" src="https://img.shields.io/github/stars/{repo}?style=flat">
    &nbsp;<img alt="downloads" src="https://img.shields.io/github/downloads/{repo}/total?style=flat">"""
        if added_unix is not None:
            cell += f"""
    &nbsp;<img alt="added" src="https://img.shields.io/date/{added_unix}?label=added&style=flat">"""
        cell += """
  </div>
</td>""".rstrip()

        cells.append(cell)

    rows = ["<tr>" + "".join(cells[i : i + 2]) + "</tr>" for i in range(0, len(cells), 2)]
    return "\n".join(["<table>", *rows, "</table>"])


def generate_recent_plugins_md(entries: List[Dict[str, Any]]) -> str:
    """
    Build the 'Recently Added Plugins' section content for PLUGINS.md.

    Injected between:
      <!--- Recently Added Plugins Start -->
      <!--- Recently Added Plugins End -->

    Renders as a 2-column card grid using the Top 6 card layout.
    """
    if not entries:
        return "No recently added plugins found.\n"

    items = _recent_items_for_cards(entries)
    cards_html = _render_recent_cards(items)

    lines: List[str] = []
    lines.append("> These are the six most recently added plugins (based on `added_at`).")
    lines.append("")
    lines.append(cards_html)
    lines.append("")
    return "\n".join(lines)


# -----------------------
# Markdown generator for each plugin/theme entry
# -----------------------

def generate_entry_md(entry, is_plugin: bool = True, index: int = 0) -> str:
    # Badge: repo release date (links to releases page)
    latest_release_badge = (
        f"[![Latest Release Date]"
        f"(https://img.shields.io/github/release-date/{entry['repo']}?label=Latest%20Release&color=green)]"
        f"(https://github.com/{entry['repo']}/releases)"
    )

    # Downloads badge image is repo-wide total; the LINK now uses jar_url (or latest release page)
    downloads_link = entry.get("jar_url") or f"https://github.com/{entry['repo']}/releases/latest"
    downloads_badge = (
        f"[![GitHub Downloads](https://img.shields.io/github/downloads/{entry['repo']}/total)]"
        f"({downloads_link})"
    )

    # Top line: name with repo link
    md = f"- ### [{entry['name']}](https://github.com/{entry['repo']}) <br>\n"
    md += f" {latest_release_badge} {downloads_badge}<br>\n"

    # MC version and core plugin badge (plugins only)
    if is_plugin and "mc_versions" in entry:
        mc_versions = entry["mc_versions"].replace("-", "--").replace(".", "%20")
        md += f" ![MC Version](https://img.shields.io/badge/MC%20Version-{mc_versions}-blueviolet)<br>\n"
    if is_plugin and entry.get("is_core", False):
        md += " ![Core Plugin](https://img.shields.io/badge/Core%20Plugin-blue)<br>\n"

    # Creator section with avatar
    creator = entry.get("creator", {})
    avatar = creator.get("avatar", "")
    creator_name = creator.get("name", "Unknown")
    creator_url = creator.get("url", "#")
    if avatar:
        md += f' **Creator**: <img src="{avatar}" width="20" height="20"> [{creator_name}]({creator_url})<br>\n'
    else:
        md += f" **Creator**: [{creator_name}]({creator_url})<br>\n"

    # Description (cleaned of embedded images)
    desc = entry.get("description", "")
    cleaned_description = re.sub(r"!\[.*?\]\(.*?\)", "", desc)
    md += f" {cleaned_description.strip()}\n\n"

    # Screenshots section (standard and YouTube thumbnails)
    screenshots = entry.get("screenshots") or []
    if screenshots:
        md += " <details>\n <summary>Show Screenshots</summary>\n <p align=\"center\">\n"
        for ss in screenshots:
            url = ss.get("url", "")
            alt = ss.get("alt", "")
            width = ss.get("width", 250)
            youtube_match = re.match(r"https://img\.youtube\.com/vi/([^/]+)/[^/]+\.jpg", url)
            if youtube_match:
                video_id = youtube_match.group(1)
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                md += (
                    f' <a href="{video_url}" target="_blank"><img src="{url}" alt="{alt}" '
                    f'width="{width}"></a>\n'
                )
            else:
                md += f' <img src="{url}" alt="{alt}" width="{width}">\n'
        md += " </p>\n </details>\n\n"

    md += "---\n\n"
    return md


# -----------------------
# Count plugin and theme entries
# -----------------------

plugin_count = len(data.get("plugins", []) or [])
theme_count = len(data.get("themes", []) or [])

# -----------------------
# Update PLUGINS.md
# -----------------------

with open("PLUGINS.md", "r", encoding="utf-8") as f:
    plugins_content = f.read()

plugin_entries = "".join(
    generate_entry_md(p, is_plugin=True, index=i)
    for i, p in enumerate(data.get("plugins", []) or [])
)

# Update plugin badge count (in PLUGINS.md itself)
plugins_content, badge_repl = re.subn(
    r"\[!\[Plugins\].*?\]\(#plugins-list\)",
    f"[![Plugins](https://img.shields.io/badge/Plugins-{plugin_count}-green)](#plugins-list)",
    plugins_content,
)
if badge_repl == 0:
    print("[generate] NOTE: Plugins badge pattern not found in PLUGINS.md (badge count not updated).")

# Inject plugin entries between comments
plugins_block_pattern = r"<!--- Plugins Start -->.*?<!--- Plugins End -->"
plugins_replacement = f"<!--- Plugins Start -->\n{plugin_entries}<!--- Plugins End -->"

plugins_content, plugins_block_repl = re.subn(
    plugins_block_pattern,
    plugins_replacement,
    plugins_content,
    flags=re.DOTALL,
)
if plugins_block_repl == 0:
    print("[generate] WARNING: 'Plugins Start/End' markers not found – plugin list not injected.")

# Inject "Recently Added Plugins" section (top 6 by added_at) as card grid
recent_plugins = _recent_plugins(data.get("plugins", []) or [], limit=6)
recent_md_block = generate_recent_plugins_md(recent_plugins)

recent_block_pattern = r"<!--- Recently Added Plugins Start -->.*?<!--- Recently Added Plugins End -->"
recent_replacement = (
    f"<!--- Recently Added Plugins Start -->\n"
    f"{recent_md_block}"
    f"<!--- Recently Added Plugins End -->"
)

plugins_content, recent_block_repl = re.subn(
    recent_block_pattern,
    recent_replacement,
    plugins_content,
    flags=re.DOTALL,
)
if recent_block_repl == 0:
    print("[generate] WARNING: 'Recently Added Plugins Start/End' markers not found – cards not injected.")

with open("PLUGINS.md", "w", encoding="utf-8") as f:
    f.write(plugins_content)

print(
    f"[generate] PLUGINS.md updated "
    f"(badge={badge_repl}, plugins_block={plugins_block_repl}, recent_block={recent_block_repl})"
)

# -----------------------
# Update THEMES.md
# -----------------------

with open("THEMES.md", "r", encoding="utf-8") as f:
    themes_content = f.read()

theme_entries = "".join(
    generate_entry_md(t, is_plugin=False, index=i)
    for i, t in enumerate(data.get("themes", []) or [])
)

# Update theme badge count
themes_content, theme_badge_repl = re.subn(
    r"\[!\[Themes\].*?\]\(#themes-list\)",
    f"[![Themes](https://img.shields.io/badge/Themes-{theme_count}-green)](#themes-list)",
    themes_content,
)
if theme_badge_repl == 0:
    print("[generate] NOTE: Themes badge pattern not found in THEMES.md (badge count not updated).")

# Inject theme entries between comments
themes_block_pattern = r"<!--- THEMES START -->.*?<!--- THEMES END -->"
themes_replacement = f"<!--- THEMES START -->\n{theme_entries}<!--- THEMES END -->"

themes_content, themes_block_repl = re.subn(
    themes_block_pattern,
    themes_replacement,
    themes_content,
    flags=re.DOTALL,
)
if themes_block_repl == 0:
    print("[generate] WARNING: 'THEMES START/END' markers not found – theme list not injected.")

with open("THEMES.md", "w", encoding="utf-8") as f:
    f.write(themes_content)

print(
    f"[generate] THEMES.md updated "
    f"(badge={theme_badge_repl}, themes_block={themes_block_repl})"
)

# -----------------------
# Update badge counts in README.md
# -----------------------

with open("README.md", "r", encoding="utf-8") as f:
    readme_original = f.read()

readme_updated, readme_plugins_repl = re.subn(
    r"\[!\[Plugins\]\(.*?shields\.io/badge/Plugins-\d+-green.*?\)\]\([^)]+\)",
    f"[![Plugins](https://img.shields.io/badge/Plugins-{plugin_count}-green)](./PLUGINS.md)",
    readme_original,
    count=1,
)

if readme_plugins_repl == 0:
    print("[generate] NOTE: Plugins badge pattern not found in README.md (no change).")

readme_updated, readme_themes_repl = re.subn(
    r"\[!\[Themes\]\(.*?shields\.io/badge/Themes-\d+-green.*?\)\]\([^)]+\)",
    f"[![Themes](https://img.shields.io/badge/Themes-{theme_count}-green)](./THEMES.md)",
    readme_updated,
    count=1,
)

if readme_themes_repl == 0:
    print("[generate] NOTE: Themes badge pattern not found in README.md (no change).")

# Only write if changes were made
if readme_original != readme_updated:
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_updated)
    print(
        f"[generate] README.md updated "
        f"(plugins_badge={readme_plugins_repl}, themes_badge={readme_themes_repl})"
    )
else:
    print("[generate] README.md unchanged (badge patterns may not have matched).")
