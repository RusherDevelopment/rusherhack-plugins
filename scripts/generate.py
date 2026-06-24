# -----------------------------------------------------------
# Markdown Generator - plugins-and-themes.yml
# -----------------------------------------------------------
#
# Generates:
#   - PLUGINS.md
#   - THEMES.md
#   - README.md badge counts
#
# Relies on validated data from data/plugins-and-themes.yml.
#
# Usage:
#   python scripts/generate.py
#
# Created by: GarlicRot
# -----------------------------------------------------------

from __future__ import annotations

import html
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List
from urllib.parse import urlencode

import yaml

DATA_FILE = Path("data/plugins-and-themes.yml")
PLUGINS_MD = Path("PLUGINS.md")
THEMES_MD = Path("THEMES.md")
README_MD = Path("README.md")

PLUGIN_BLOCK_START = "<!--- Plugins Start -->"
PLUGIN_BLOCK_END = "<!--- Plugins End -->"

RECENT_BLOCK_START = "<!--- Recently Added Plugins Start -->"
RECENT_BLOCK_END = "<!--- Recently Added Plugins End -->"

THEMES_BLOCK_START = "<!--- THEMES START -->"
THEMES_BLOCK_END = "<!--- THEMES END -->"


# -----------------------
# Basic helpers
# -----------------------

def to_text(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return str(value)


def md_escape(value: Any) -> str:
    """
    Light Markdown/HTML-safe text escaping.
    """
    text = to_text(value).strip()
    return text.replace("<", "&lt;").replace(">", "&gt;")


def html_attr(value: Any) -> str:
    return html.escape(to_text(value), quote=True)


def md_url(value: Any) -> str:
    """
    Keep Markdown links from breaking on spaces or parentheses.
    """
    url = to_text(value).strip()
    return (
        url.replace(" ", "%20")
        .replace("(", "%28")
        .replace(")", "%29")
    )


def write_if_changed(path: Path, content: str) -> bool:
    old = path.read_text(encoding="utf-8") if path.exists() else ""

    if old == content:
        return False

    path.write_text(content, encoding="utf-8")
    return True


def replace_between_markers(
    content: str,
    start_marker: str,
    end_marker: str,
    replacement: str,
    label: str,
) -> str:
    pattern = re.compile(
        rf"{re.escape(start_marker)}.*?{re.escape(end_marker)}",
        flags=re.DOTALL,
    )

    new_content, count = pattern.subn(
        f"{start_marker}\n{replacement}{end_marker}",
        content,
        count=1,
    )

    if count != 1:
        raise RuntimeError(
            f"[generate] Could not replace {label}: expected exactly 1 marker block, found {count}."
        )

    return new_content


# -----------------------
# Dates
# -----------------------

def parse_date_safe(value: Any) -> datetime:
    """
    Parse ISO-ish date strings for added_at/updated_at.

    Returns datetime.min when missing/invalid so invalid dates sink to the bottom.
    """
    if not isinstance(value, str):
        return datetime.min

    text = value.strip()
    if not text:
        return datetime.min

    for fmt in (
        "%Y-%m-%d",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%dT%H:%M:%S.%fZ",
    ):
        try:
            parsed = datetime.strptime(text, fmt)
            if parsed.tzinfo is None:
                parsed = parsed.replace(tzinfo=timezone.utc)
            return parsed
        except ValueError:
            continue

    try:
        parsed = datetime.fromisoformat(text)
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed
    except Exception:
        return datetime.min


def date_to_unix(value: Any) -> int | None:
    parsed = parse_date_safe(value)

    if parsed == datetime.min:
        return None

    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)

    return int(parsed.timestamp())


# -----------------------
# Shields badge helpers
# -----------------------

def shield_static_badge(label: str, message: Any, color: str = "blueviolet") -> str:
    """
    Build a Shields static badge using query params instead of path params.

    This avoids badge breakage from:
      - commas
      - spaces
      - dots
      - parentheses
      - long Minecraft version lists
      - special characters
    """
    query = urlencode(
        {
            "label": label,
            "message": to_text(message).strip(),
            "color": color,
        }
    )

    return f"https://img.shields.io/static/v1?{query}"


