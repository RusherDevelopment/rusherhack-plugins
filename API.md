![RusherHack Logo](./Assets/RusherHacks/rh_head.png)
# RusherHack Plugin/Theme API

[![Deploy API (GitHub Pages)](https://github.com/RusherDevelopment/rusherhack-plugins/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/RusherDevelopment/rusherhack-plugins/actions/workflows/deploy-pages.yml)

A free, static JSON API generated from the canonical JSON in this repo:  
**[plugins-and-themes.json](https://github.com/RusherDevelopment/rusherhack-plugins/blob/main/generated/json/plugins-and-themes.json)**  
It is deployed via GitHub Pages at:

```
https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/
```

> **Note**  
> Endpoints are **static**. They update only when the repo is updated.  

---

## Endpoints

### Core
- **[`index.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/index.json)**  
  Full dataset (plugins + themes).

- **[`plugins.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/plugins.json)**  
  Plugins only.

- **[`themes.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/themes.json)**  
  Themes only.

---

## Metadata
- **[`stats.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/stats.json)**  
  Aggregate counts by type, Minecraft version, and creator.

- **[`versions.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/versions.json)**  
  List of all supported Minecraft versions.

- **[`creators.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/creators.json)**  
  List of all creators with plugin/theme counts.

- **[`meta.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/meta.json)**  
  Metadata about generation time + counts.

- **[`manifest.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/manifest.json)**  
  SHA256 & size for all API files.

- **[`search-index.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/search-index.json)**  
  Compact search index.

---

## Activity (New & Recently Updated)

These files rely on the YAML fields `added_at` and `updated_at`:

- **[`new.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/new.json)**  
  Recently added items (sorted by newest `added_at`).

- **[`recent.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/recent.json)**  
  Recently updated items (sorted by newest `updated_at` or `added_at`).

---

## Per‑Item
- **`/items/{owner}/{repo}.json`**  
  Example:  
  [`items/kybe236/rusher-silent-close.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/items/kybe236/rusher-silent-close.json)

---

## Buckets (Filtered Views)

- **`/by-version/{mc_version}.json`**  
  Example:  
  [`by-version/1.21.4.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/by-version/1.21.4.json)

- **`/by-creator/{creator}.json`**  
  Example:  
  [`by-creator/tillay.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/by-creator/tillay.json)

---

## Usage Examples

### Fetch plugins via curl
```bash
curl -s https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/plugins.json | jq length
```

### Find all kybe’s plugins
```bash
curl -s https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/by-creator/kybe236.json | jq '.[].name'
```

### Get stats
```bash
curl -s https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/stats.json | jq .
```

---

## Showcase
- **[RusherSearch](https://garlicrot.github.io/RusherSearch/)**  
  Instant search UI consuming the API.

---

> **Important:**  
> This is an early **v1**. API shapes may slightly evolve.
