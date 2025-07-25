import yaml
import re

# Load YAML
with open('data/plugins-and-themes.yml', 'r') as f:
    data = yaml.safe_load(f)

# Generate MD entry for plugins/themes
def generate_entry_md(entry, is_plugin=True, index=0):
    owner, repo_name = entry['repo'].split('/')
    sanitized_name = entry['name'].replace(' ', '%20')

    # Title + Badges (only once)
    md = f"- ### [{entry['name']}](https://github.com/{entry['repo']}) <br>\n"
    md += f"   [![Latest Release Date](https://img.shields.io/github/release-date/{entry['repo']}?label=Latest%20Release&color=green)](https://github.com/{entry['repo']}/releases) "
    md += f"[![GitHub Downloads](https://img.shields.io/github/downloads/{entry['repo']}/total)](https://github.com/{entry['repo']}/releases/download/{entry.get('latest_release_tag', 'latest')}/{sanitized_name}.jar)<br>\n"

    # MC version + core badge
    if is_plugin and 'mc_versions' in entry:
        mc_versions = entry['mc_versions'].replace('-', '--').replace('.', '%20')
        md += f"   ![MC Version](https://img.shields.io/badge/MC%20Version-{mc_versions}-blueviolet)<br>\n"

    if is_plugin and entry.get('is_core', False):
        md += "   ![Core Plugin](https://img.shields.io/badge/Core%20Plugin-blue)<br>\n"

    # Creator
    md += f"   **Creator**: <img src=\"{entry['creator']['avatar']}\" width=\"20\" height=\"20\"> [{entry['creator']['name']}]({entry['creator']['url']})<br>\n"
    
    # Description
    cleaned_description = re.sub(r'!\[.*?\]\(.*?\)', '', entry['description'])
    md += f"   {cleaned_description.strip()}\n\n"

    # Screenshots
    if entry.get('screenshots'):
        md += "   <details>\n   <summary>Show Screenshots</summary>\n   <p align=\"center\">\n"
        for ss in entry['screenshots']:
            md += f"     <img src=\"{ss['url']}\" alt=\"{ss['alt']}\" width=\"{ss.get('width', 250)}\">\n"
        md += "   </p>\n   </details>\n"

    md += "---\n\n"
    return md

# Update PLUGINS.md
with open('PLUGINS.md', 'r') as f:
    plugins_content = f.read()

# Generate plugin entries
plugin_entries = ''
for i, plugin in enumerate(data.get('plugins', [])):
    plugin_entries += generate_entry_md(plugin, is_plugin=True, index=i)

# Update Plugins badge count and plugin list section
plugins_content = re.sub(r'\[!\[Plugins\].*?\]\(#plugins-list\)', 
                         f'[![Plugins](https://img.shields.io/badge/Plugins-{len(data.get("plugins", []))}-green)](#plugins-list)', 
                         plugins_content)
plugins_content = re.sub(r'<!--- Plugins Start -->.*<!--- Plugins End -->', 
                         f'<!--- Plugins Start -->\n{plugin_entries}<!--- Plugins End -->', 
                         plugins_content, flags=re.DOTALL)

with open('PLUGINS.md', 'w') as f:
    f.write(plugins_content)

# Update THEMES.md
with open('THEMES.md', 'r') as f:
    themes_content = f.read()

# Generate theme entries
theme_entries = ''
themes = data.get('themes', []) or []
for i, theme in enumerate(themes):
    theme_entries += generate_entry_md(theme, is_plugin=False, index=i)

# Update Themes badge count and theme list section
themes_content = re.sub(r'\[!\[Themes\].*?\]\(#themes-list\)', 
                        f'[![Themes](https://img.shields.io/badge/Themes-{len(themes)}-green)](#themes-list)', 
                        themes_content)
themes_content = re.sub(r'<!--- THEMES START -->.*<!--- THEMES END -->', 
                        f'<!--- THEMES START -->\n{theme_entries}<!--- THEMES END -->', 
                        themes_content, flags=re.DOTALL)

with open('THEMES.md', 'w') as f:
    f.write(themes_content)
