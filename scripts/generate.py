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

with open('data/plugins-and-themes.yml', 'r') as f:
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

def generate_recent_plugins_md(entries: List[Dict[str, Any]]) -> str:
    """
    Build the 'Recently Added Plugins' section content for PLUGINS.md.

    Injected between:
      <!--- Recently Added Plugins Start -->
      <!--- Recently Added Plugins End -->
    """
    if not entries:
        return "No recently added plugins found.\n"

    lines: List[str] = []
    lines.append("> These are the six most recently added plugins (based on `added_at`).")
    lines.append("")

    for idx, entry in enumerate(entries, start=1):
        name = _escape_inline(entry.get("name", "Unknown"))
        repo = entry.get("repo")
        desc = _escape_inline(entry.get("description", ""))
        mc = _escape_inline(entry.get("mc_versions", ""))

        creator_obj = entry.get("creator") or {}
        creator_name = _escape_inline(creator_obj.get("name", "Unknown"))
        creator_url = creator_obj.get("url")
        added_at = _escape_inline(entry.get("added_at", ""))

        if repo:
            name_md = f"[{name}](https://github.com/{repo})"
        else:
            name_md = name

        if creator_url:
            creator_md = f"[{creator_name}]({creator_url})"
        else:
            creator_md = creator_name

        meta_bits = []
        if mc:
            meta_bits.append(f"`MC: {mc}`")
        if creator_md:
            meta_bits.append(f"by {creator_md}")
        if added_at:
            meta_bits.append(f"added `{added_at}`")

        meta_line = " · ".join(meta_bits) if meta_bits else ""
        desc_part = f" – {desc}" if desc else ""

        lines.append(f"{idx}. **{name_md}**{desc_part}")
        if meta_line:
            lines.append(f"   {meta_line}")
        lines.append("")  # blank line between items

    return "\n".join(lines).rstrip() + "\n"

# -----------------------
# Markdown generator for each plugin/theme entry
# -----------------------

def generate_entry_md(entry, is_plugin=True, index=0):
    # Badge: repo release date (links to releases page)
    latest_release_badge = (
        f"[![Latest Release Date]"
        f"(https://img.shields.io/github/release-date/{entry['repo']}?label=Latest%20Release&color=green)]"
        f"(https://github.com/{entry['repo']}/releases)"
    )

    # Downloads badge image is repo-wide total; the LINK now uses jar_url (or latest release page)
    downloads_link = entry.get('jar_url') or f"https://github.com/{entry['repo']}/releases/latest"
    downloads_badge = (
        f"[![GitHub Downloads](https://img.shields.io/github/downloads/{entry['repo']}/total)]"
        f"({downloads_link})"
    )

    # Top line: name with repo link
    md = f"- ### [{entry['name']}](https://github.com/{entry['repo']}) <br>\n"
    md += f" {latest_release_badge} {downloads_badge}<br>\n"

    # MC version and core plugin badge (plugins only)
    if is_plugin and 'mc_versions' in entry:
        mc_versions = entry['mc_versions'].replace('-', '--').replace('.', '%20')
        md += f" ![MC Version](https://img.shields.io/badge/MC%20Version-{mc_versions}-blueviolet)<br>\n"
    if is_plugin and entry.get('is_core', False):
        md += " ![Core Plugin](https://img.shields.io/badge/Core%20Plugin-blue)<br>\n"

    # Creator section with avatar
    creator = entry.get('creator', {})
    avatar = creator.get('avatar', '')
    creator_name = creator.get('name', 'Unknown')
    creator_url = creator.get('url', '#')
    if avatar:
        md += f" **Creator**: <img src=\"{avatar}\" width=\"20\" height=\"20\"> [{creator_name}]({creator_url})<br>\n"
    else:
        md += f" **Creator**: [{creator_name}]({creator_url})<br>\n"

    # Description (cleaned of embedded images)
    desc = entry.get('description', '')
    cleaned_description = re.sub(r'!\[.*?\]\(.*?\)', '', desc)
    md += f" {cleaned_description.strip()}\n\n"

    # Screenshots section (standard and YouTube thumbnails)
    screenshots = entry.get('screenshots') or []
    if screenshots:
        md += " <details>\n <summary>Show Screenshots</summary>\n <p align=\"center\">\n"
        for ss in screenshots:
            url = ss.get('url', '')
            alt = ss.get('alt', '')
            width = ss.get('width', 250)
            youtube_match = re.match(r'https://img\.youtube\.com/vi/([^/]+)/[^/]+\.jpg', url)
            if youtube_match:
                video_id = youtube_match.group(1)
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                md += f" <a href=\"{video_url}\" target=\"_blank\"><img src=\"{url}\" alt=\"{alt}\" width=\"{width}\"></a>\n"
            else:
                md += f" <img src=\"{url}\" alt=\"{alt}\" width=\"{width}\">\n"
        md += " </p>\n </details>\n\n"

    md += "---\n\n"
    return md