def mc_versions_message(mc_versions: Any) -> str:
    if mc_versions is None:
        return ""

    if isinstance(mc_versions, list):
        return ", ".join(
            to_text(version).strip()
            for version in mc_versions
            if to_text(version).strip()
        )

    return to_text(mc_versions).strip()


def mc_versions_badge(mc_versions: Any) -> str:
    message = mc_versions_message(mc_versions)

    if not message:
        return ""

    badge_url = shield_static_badge("MC Version", message, "blueviolet")
    return f"![MC Version]({badge_url})"


# -----------------------
# Avatar helpers
# -----------------------

def is_github_avatar(url: str | None) -> bool:
    if not url:
        return False

    return ("avatars.githubusercontent.com" in url) or bool(
        re.search(r"github\.com/.+\.png$", url)
    )


def sharp_github_avatar(url: str, px: int = 400) -> str:
    """
    Force crisp GitHub avatars by requesting a larger size.
    """
    if not url:
        return url

    if "avatars.githubusercontent.com" in url:
        return url + (f"&s={px}" if "?" in url else f"?s={px}")

    if re.search(r"github\.com/.+\.png$", url):
        return url + (f"&size={px}" if "?" in url else f"?size={px}")

    return url


# -----------------------
# Recently added plugin cards
# -----------------------

def recent_plugins(entries: List[Dict[str, Any]], limit: int = 6) -> List[Dict[str, Any]]:
    plugins_only = [entry for entry in entries if isinstance(entry, dict)]
    plugins_only.sort(
        key=lambda entry: parse_date_safe(entry.get("added_at")),
        reverse=True,
    )
    return plugins_only[:limit]


