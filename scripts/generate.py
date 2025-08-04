import yaml
import re
import os

# -----------------------
# Load YAML data
# -----------------------
with open('data/plugins-and-themes.yml', 'r') as f:
    data = yaml.safe_load(f)

# -----------------------
# Markdown generator for each plugin/theme entry
# -----------------------
def generate_entry_md(entry, is_plugin=True, index=0):
    owner, repo_name = entry['repo'].split('/')
    sanitized_name = entry['name'].replace(' ', '%20')

    md = f"- ### [{entry['name']}](https://github.com/{entry['repo']}) <br>\n"
    md += f" [![Latest Release Date](https://img.shields.io/github/release-date/{entry['repo']}?label=Latest%20Release&color=green)](https://github.com/{entry['repo']}/releases) "
    md += f"[![GitHub Downloads](https://img.shields.io/github/downloads/{entry['repo']}/total)](https://github.com/{entry['repo']}/releases/download/{entry.get('latest_release_tag', 'latest')}/{sanitized_name}.jar)<br>\n"

    if is_plugin and 'mc_versions' in entry:
        mc_versions = entry['mc_versions'].replace('-', '--').replace('.', '%20')
        md += f" ![MC Version](https://img.shields.io/badge/MC%20Version-{mc_versions}-blueviolet)<br>\n"
    if is_plugin and entry.get('is_core', False):
        md += " ![Core Plugin](https://img.shields.io/badge/Core%20Plugin-blue)<br>\n"

    md += f" **Creator**: <img src=\"{entry['creator']['avatar']}\" width=\"20\" height=\"20\"> [{entry['creator']['name']}]({entry['creator']['url']})<br>\n"

    cleaned_description = re.sub(r'!\[.*?\]\(.*?\)', '', entry['description'])
    md += f" {cleaned_description.strip()}\n\n"

    if entry.get('screenshots'):
        md += " <details>\n <summary>Show Screenshots</summary>\n <p align=\"center\">\n"
        for ss in entry['screenshots']:
            youtube_match = re.match(r'https://img.youtube.com/vi/([^/]+)/\d+\.jpg', ss['url'])
            if youtube_match:
                video_id = youtube_match.group(1)
                video_url = f"https://www.youtube.com/watch?v={video_id}"
                md += f" <a href=\"{video_url}\" target=\"_blank\"><img src=\"{ss['url']}\" alt=\"{ss['alt']}\" width=\"{ss.get('width', 250)}\"></a>\n"
            else:
                md += f" <img src=\"{ss['url']}\" alt=\"{ss['alt']}\" width=\"{ss.get('width', 250)}\">\n"
        md += " </p>\n </details>\n\n"

    md += "---\n\n"
    return md

# -----------------------
# Count plugin and theme entries
# -----------------------
plugin_count = len(data.get("plugins", []))
theme_count = len(data.get("themes", []) or [])

# -----------------------
# Update PLUGINS.md
# -----------------------
with open('PLUGINS.md', 'r') as f:
    plugins_content = f.read()

plugin_entries = ''.join(generate_entry_md(p, is_plugin=True, index=i) for i, p in enumerate(data.get('plugins', [])))
plugins_content = re.sub(r'\[!\[Plugins\].*?\]\(#plugins-list\)',
                         f'[![Plugins](https://img.shields.io/badge/Plugins-{plugin_count}-green)](#plugins-list)',
                         plugins_content)

plugins_content = re.sub(r'<!--- Plugins Start -->.*<!--- Plugins End -->',
                         f'<!--- Plugins Start -->\n{plugin_entries}<!--- Plugins End -->',
                         plugins_content, flags=re.DOTALL)

with open('PLUGINS.md', 'w') as f:
    f.write(plugins_content)

# -----------------------
# Update THEMES.md
# -----------------------
with open('THEMES.md', 'r') as f:
    themes_content = f.read()

theme_entries = ''.join(generate_entry_md(t, is_plugin=False, index=i) for i, t in enumerate(data.get('themes', [])))
themes_content = re.sub(r'\[!\[Themes\].*?\]\(#themes-list\)',
                        f'[![Themes](https://img.shields.io/badge/Themes-{theme_count}-green)](#themes-list)',
                        themes_content)

themes_content = re.sub(r'<!--- THEMES START -->.*<!--- THEMES END -->',
                        f'<!--- THEMES START -->\n{theme_entries}<!--- THEMES END -->',
                        themes_content, flags=re.DOTALL)

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

if readme_original != readme_updated:
    with open('README.md', 'w') as f:
        f.write(readme_updated)
