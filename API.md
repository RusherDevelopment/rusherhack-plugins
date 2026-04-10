![RusherHack Logo](./Assets/RusherHacks/rh_head.png)

# RusherHack Plugin/Theme API

[![Deploy API (GitHub Pages)](https://github.com/RusherDevelopment/rusherhack-plugins/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/RusherDevelopment/rusherhack-plugins/actions/workflows/deploy-pages.yml)

A free, static JSON API generated from the canonical JSON in this repo:

- **[plugins-and-themes.json](https://github.com/RusherDevelopment/rusherhack-plugins/blob/main/generated/json/plugins-and-themes.json)**
- **[plugin-modules.json](https://github.com/RusherDevelopment/rusherhack-plugins/blob/main/generated/json/plugin-modules.json)**

It is deployed via GitHub Pages at:

```text
https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/
```

> **Note**  
> Endpoints are **static**. They update only when the repo is updated.

---

## Backward Compatibility

The API remains **additive**.

Existing endpoints stay the same, and existing fields are preserved.  
Plugin-related endpoints may now include extra metadata fields such as:

- `features`
- `feature_counts`
- `has_features`

---

## Endpoints

### Core
- **[`index.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/index.json)**  
  Full dataset (plugins + themes).

- **[`plugins.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/plugins.json)**  
  Plugins only.  
  Plugin entries may now include module / HUD metadata.

- **[`themes.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/themes.json)**  
  Themes only.

---

## Plugin Feature Metadata

Plugin objects may now include the following fields:

### `features`
A list of extracted plugin features, such as modules and HUD elements.

Example:
```json
[
  {
    "name": "QueueManager",
    "class_name": "QueueManagerModule",
    "feature_type": "module",
    "description": "2b2t Queue status through discord bot",
    "settings": []
  }
]
```

### `feature_counts`
A compact summary of extracted feature counts.

Example:
```json
{
  "total": 3,
  "modules": 2,
  "hud_elements": 1
}
```

### `has_features`
Boolean indicating whether extracted module or HUD metadata exists.

Example:
```json
true
```

> **Note**  
> These fields apply to **plugins**. Themes do not include module / HUD feature metadata.

---

## Metadata

- **[`stats.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/stats.json)**  
  Aggregate counts by type, Minecraft version, and creator.  
  Also includes feature-related plugin stats.

- **[`versions.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/versions.json)**  
  List of all supported Minecraft versions.

- **[`creators.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/creators.json)**  
  List of all creators with plugin/theme counts.

- **[`meta.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/meta.json)**  
  Metadata about generation time, counts, and source files.

- **[`manifest.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/manifest.json)**  
  SHA256 & size for all API files.

- **[`search-index.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/search-index.json)**  
  Compact search index.  
  Includes feature-related search hints for plugins.

---

## Activity (New & Recently Updated)

These files rely on the YAML fields `added_at` and `updated_at`:

- **[`new.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/new.json)**  
  Recently added items (sorted by newest `added_at`).

- **[`recent.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/recent.json)**  
  Recently updated items (sorted by newest `updated_at` or `added_at`).

---

## Per-Item

- **`/items/{owner}/{repo}.json`**  
  Example:  
  [`items/kybe236/rusher-silent-close.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/items/kybe236/rusher-silent-close.json)

Per-item docs preserve the original item shape and may also include normalized helper fields such as:

- `versions_canonical`
- `owner`
- `repo_name`
- `repo_url`
- `creator_slug`

Plugin item docs may also include:

- `features`
- `feature_counts`
- `has_features`

---

## Buckets (Filtered Views)

- **`/by-version/{mc_version}.json`**  
  Example:  
  [`by-version/1.21.4.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/by-version/1.21.4.json)

- **`/by-creator/{creator}.json`**  
  Example:  
  [`by-creator/tillay.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/by-creator/tillay.json)

These filtered views preserve the same item structure as the main API output.

---

## Usage Examples

### Fetch plugins via curl
```bash
curl -s https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/plugins.json | jq length
```

### Find all Kybe's plugins
```bash
curl -s https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/by-creator/kybe236.json | jq '.[].name'
```

### Get stats
```bash
curl -s https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/stats.json | jq .
```

### Check extracted features for a plugin
```bash
curl -s https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/plugins.json \
  | jq '.[] | select(.repo=="GabiRP/QueueManager") | {name, features, feature_counts, has_features}'
```

### List plugins with HUD elements
```bash
curl -s https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/plugins.json \
  | jq '.[] | select(.feature_counts.hud_elements > 0) | {name, repo, feature_counts}'
```

### Search for a feature name in the compact search index
```bash
curl -s https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/search-index.json \
  | jq '.[] | select((.feature_names // []) | index("Spotify"))'
```

---

## Stats Notes

`stats.json` now includes feature-related aggregate counts for plugins:

- `plugins_with_features`
- `plugins_without_features`
- `total_features`
- `total_modules`
- `total_hud_elements`

This makes it easier for clients to show ecosystem-wide module / HUD totals without scanning every plugin doc.

---

## Search Index Notes

`search-index.json` remains a compact client-friendly file and may now include:

- `has_features`
- `feature_counts`
- `feature_names`

This helps search UIs filter plugins by extracted modules / HUD elements without loading the full plugin dataset.

---

## Showcase
- **[RusherSearch](https://garlicrot.github.io/RusherSearch/)**  
  Instant search UI consuming the API.

---

> **Important:**  
> This is an early **v1**. API shapes may continue to evolve, but changes aim to remain additive and backward-friendly.
