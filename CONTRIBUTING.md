![RusherHack Logo](https://avatars.githubusercontent.com/u/121969799?s=280&v=4)

# Contributing to the RusherHacks Plugin Collection

Thanks for helping improve the registry and website.

**TL;DR:**  
- For registry updates, you usually only need to edit `data/plugins-and-themes.yml`
- For website updates, only edit the relevant website files
- Generated pages, JSON, badges, and API files are handled automatically

## How it works

- **Source of truth for plugin/theme data:** `data/plugins-and-themes.yml`
- **Auto-generated outputs (no manual edits):**
  - `PLUGINS.md`, `THEMES.md`
  - `README` badges / counts
  - JSON under `generated/json/`
  - Static API under `api/v1/` (GitHub Pages)

When your PR is opened or updated, **GitHub Actions validates the PR changes and the YAML file automatically**.  
If something is wrong, the checks will fail with a helpful error message.

After a YAML change is merged into `main`, GitHub Actions automatically regenerates the markdown and JSON output files.

## Automatic update handling

Routine plugin and theme update maintenance is handled automatically by our scripts.  
This includes things like refreshing release metadata, generated outputs, and related registry files.

**You do not need to open a PR just to update:**
- `latest_release_tag`
- `jar_url`
- generated markdown or JSON files
- other auto-generated output files

PRs are mainly needed for:
- adding a new plugin or theme
- fixing or improving descriptions, screenshots, metadata, or structure in `data/plugins-and-themes.yml`
- correcting information the automation cannot determine on its own
- updating the plugin/theme search website

## What you need to do

### For registry updates

1. **Edit `data/plugins-and-themes.yml`**
   - Add a new entry or update an existing one
   - Keep the existing structure and indentation

2. **Open a Pull Request**
   - Use the PR template and mark it as a registry update

> No generated files need to be edited manually in your PR.

### For website updates

1. **Edit only the relevant website files**
2. **Open a Pull Request**
   - Use the PR template and mark it as a website update

## Required fields (per registry entry)

- `name`: Display name  
- `repo`: GitHub repo (`owner/repo` format preferred)  
- `description`: One-line summary  
- `creator`: Object with `name`, `url`, `avatar`  
- `latest_release_tag`: Tag of the most recent release  
- `screenshots`: List of screenshots (each with `url`, `alt`, optional `width`)  
- `is_core`: Boolean (`true` if a core plugin)  
- `mc_versions`: Supported Minecraft versions (range or list)  
- `jar_url`: Direct download link to the release jar  
- `added_at`: ISO date string when the plugin was added to the registry  
- `updated_at`: ISO date string of the latest registry update (auto-managed by automation)

## Example registry entry

```yaml
- name: 2b2t.vc Rusherhack
  repo: rfresh2/2b2t.vc-rusherhack
  description: 2b2t data and statistics API commands and HUD.
  creator:
    name: rfresh2
    url: https://github.com/rfresh2
    avatar: https://github.com/rfresh2.png?size=20
  latest_release_tag: '1.12'
  screenshots:
    - url: ./Assets/2b2t.vc Rusherhack/HudSettings.png
      alt: Hud Setting
      width: 250
    - url: ./Assets/2b2t.vc Rusherhack/HudDisplay.png
      alt: Hud Display w/2b2t Queue
      width: 550
  is_core: false
  mc_versions: 1.20.1-1.21.4
  jar_url: https://github.com/rfresh2/2b2t.vc-rusherhack/releases/download/1.12/2b2t.vc-rusherhack-1.12.jar
  added_at: 2025-02-18
  updated_at: 2025-02-18
