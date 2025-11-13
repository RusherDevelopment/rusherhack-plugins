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
    data = yaml.safe_load(f) or {}

plugins: List[Dict[str, Any]] = data.get("plugins", []) or []
themes: List[Dict[str, Any]] = data.get("themes", []) or []

# -----------------------
# Helpers
# -----------------------

def clean_description(desc: str) -> str:
    """Remove embedded images from description to keep markdown tidy."""
    desc = desc or ""
    return re.sub(r"!\[.*?\]\(.*?\)", "", desc).strip()

def safe_repo(entry: Dict[str, Any]) -> str:
    return entry.get("repo", "").strip()

def first_screenshot_url(entry: Dict[str, Any]) -> str:
    """Return the first screenshot URL, or a GitHub OG fallback."""
    screenshots = entry.get("screenshots") or []
    if isinstance(screenshots, list) and screenshots:
        first = screenshots[0] or {}
        url = first.get("url") or ""
        if isinstance(url, str) and url.strip():
            return url.strip()
    repo = safe_repo(entry)
    if repo:
        # Fallback: GitHub OpenGraph image
        return f"https://opengraph.githubassets.com/1/{repo}"
    return ""

def parse_added_at(entry: Dict[str, Any]) -> datetime:
    """Parse added_at (YYYY-MM-DD). Missing/invalid dates sort to the oldest."""
    raw = entry.get("added_at")
    if not raw or not isinstance(raw, str):
        return datetime.min
    try:
        return datetime.fromisoformat(raw.strip())
    except ValueError:
        return datetime.min

# -----------------------
# Markdown generator for each plugin/theme entry
# -----------------------

def generate_entry_md(entry: Dict[str, Any], is_plugin: bool = True, index: int = 0) -> str:
    repo = safe_repo(entry)

    # Badge: repo release date (links to releases page)
    latest_release_badge = (
        f"[![Latest Release Date]"
        f"(https://img.shields.io/github/release-date/{repo}?label=Latest%20Release&color=green)]"
        f"(https://github.com/{repo}/releases)"
    )

    # Downloads badge image is repo-wide total; the LINK now uses jar_url (or latest release page)
    downloads_link = entry.get("jar_url") or f"https://github.com/{repo}/releases/latest"
    downloads_badge = (
        f"[![GitHub Downloads](https://img.shields.io/github/downloads/{repo}/total)]"
        f"({downloads_link})"
    )

    # Top line: name with repo link
    md = f"- ### [{entry['name']}](https://github.com/{repo}) <br>\n"
    md += f" {latest_release_badge} {downloads_badge}<br>\n"

    # MC version and core plugin badge (plugins only)
    if is_plugin and "mc_versions" in entry:
        mc_versions = str(entry["mc_versions"]).replace("-", "--").replace(".", "%20")
        md += f" ![MC Version](https://img.shields.io/badge/MC%20Version-{mc_versions}-blueviolet)<br>\n"
    if is_plugin and entry.get("is_core", False):
        md += " ![Core Plugin](https://img.shields.io/badge/Core%20Plugin-blue)<br>\n"

    # Creator section with avatar
    creator = entry.get("creator", {}) or {}
    avatar = creator.get("avatar", "") or ""
    creator_name = creator.get("name", "Unknown")
    creator_url = creator.get("url", "#")
    if avatar:
        md += f' **Creator**: <img src="{avatar}" width="20" height="20"> [{creator_name}]({creator_url})<br>\n'
    else:
        md += f" **Creator**: [{creator_name}]({creator_url})<br>\n"

    # Description (cleaned of embedded images)
    cleaned_description = clean_description(entry.get("description", ""))
    if cleaned_description:
        md += f" {cleaned_description}\n\n"

    # Screenshots section (standard and YouTube thumbnails)
    screenshots = entry.get("screenshots") or []
    if screenshots:
        md += " <details>\n <summary>Show Screenshots</summary>\n <p align=\"center\">\n"
        for ss in screenshots:
            url = ss.get("url", "") or ""
            alt = ss.get("alt", "") or ""
            width = ss.get("width", 250) or 250
            youtube_match = re.match(
                r"https://img\.youtube\.com/vi/([^/]+)/[^/]+\.jpg", url
            )
            if youtube_match:
                video_id = youtube_match.group(1)
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                md += (
                    f' <a href="{video_url}" target="_blank">'
                    f'<img src="{url}" alt="{alt}" width="{width}"></a>\n'
                )
            else:
                md += f' <img src="{url}" alt="{alt}" width="{width}">\n'
        md += " </p>\n </details>\n\n"

    md += "---\n\n"
    return md

# -----------------------
# Recently Added (card grid) for PLUGINS.md
# -----------------------