def recent_items_for_cards(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []

    for entry in entries:
        repo = to_text(entry.get("repo")).strip()

        if not repo or "/" not in repo:
            continue

        creator = entry.get("creator") or {}
        creator_avatar = creator.get("avatar")

        if is_github_avatar(creator_avatar):
            creator_avatar = sharp_github_avatar(creator_avatar, 400)
        else:
            creator_avatar = None

        owner = repo.split("/", 1)[0]
        owner_avatar = f"https://avatars.githubusercontent.com/{owner}?s=400"

        items.append(
            {
                "repo": repo,
                "name": entry.get("name"),
                "desc": entry.get("description", ""),
                "creatorAvatar": creator_avatar,
                "ownerAvatar": owner_avatar,
                "addedUnix": date_to_unix(entry.get("added_at")),
            }
        )

    return items


def render_recent_cards(items: List[Dict[str, Any]]) -> str:
    if not items:
        return ""

    cells: List[str] = []

    for item in items:
        repo = to_text(item.get("repo")).strip()
        repo_url = f"https://github.com/{repo}"
        img = item.get("creatorAvatar") or item.get("ownerAvatar")
        name = html.escape(to_text(item.get("name") or repo.split("/", 1)[1]))
        desc = html.escape(to_text(item.get("desc") or "")) or "&nbsp;"
        added_unix = item.get("addedUnix")

        cell = f"""
<td align="left" valign="top" width="50%">
  <a href="{html_attr(repo_url)}"><img src="{html_attr(img)}" alt="{name}" width="100" height="100" style="border-radius:12px;"></a>
  <div><strong><a href="{html_attr(repo_url)}">{name}</a></strong>&nbsp;<code>plugin</code></div>
  <div style="margin:4px 0 6px 0;">{desc}</div>
  <div>
    <img alt="stars" src="https://img.shields.io/github/stars/{html_attr(repo)}?style=flat">
    &nbsp;<img alt="downloads" src="https://img.shields.io/github/downloads/{html_attr(repo)}/total?style=flat">"""

        if added_unix is not None:
            cell += f"""
    &nbsp;<img alt="added" src="https://img.shields.io/date/{added_unix}?label=added&style=flat">"""

        cell += """
  </div>
</td>""".rstrip()

        cells.append(cell)

    rows = [
        "<tr>" + "".join(cells[index : index + 2]) + "</tr>"
        for index in range(0, len(cells), 2)
    ]

    return "\n".join(["<table>", *rows, "</table>"])


def generate_recent_plugins_md(entries: List[Dict[str, Any]]) -> str:
    if not entries:
        return "No recently added plugins found.\n"

    cards_html = render_recent_cards(recent_items_for_cards(entries))

    return "\n".join(
        [
            "> These are the six most recently added plugins (based on `added_at`).",
            "",
            cards_html,
            "",
        ]
    )


# -----------------------
# Entry renderer
# -----------------------

def clean_description(description: Any) -> str:
    text = to_text(description)
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    return md_escape(text.strip())


def render_screenshots(screenshots: List[Dict[str, Any]]) -> str:
    if not screenshots:
        return ""

    lines = [
        ' <details>',
        ' <summary>Show Screenshots</summary>',
        ' <p align="center">',
    ]

    for screenshot in screenshots:
        url = to_text(screenshot.get("url")).strip()
        alt = html.escape(to_text(screenshot.get("alt")).strip())
        width = screenshot.get("width", 250)

        youtube_match = re.match(r"https://img\.youtube\.com/vi/([^/]+)/[^/]+\.jpg", url)

        if youtube_match:
            video_id = youtube_match.group(1)
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            lines.append(
                f' <a href="{html_attr(video_url)}" target="_blank"><img src="{html_attr(url)}" alt="{alt}" width="{html_attr(width)}"></a>'
            )
        else:
            lines.append(
                f' <img src="{html_attr(url)}" alt="{alt}" width="{html_attr(width)}">'
            )

    lines.extend(
        [
            " </p>",
            " </details>",
            "",
        ]
    )

    return "\n".join(lines)


def generate_entry_md(entry: Dict[str, Any], is_plugin: bool = True) -> str:
    repo = to_text(entry.get("repo")).strip()
    name = md_escape(entry.get("name") or repo)
    repo_url = f"https://github.com/{repo}"

    latest_release_badge = (
        f"[![Latest Release Date]"
        f"(https://img.shields.io/github/release-date/{repo}?label=Latest%20Release&color=green)]"
        f"({md_url(repo_url + '/releases')})"
    )

    downloads_link = entry.get("jar_url") or f"{repo_url}/releases/latest"
    downloads_badge = (
        f"[![GitHub Downloads](https://img.shields.io/github/downloads/{repo}/total)]"
        f"({md_url(downloads_link)})"
    )

    md = f"- ### [{name}]({md_url(repo_url)}) <br>\n"
    md += f" {latest_release_badge} {downloads_badge}<br>\n"

    if is_plugin and "mc_versions" in entry:
        badge = mc_versions_badge(entry.get("mc_versions"))
        if badge:
            md += f" {badge}<br>\n"

    if is_plugin and entry.get("is_core", False):
        md += " ![Core Plugin](https://img.shields.io/static/v1?label=Core&message=Plugin&color=blue)<br>\n"

    creator = entry.get("creator") or {}
    creator_avatar = to_text(creator.get("avatar")).strip()
    creator_name = md_escape(creator.get("name") or "Unknown")
    creator_url = md_url(creator.get("url") or "#")

    if creator_avatar:
        md += (
            f' **Creator**: <img src="{html_attr(creator_avatar)}" width="20" height="20"> '
            f"[{creator_name}]({creator_url})<br>\n"
        )
    else:
        md += f" **Creator**: [{creator_name}]({creator_url})<br>\n"

    description = clean_description(entry.get("description", ""))
    md += f" {description}\n\n"

    screenshots = entry.get("screenshots") or []
    if screenshots:
        md += render_screenshots(screenshots)
        md += "\n"

    md += "---\n\n"
    return md


# -----------------------
# Badge count updates
# -----------------------

def update_badge_count(
    content: str,
    label: str,
    count: int,
    target: str,
    anchor_label: str,
) -> tuple[str, int]:
    pattern = (
        rf"\[!\[{re.escape(label)}\]"
        rf"\(https://img\.shields\.io/badge/{re.escape(label)}-\d+-green\)"
        rf"\]\({re.escape(target)}\)"
    )

    replacement = (
        f"[![{label}](https://img.shields.io/badge/{label}-{count}-green)]({target})"
    )

    updated, count_replaced = re.subn(pattern, replacement, content, count=1)

    if count_replaced == 0:
        print(f"[generate] NOTE: {anchor_label} badge pattern not found.")

    return updated, count_replaced


# -----------------------
# Main generation
# -----------------------

def main() -> None:
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Missing data file: {DATA_FILE}")

    with DATA_FILE.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}

    plugins = data.get("plugins", []) or []
    themes = data.get("themes", []) or []

    plugin_count = len(plugins)
    theme_count = len(themes)

    # -----------------------
    # PLUGINS.md
    # -----------------------

    plugins_content = PLUGINS_MD.read_text(encoding="utf-8")

    plugin_entries = "".join(
        generate_entry_md(plugin, is_plugin=True)
        for plugin in plugins
    )

    plugins_content, plugin_badge_repl = update_badge_count(
        plugins_content,
        label="Plugins",
        count=plugin_count,
        target="#plugins-list",
        anchor_label="PLUGINS.md plugin count",
    )

    plugins_content = replace_between_markers(
        plugins_content,
        PLUGIN_BLOCK_START,
        PLUGIN_BLOCK_END,
        plugin_entries,
        "plugin list",
    )

    recent_block = generate_recent_plugins_md(recent_plugins(plugins, limit=6))

    plugins_content = replace_between_markers(
        plugins_content,
        RECENT_BLOCK_START,
        RECENT_BLOCK_END,
        recent_block,
        "recent plugins",
    )

    plugins_changed = write_if_changed(PLUGINS_MD, plugins_content)

    print(
        "[generate] PLUGINS.md "
        f"{'updated' if plugins_changed else 'unchanged'} "
        f"(badge={plugin_badge_repl})"
    )

    # -----------------------
    # THEMES.md
    # -----------------------

    themes_content = THEMES_MD.read_text(encoding="utf-8")

    theme_entries = "".join(
        generate_entry_md(theme, is_plugin=False)
        for theme in themes
    )

    themes_content, theme_badge_repl = update_badge_count(
        themes_content,
        label="Themes",
        count=theme_count,
        target="#themes-list",
        anchor_label="THEMES.md theme count",
    )

    themes_content = replace_between_markers(
        themes_content,
        THEMES_BLOCK_START,
        THEMES_BLOCK_END,
        theme_entries,
        "theme list",
    )

    themes_changed = write_if_changed(THEMES_MD, themes_content)

    print(
        "[generate] THEMES.md "
        f"{'updated' if themes_changed else 'unchanged'} "
        f"(badge={theme_badge_repl})"
    )

    # -----------------------
    # README.md badge counts
    # -----------------------

    readme_content = README_MD.read_text(encoding="utf-8")

    readme_content, readme_plugin_badge_repl = update_badge_count(
        readme_content,
        label="Plugins",
        count=plugin_count,
        target="./PLUGINS.md",
        anchor_label="README.md plugin count",
    )

    readme_content, readme_theme_badge_repl = update_badge_count(
        readme_content,
        label="Themes",
        count=theme_count,
        target="./THEMES.md",
        anchor_label="README.md theme count",
    )

    readme_changed = write_if_changed(README_MD, readme_content)

    print(
        "[generate] README.md "
        f"{'updated' if readme_changed else 'unchanged'} "
        f"(plugins_badge={readme_plugin_badge_repl}, themes_badge={readme_theme_badge_repl})"
    )


if __name__ == "__main__":
    main()
