![RusherHack Logo](https://avatars.githubusercontent.com/u/121969799?s=280&v=4)

# Plugin/Theme Registry or Website Update

Thank you for contributing to the RusherHack Plugin Collection!
Please fill out the details below to help keep review quick and clean.

Type of Change

- [ ] Plugin/theme registry update
- [ ] Plugin/theme search website update
- [ ] Both

Summary of Changes

<!--
Briefly describe what this PR does:
- Add a new plugin or theme
- Update an existing YAML entry
- Fix metadata, screenshots, descriptions, creator info, MC versions, or formatting
- Update the plugin/theme search website in public_html/**
-->Before You Submit

Routine plugin/theme update maintenance is handled automatically by repository scripts.

You do not need to open a PR just to update:

- "latest_release_tag"
- "jar_url"
- "updated_at"
- generated markdown files
- generated JSON files
- generated API output files
- other automation-managed output files

PRs are mainly for:

- adding a new plugin or theme
- correcting metadata the automation cannot determine
- updating descriptions, screenshots, creator info, version support, or structure in "data/plugins-and-themes.yml"
- adding or updating screenshot assets in "Assets/**"
- updating the plugin/theme search website in "public_html/**"

Files Changed

Contributor PRs should usually only change:

- "data/plugins-and-themes.yml"
- "Assets/**"
- "public_html/**"

Please do not manually edit generated files such as:

- "README.md"
- "PLUGINS.md"
- "THEMES.md"
- "generated/json/plugins-and-themes.json"
- "api/v1/**"

Generated files are updated automatically after YAML changes are merged into "main".

Checklist

- [ ] I updated only the relevant files for this PR
- [ ] If this is a registry update, I updated "data/plugins-and-themes.yml"
- [ ] If screenshots are needed, I added or updated the related "Assets/**" files
- [ ] If this is a website update, I changed only the relevant "public_html/**" files
- [ ] All required fields are present and correctly formatted
- [ ] YAML syntax is valid, including quotes, spacing, and indentation, if applicable
- [ ] GitHub repo is public and accessible, if applicable
- [ ] MC versions are accurate and use the required comma-separated format, if applicable
- [ ] This PR is not only for auto-managed release, jar, date, markdown, JSON, or API output updates

«When a PR is opened or updated, GitHub Actions automatically validates the PR changes and the YAML file.
After YAML changes are merged into "main", generated markdown, JSON, and API output files are updated automatically.
If the PR fails checks, the error message should help show what needs to be fixed.»

Quick Field Reference

- "name" → Display name of the plugin/theme
- "repo" → GitHub repo in "owner/repo" format
- "description" → One-line summary
- "creator" → Object with:
  - "name": Author name
  - "url": Author profile URL
  - "avatar": Author avatar URL
- "latest_release_tag" → Latest GitHub release tag, if applicable
- "screenshots" → List of screenshots with:
  - "url": Path to image in "./Assets/..." or valid hosted image
  - "alt": Short description
  - "width": Optional width in pixels
- "is_core" → "true" if it is a core plugin, otherwise "false"
- "mc_versions" → Supported Minecraft versions as a comma-separated string, for example:
  - "1.21.4"
  - "1.20.1, 1.20.2, 1.21, 1.21.1, 1.21.4"
  - "N/A" only when version support does not apply
- "jar_url" → Direct link to the ".jar" release asset, if applicable
- "added_at" → Date added to the registry in "YYYY-MM-DD" format
- "updated_at" → Auto-managed update date in "YYYY-MM-DD" format

Additional Notes Optional

<!--
Include any other helpful information, such as:
- missing screenshots for now
- special install notes
- why some metadata may look unusual
- how MC version support was confirmed
- anything the reviewer should know
-->