def generate_recent_card(entry: Dict[str, Any]) -> str:
    """
    Generate a single plugin card as a <td> with:
      - screenshot
      - name + 'plugin' label
      - description
      - stars / downloads / updated badges
    """
    repo = safe_repo(entry)
    name = entry.get("name", "Unknown Plugin")
    desc = clean_description(entry.get("description", ""))
    img_url = first_screenshot_url(entry)

    added_raw = entry.get("added_at") or ""
    added_display = added_raw
    mc_versions = entry.get("mc_versions")
    mc_display = str(mc_versions) if mc_versions else ""

    creator = entry.get("creator", {}) or {}
    creator_name = creator.get("name", "")

    parts = []
    parts.append('    <td valign="top" width="50%">')

    if img_url:
        parts.append(f'      <img src="{img_url}" alt="{name} preview" width="220"><br>')

    parts.append(
        f'      <a href="https://github.com/{repo}"><strong>{name}</strong></a> '
        f'<code>plugin</code><br>'
    )

    if desc:
        parts.append(f"      {desc}<br>")

    meta_bits = []
    if mc_display:
        meta_bits.append(f"<code>MC: {mc_display}</code>")
    if creator_name:
        meta_bits.append(f"by <strong>{creator_name}</strong>")
    if added_display:
        meta_bits.append(f"added <code>{added_display}</code>")
    if meta_bits:
        parts.append("      " + " · ".join(meta_bits) + "<br>")

    # Badge row (stars / downloads / updated)
    if repo:
        parts.append(
            f'      <img src="https://img.shields.io/github/stars/{repo}?style=flat&amp;label=stars"> '
            f'<img src="https://img.shields.io/github/downloads/{repo}/total?style=flat&amp;label=downloads"> '
            f'<img src="https://img.shields.io/github/release-date/{repo}?label=updated">'
        )

    parts.append("    </td>")
    return "\n".join(parts)

def generate_recent_section_md() -> str:
    """Build the full Recently Added Plugins section (header + 2-column card grid)."""
    if not plugins:
        return ""

    # Sort plugins by added_at (newest first) and take top 6
    sorted_plugins = sorted(
        plugins,
        key=parse_added_at,
        reverse=True,
    )
    recent = sorted_plugins[:6]

    if not recent:
        return ""

    rows: List[str] = []
    for i in range(0, len(recent), 2):
        left = generate_recent_card(recent[i])
        if i + 1 < len(recent):
            right = generate_recent_card(recent[i + 1])
        else:
            right = "    <td></td>"
        rows.append("  <tr>\n" + left + "\n" + right + "\n  </tr>")

    table_md = "<table>\n" + "\n".join(rows) + "\n</table>\n"

    header = (
        "## Recently Added Plugins\n\n"
        "These are the six most recently added plugins "
        "(based on the `added_at` field in `plugins-and-themes.yml`).\n\n"
    )

    return header + table_md + "\n"

# -----------------------
# Count plugin and theme entries
# -----------------------

plugin_count = len(plugins)
theme_count = len(themes)

# -----------------------
# Update PLUGINS.md
# -----------------------

with open("PLUGINS.md", "r", encoding="utf-8") as f:
    plugins_content = f.read()

# 1) Recently Added section (card grid)
recent_section_md = generate_recent_section_md()

plugins_content = re.sub(
    r"<!--- Recently Added Start -->.*<!--- Recently Added End -->",
    f"<!--- Recently Added Start -->\n{recent_section_md}<!--- Recently Added End -->",
    plugins_content,
    flags=re.DOTALL,
)

# 2) Full plugin entries
plugin_entries = "".join(
    generate_entry_md(p, is_plugin=True, index=i) for i, p in enumerate(plugins)
)

# Update plugin badge count
plugins_content = re.sub(
    r"\[!\[Plugins\].*?\]\(#plugins-list\)",
    f"[![Plugins](https://img.shields.io/badge/Plugins-{plugin_count}-green)](#plugins-list)",
    plugins_content,
)

# Inject plugin entries between comments
plugins_content = re.sub(
    r"<!--- Plugins Start -->.*<!--- Plugins End -->",
    f"<!--- Plugins Start -->\n{plugin_entries}<!--- Plugins End -->",
    plugins_content,
    flags=re.DOTALL,
)

with open("PLUGINS.md", "w", encoding="utf-8", newline="\n") as f:
    f.write(plugins_content)

# -----------------------
# Update THEMES.md
# -----------------------

with open("THEMES.md", "r", encoding="utf-8") as f:
    themes_content = f.read()

theme_entries = "".join(
    generate_entry_md(t, is_plugin=False, index=i) for i, t in enumerate(themes)
)

# Update theme badge count
themes_content = re.sub(
    r"\[!\[Themes\].*?\]\(#themes-list\)",
    f"[![Themes](https://img.shields.io/badge/Themes-{theme_count}-green)](#themes-list)",
    themes_content,
)

# Inject theme entries between comments
themes_content = re.sub(
    r"<!--- THEMES START -->.*<!--- THEMES END -->",
    f"<!--- THEMES START -->\n{theme_entries}<!--- THEMES END -->",
    themes_content,
    flags=re.DOTALL,
)

with open("THEMES.md", "w", encoding="utf-8", newline="\n") as f:
    f.write(themes_content)

# -----------------------
# Update badge counts in README.md
# -----------------------

with open("README.md", "r", encoding="utf-8") as f:
    readme_original = f.read()

readme_updated = re.sub(
    r"\[!\[Plugins\]\(.*?shields\.io/badge/Plugins-\d+-green.*?\)\]\([^)]+\)",
    f"[![Plugins](https://img.shields.io/badge/Plugins-{plugin_count}-green)](./PLUGINS.md)",
    readme_original,
    count=1,
)

readme_updated = re.sub(
    r"\[!\[Themes\]\(.*?shields\.io/badge/Themes-\d+-green.*?\)\]\([^)]+\)",
    f"[![Themes](https://img.shields.io/badge/Themes-{theme_count}-green)](./THEMES.md)",
    readme_updated,
    count=1,
)

# Only write if changes were made
if readme_original != readme_updated:
    with open("README.md", "w", encoding="utf-8", newline="\n") as f:
        f.write(readme_updated)
