![RusherHack Logo](https://avatars.githubusercontent.com/u/121969799?s=280&v=4)

# Contributing to the RusherHacks Plugin Collection

Thanks for helping improve the registry!  
**TL;DR: You only need to edit one file:** `data/plugins-and-themes.yml`.  
All pages, JSON, badges, and API files are generated automatically by our scripts and GitHub Actions.

---

## How it works

- **Source of truth:** `data/plugins-and-themes.yml`
- **Auto-generated outputs (no manual edits):**
  - `PLUGINS.md`, `THEMES.md`
  - `README` badges / counts
  - JSON under `generated/json/`
  - Static API under `api/v1/` (GitHub Pages)

When your PR is opened, **GitHub Actions validates the YAML** and **generates everything**.  
If something is wrong, the job will fail with a helpful error message.

---

## What you need to do

1. **Edit `data/plugins-and-themes.yml`**
   - Add a new entry **or** update an existing one.
   - Keep the existing structure and indentation.
2. **Open a Pull Request**
   - Use the PR template and check the box confirming you only changed the YAML.

> That’s it—no other files should be changed in your PR.

---

## Required fields (per entry)

- `name`: Display name  
- `repo`: GitHub repo (`owner/repo` format preferred)  
- `description`: One-line summary  
- `creator`: Object with `name`, `url`, `avatar`  
- `latest_release_tag`: Tag of the most recent release  
- `screenshots`: List of screenshots (each with `url`, `alt`, optional `width`)  
- `is_core`: Boolean (`true` if a core plugin)  
- `mc_versions`: Supported Minecraft versions (range or list)  
- `jar_url`: Direct download link to the release jar  

---

## Example entry

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
