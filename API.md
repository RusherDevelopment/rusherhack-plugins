![RusherHack Logo](./Assets/RusherHacks/rh_head.png)
# RusherHack Plugin/Theme API

A free, static JSON API generated from the canonical JSON in this repo:  
**[plugins-and-themes.json](https://github.com/RusherDevelopment/rusherhack-plugins/blob/main/generated/json/plugins-and-themes.json)**  
It is deployed via GitHub Pages at:

```
https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/
```

> [!NOTE]  
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

### Metadata
- **[`stats.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/stats.json)**  
  Aggregate counts by type, Minecraft version, and creator.

- **[`versions.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/versions.json)**  
  List of all supported Minecraft versions (unique + sorted).

- **[`creators.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/creators.json)**  
  List of all creators with plugin/theme counts.

---

> [!TIP]  
> Slugs (`/items/`, `/by-creator/`, `/by-version/`) are **lowercased** and URL-safe.  

### Per-item
- **`/items/{owner}/{repo}.json`**  
  One file per plugin/theme, using the GitHub repo slug.  
  Example:  
  [`items/kybe236/rusher-silent-close.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/items/kybe236/rusher-silent-close.json)

---

### Buckets (Filters)
- **`/by-version/{mc_version}.json`**  
  All plugins/themes supporting that Minecraft version.  
  Example:  
  [`by-version/1.21.4.json`](https://rusherdevelopment.github.io/rusherhack-plugins/api/v1/by-version/1.21.4.json)

- **`/by-creator/{creator}.json`**  
  All plugins/themes by a given creator (lowercased slug).  
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

> [!IMPORTANT]  
> This is an **unstable v1**. Shapes may evolve slightly as we improve consistency.
