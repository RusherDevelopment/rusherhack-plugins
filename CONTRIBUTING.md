![RusherHack Logo](https://avatars.githubusercontent.com/u/121969799?s=280&v=4)

# Contributing to the RusherHack Plugin Collection

Thanks for helping improve the registry and website.

**TL;DR:**

- For registry updates, you usually only need to edit `data/plugins-and-themes.yml`
- For website updates, only edit the relevant files under `public_html/`
- Do not manually edit generated markdown, generated JSON, badges, or API output
- The static API is generated during the GitHub Pages deploy workflow

## How it works

- **Source of truth for plugin/theme data:** `data/plugins-and-themes.yml`
- **Committed website source:** `public_html/`
- **Auto-generated outputs:**
  - `PLUGINS.md`
  - `THEMES.md`
  - README badges / counts
  - JSON under `generated/json/`
- **Deploy-only generated output:**
  - Static API under `public/api/v1/` during GitHub Pages deploy

The live API is served at:

```text
https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/
```

> **Note**  
> `public/` is a temporary deploy artifact folder. Do not commit files under `public/`.
>
> `public_html/` is the committed website source folder. Do not commit generated API files under `public_html/api/`.

When your PR is opened or updated, GitHub Actions validates the PR changes and the YAML file automatically. If something is wrong, the checks will fail with a helpful error message.

After a YAML change is merged into `main`, GitHub Actions automatically regenerates the markdown and JSON output files. The static API is generated later during the GitHub Pages deploy workflow.

## Automatic update handling

Routine plugin and theme update maintenance is handled automatically by our scripts. This includes things like refreshing release metadata, generated outputs, and related registry files.

**You do not need to open a PR just to update:**

- `latest_release_tag`
- `jar_url`
- generated markdown files
- generated JSON files
- generated API files
- other auto-generated output files

PRs are mainly needed for:

- adding a new plugin or theme
- fixing or improving descriptions, screenshots, metadata, or structure in `data/plugins-and-themes.yml`
- correcting information the automation cannot determine on its own
- updating the plugin/theme search website under `public_html/`

## What you need to do

### For registry updates

1. **Edit `data/plugins-and-themes.yml`**
   - Add a new entry or update an existing one
   - Keep the existing structure and indentation
   - Use explicit comma-separated Minecraft versions for `mc_versions`

2. **Open a Pull Request**
   - Use the PR template
   - Mark it as a registry update

> No generated files need to be edited manually in your PR.

### For website updates

1. **Edit only the relevant website files under `public_html/`**
2. **Open a Pull Request**
   - Use the PR template
   - Mark it as a website update

> Do not edit `public/`. It is created during deployment.

## Allowed PR file changes

Contributor PRs may change:

- `data/plugins-and-themes.yml`
- `Assets/**`
- `public_html/**`

Contributor PRs should not change:

- `README.md`
- `PLUGINS.md`
- `THEMES.md`
- `generated/json/**`
- `public/**`
- `public_html/api/**`

Automation PRs may also update generated markdown and generated JSON files when using an approved automation branch.

## Required fields per registry entry

- `name`: Display name
- `repo`: GitHub repo, preferably in `owner/repo` format
- `description`: One-line summary
- `creator`: Object with `name`, `url`, and `avatar`
- `latest_release_tag`: Tag of the most recent release
- `screenshots`: List of screenshots, each with `url`, `alt`, and optional `width`
- `is_core`: Boolean, usually `false`
- `mc_versions`: Supported Minecraft versions as a comma-separated string
- `jar_url`: Direct download link to the release jar
- `added_at`: ISO date string for when the plugin/theme was added to the registry
- `updated_at`: ISO date string for the latest registry update

## Minecraft version format

Use explicit comma-separated versions:

```yaml
mc_versions: "1.21.4"
mc_versions: "1.20.1, 1.20.2, 1.21, 1.21.1, 1.21.4"
mc_versions: "N/A"
```

Do not use dash ranges:

```yaml
mc_versions: 1.20.1-1.21.4
```

## Example registry entry

```yaml
- name: 2b2t.vc RusherHack
  repo: rfresh2/2b2t.vc-rusherhack
  description: 2b2t data and statistics API commands and HUD.
  creator:
    name: rfresh2
    url: https://github.com/rfresh2
    avatar: https://github.com/rfresh2.png?size=20
  latest_release_tag: "1.12"
  screenshots:
    - url: ./Assets/2b2t.vc Rusherhack/HudSettings.png
      alt: Hud Setting
      width: 250
    - url: ./Assets/2b2t.vc Rusherhack/HudDisplay.png
      alt: Hud Display w/2b2t Queue
      width: 550
  is_core: false
  mc_versions: "1.20.1, 1.20.2, 1.21, 1.21.1, 1.21.4"
  jar_url: https://github.com/rfresh2/2b2t.vc-rusherhack/releases/download/1.12/2b2t.vc-rusherhack-1.12.jar
  added_at: 2025-02-18
  updated_at: 2025-02-18
```

## Screenshot guidelines

Screenshots should be stored in the `Assets/` folder when possible.

Recommended path format:

```text
Assets/Plugin Name/screenshot-name.png
```

Then reference it from the YAML like this:

```yaml
screenshots:
  - url: ./Assets/Plugin Name/screenshot-name.png
    alt: Short screenshot description
    width: 500
```

Use useful `alt` text so the generated pages and website are easier to browse.

## Notes for maintainers

Generated markdown and generated JSON can be refreshed by the repository workflows. The static API is generated during GitHub Pages deployment into the temporary `public/api/v1/` folder.

Do not commit generated API files.
