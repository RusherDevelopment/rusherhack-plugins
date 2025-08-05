# Contributing to the RusherHacks Plugin Collection

Thank you for your interest in contributing to the **RusherHacks Plugin Collection**!  
Your contributions help improve and expand the collection, making it more useful for everyone.  
Whether you're submitting a new plugin, fixing typos, or enhancing existing entries, your support is greatly appreciated.

> [!NOTE]  
> Please follow the style and formatting guidelines described below to ensure consistency across all submissions.

## How to Contribute

1. **Fork the repository**  
   Click the **Fork** button at the top right of this page to create a copy of this repository on your own GitHub account.  
   ![Fork Button](./Assets/Contributing/Fork.png)

2. **Clone the repository**  
   Clone your forked repository to your local development machine using Git.  
   ![Clone Button](./Assets/Contributing/Clone.jpg)

3. **Create a new branch**  
   Always create a new branch for your changes before committing.  
   ![Create Branch](./Assets/Contributing/NewBranch.png)

4. **Add your plugin or theme**  
   Open the `data/plugins-and-themes.yml` file and add your plugin or theme in the appropriate section:
   - Add plugin entries under the `plugins:` section.
   - Add theme entries under the `themes:` section.

   Follow the format used in existing entries. Each entry must include:
   - `name`
   - `repo`
   - `description`
   - `creator`:
     - `name`
     - `url`
     - `avatar`
   - `latest_release_tag`
   - `screenshots` (can be an empty list)
   - For plugins:
     - `mc_versions`
     - `is_core` (true or false)

5. **Push and create a pull request**  
   Push your branch and open a pull request targeting the `main` branch.

6. **Check GitHub Actions**  
   Your pull request will automatically run a validation check.  
   If it fails, visit the **Actions** tab to view the error details and fix any issues.

> [!TIP]  
> If everything is correct, the markdown files (`PLUGINS.md`, `THEMES.md`, and `README.md`) will be automatically updated on merge.

> [!NOTE]  
> You no longer need to manually validate YAML — it's automatically handled by `validate-yml.py` and checked via GitHub Actions.
   
### Example Plugin Format (with screenshots):
```yaml
- name: RusherHack-HudElement
  repo: Aspect-404/RusherHack-HudElement
  description: Create a customizable HUD element for Minecraft utility mod RusherHack.
  creator:
    name: Aspect-404
    url: https://github.com/Aspect-404
    avatar: https://github.com/Aspect-404.png?size=20
  latest_release_tag: Release
  screenshots:
  - url: ./Assets/RusherHack-HudElement/HudSettings.png
    alt: Hud Setting
    width: 250
  - url: ./Assets/RusherHack-HudElement/HudElement.png
    alt: Hud Element
    width: 550
  is_core: false
  mc_versions: 1.20.4-1.21
```

### Example Plugin Format (without screenshots):
```yaml
- name: Example Plugin
  repo: RusherDevelopment/example-plugin
  description: A basic example plugin demonstrating the structure and capabilities of RusherHacks plugins.
  creator:
    name: RusherDevelopment
    url: https://github.com/RusherDevelopment
    avatar: https://github.com/RusherDevelopment.png?size=20
  latest_release_tag: ''
  screenshots: []
  is_core: false
  mc_versions: N/A
```

### Example Theme Format (with screenshots):
```yaml
- name: rusherNodusTheme
  repo: bakjedev/rusherNodusTheme
  description: Nodus - Best theme evaAAAA. Code is terrible. Blame xyzbtw!
  creator:
    name: bakjedev
    url: https://github.com/bakjedev
    avatar: https://github.com/bakjedev.png?size=20
  latest_release_tag: ''
  screenshots:
  - url: ./Assets/rusherNodusTheme/NodusGUI.png
    alt: Module
    width: 750
```

### Example Theme Format (without screenshots):
```yaml
- name: Nhack Theme
  repo: h1tm4nqq/Nhack-theme
  description: A theme like Nhack 2015 for RH.
  creator:
    name: h1tm4nqq
    url: https://github.com/h1tm4nqq
    avatar: https://github.com/h1tm4nqq.png?size=20
  latest_release_tag: 1.0.1
  screenshots: []
```
