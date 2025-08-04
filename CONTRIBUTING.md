# Contributing to the RusherHacks Plugin Collection

Thank you for your interest in contributing to the **RusherHacks Plugin Collection**!  
Your contributions help improve and expand the collection, making it more useful for everyone.  
Whether you're submitting a new plugin, fixing typos, or enhancing existing entries, your support is greatly appreciated.

> [!NOTE]  
> Please follow the style and formatting guidelines described below to ensure consistency across all submissions.

## How to Contribute

1. **Fork the repository**  
   Click the "Fork" button on the top right of the repository page to create a copy of this repository on your GitHub account.  
   <img src="./Assets/Contributing/Fork.png" alt="Fork Button" width="125">

2. **Clone the repository**  
   Clone the forked repository to your local machine.  
   <img src="./Assets/Contributing/Clone.jpg" alt="Clone Button" width="250">

3. **Create a new branch**  
   Create a new branch for your contribution.  
   <img src="./Assets/Contributing/NewBranch.png" alt="Create Branch" width="100">

4. **Add your plugin or theme**  
   Open the `data/plugins-and-themes.yml` file and add your plugin or theme entry in the appropriate section.

5. **Validate your changes**
   Make sure your `plugins-and-themes.yml` file is valid YAML. You can use tools like [YAML Lint](https://www.yamllint.com/) to verify formatting.
   
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
