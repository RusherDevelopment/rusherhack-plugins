![RusherHack Logo](https://avatars.githubusercontent.com/u/121969799?s=280&v=4)

# Plugin/Theme Submission or Metadata Update

Thank you for contributing to the RusherHacks Plugin Collection!  
Please fill out the details below to help keep review quick and clean.

## Summary of Changes

<!--
Briefly describe what this PR does:
- Add a new plugin or theme
- Update an existing YAML entry
- Fix metadata, screenshots, descriptions, or formatting
-->

## Before You Submit

Routine plugin/theme update maintenance is handled automatically by our scripts.

**You do not need to open a PR just to update:**
- `latest_release_tag`
- `jar_url`
- generated markdown files
- generated JSON files
- other automation-managed output files

PRs are mainly for:
- adding a new plugin or theme
- correcting metadata the automation cannot determine
- updating descriptions, screenshots, creator info, version support, or structure in `data/plugins-and-themes.yml`

## Checklist

- [ ] I updated **only** `data/plugins-and-themes.yml`
- [ ] All required fields are present and correctly formatted
- [ ] YAML syntax is valid (quotes, spacing, indentation)
- [ ] GitHub repo is public and accessible
- [ ] MC versions and release info are accurate
- [ ] This PR is **not** only for auto-managed release/jar/generated file updates

> **YAML validation and generated output are handled automatically by GitHub Actions and repository automation.**  
> If the PR fails checks, the error message should help show what needs to be fixed.

## Quick Field Reference

- **`name`** → Display name of the plugin/theme  
- **`repo`** → GitHub repo in `owner/repo` format  
- **`description`** → One-line summary  
- **`creator`** → Object with:
  - `name`: Author name  
  - `url`: Author profile URL  
  - `avatar`: Author avatar URL (for example, GitHub `.png?size=20`)  
- **`latest_release_tag`** → Latest GitHub release tag  
- **`screenshots`** → List of screenshots with:
  - `url`: Path to image in `./Assets/...` or valid hosted image
  - `alt`: Short description  
  - `width`: Optional width in pixels  
- **`is_core`** → `true` if it is a core plugin, otherwise `false`  
- **`mc_versions`** → Supported versions (range like `1.20.1-1.21.4` or list)  
- **`jar_url`** → Direct link to the `.jar` release asset  
- **`added_at`** → Date added to the registry  
- **`updated_at`** → Auto-managed update date

## Additional Notes (optional)

<!--
Include any other helpful information, such as:
- missing screenshots for now
- special install notes
- why some metadata may look unusual
- anything the reviewer should know
-->