# -----------------------
# Count plugin and theme entries
# -----------------------

plugin_count = len(data.get("plugins", []))
theme_count = len(data.get("themes", []))

# -----------------------
# Update PLUGINS.md
# -----------------------

with open('PLUGINS.md', 'r') as f:
    plugins_content = f.read()

plugin_entries = ''.join(
    generate_entry_md(p, is_plugin=True, index=i)
    for i, p in enumerate(data.get('plugins', []))
)

# Update plugin badge count
plugins_content = re.sub(
    r'\[!\[Plugins\].*?\]\(#plugins-list\)',
    f'[![Plugins](https://img.shields.io/badge/Plugins-{plugin_count}-green)](#plugins-list)',
    plugins_content
)

# Inject plugin entries between comments
plugins_content = re.sub(
    r'<!--- Plugins Start -->.*<!--- Plugins End -->',
    f'<!--- Plugins Start -->\n{plugin_entries}<!--- Plugins End -->',
    plugins_content,
    flags=re.DOTALL
)

# Inject "Recently Added Plugins" section (top 6 by added_at)
recent_plugins = _recent_plugins(data.get("plugins", []), limit=6)
recent_md_block = generate_recent_plugins_md(recent_plugins)

plugins_content = re.sub(
    r'<!--- Recently Added Plugins Start -->.*<!--- Recently Added Plugins End -->',
    f'<!--- Recently Added Plugins Start -->\n{recent_md_block}<!--- Recently Added Plugins End -->',
    plugins_content,
    flags=re.DOTALL
)

with open('PLUGINS.md', 'w') as f:
    f.write(plugins_content)

# -----------------------
# Update THEMES.md
# -----------------------

with open('THEMES.md', 'r') as f:
    themes_content = f.read()

theme_entries = ''.join(
    generate_entry_md(t, is_plugin=False, index=i)
    for i, t in enumerate(data.get('themes', []))
)

# Update theme badge count
themes_content = re.sub(
    r'\[!\[Themes\].*?\]\(#themes-list\)',
    f'[![Themes](https://img.shields.io/badge/Themes-{theme_count}-green)](#themes-list)',
    themes_content
)

# Inject theme entries between comments
themes_content = re.sub(
    r'<!--- THEMES START -->.*<!--- THEMES END -->',
    f'<!--- THEMES START -->\n{theme_entries}<!--- THEMES END -->',
    themes_content,
    flags=re.DOTALL
)

with open('THEMES.md', 'w') as f:
    f.write(themes_content)

# -----------------------
# Update badge counts in README.md
# -----------------------

with open('README.md', 'r') as f:
    readme_original = f.read()

readme_updated = re.sub(
    r'\[!\[Plugins\]\(.*?shields\.io/badge/Plugins-\d+-green.*?\)\]\([^)]+\)',
    f'[![Plugins](https://img.shields.io/badge/Plugins-{plugin_count}-green)](./PLUGINS.md)',
    readme_original,
    count=1
)

readme_updated = re.sub(
    r'\[!\[Themes\]\(.*?shields\.io/badge/Themes-\d+-green.*?\)\]\([^)]+\)',
    f'[![Themes](https://img.shields.io/badge/Themes-{theme_count}-green)](./THEMES.md)',
    readme_updated,
    count=1
)

# Only write if changes were made
if readme_original != readme_updated:
    with open('README.md', 'w') as f:
        f.write(readme_updated)
