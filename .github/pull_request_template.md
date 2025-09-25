![RusherHack Logo](https://avatars.githubusercontent.com/u/121969799?s=280&v=4)

# Plugin/Theme Submission or Update

Thank you for contributing to the RusherHacks Plugin Collection!  
Please fill out the details below to ensure a smooth and quick review.

---

## Summary of Changes

<!--
Briefly describe what this PR does:
- Add a new plugin or theme?
- Update an existing entry?
- Fix metadata or formatting?
-->

---

## Checklist

- [ ] I updated **only** `data/plugins-and-themes.yml`
- [ ] All required fields are present and correctly formatted
- [ ] YAML syntax is valid (quotes, spacing, indentation)
- [ ] GitHub repo is public and accessible
- [ ] MC versions and release info are accurate

> **YAML validation is handled automatically by GitHub Actions.**  
> If your PR fails, the error message will tell you what to fix.

---

## 🔎 Quick Field Reference

- **`name`** → Display name of the plugin/theme  
- **`repo`** → GitHub repo in `owner/repo` format  
- **`description`** → One-line summary  
- **`creator`** → Object with:
  - `name`: Author name  
  - `url`: Author profile URL  
  - `avatar`: Author avatar URL (e.g., GitHub `.png?size=20`)  
- **`latest_release_tag`** → Latest GitHub release tag (string)  
- **`screenshots`** → List of screenshots with:
  - `url`: Path to image in `./Assets/...`  
  - `alt`: Short description  
  - `width`: Optional width in pixels  
- **`is_core`** → `true` if it’s a core plugin, else `false`  
- **`mc_versions`** → Supported versions (range like `1.20.1-1.21.4` or list)  
- **`jar_url`** → Direct link to the `.jar` release asset  

---

## Additional Notes (optional)

<!--
Include any other helpful information (e.g., why a jar link is missing,
screenshots not yet uploaded, etc.)
-->
