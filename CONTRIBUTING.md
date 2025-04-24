# Contributing to the RusherHacks Plugin Collection

Thank you for your interest in contributing to the **RusherHacks Plugin Collection**!  
Your contributions help improve and expand the collection, making it more useful for everyone.  
Whether you're submitting a new plugin, fixing typos, or enhancing existing entries, your support is greatly appreciated.

> [!NOTE]  
> Please follow the style and formatting guidelines described below to ensure consistency across all submissions.

> [!TIP]  
> You can preview your `PLUGINS.md` before submitting by using the GitHub web interface or Markdown preview extensions.

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

4. **Make changes**  
   Make your changes to the codebase. Ensure your code follows the existing style and conventions.

5. **Commit your changes**  
   Commit your changes with a clear and descriptive commit message.

6. **Push to your fork**  
   Push your changes to your forked repository.

7. **Open a pull request**  
   Open a pull request to the main repository. Go to the "Pull Requests" tab on the main repository.  
   <img src="./Assets/Contributing/PullRequestsTab.png" alt="Pull Request Tab" width="150">  
   Click "New Pull Request".  
   <img src="./Assets/Contributing/NewPullRequest.png" alt="New Pull Request" width="150">

8. **Describe your changes**  
   Clearly describe the changes you have made and any relevant context in the pull request description.

> [!WARNING]  
> Make sure not to remove or overwrite existing entries unless it's a verified fix. Always double-check the `badges.json` index value before submitting.

## Example Plugin Entries

<details>
  <summary>Explanation of Placeholders</summary>

- **PLUGIN_NAME**: The name of your plugin  
- **YOUR_USERNAME**: Your GitHub username  
- **YOUR_PLUGIN_REPO**: The name of your plugin's GitHub repository  
- **PLUGIN_INDEX**: Index of your plugin in the `badges.json` file  
- **BADGE_COLOR**: `"green"` if plugin has a release, `"red"` otherwise  
- **LATEST_VERSION**: Latest release version  
- **LATEST_RELEASE_DATE**: Format `YYYY-MM-DD`  
- **SCREENSHOT1.png**: Image file name  
- **CREATOR_URL**: Creator's GitHub URL  
</details>

### **PLUGINS.md Format**

#### **Without Screenshots**
```markdown
- ### [PLUGIN_NAME](https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO) <br>
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[PLUGIN_INDEX].releaseDate&label=Latest%20Release&color=BADGE_COLOR)](https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/YOUR_USERNAME/YOUR_PLUGIN_REPO/total)](https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO/releases/download/LATEST_VERSION/YOUR_PLUGIN_NAME-LATEST_VERSION.jar) <br>
   **Creator**: <img src="https://github.com/YOUR_USERNAME.png?size=20" width="20" height="20"> [YOUR_USERNAME](https://github.com/YOUR_USERNAME)

   YOUR_PLUGIN_DESCRIPTION
```

---

### PLUGINS.md with Screenshots
```markdown
- ### [PLUGIN_NAME](https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO) <br>
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[PLUGIN_INDEX].releaseDate&label=Latest%20Release&color=BADGE_COLOR)](https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/YOUR_USERNAME/YOUR_PLUGIN_REPO/total)](https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO/releases/download/LATEST_VERSION/YOUR_PLUGIN_NAME-LATEST_VERSION.jar) <br>
   **Creator**: <img src="https://github.com/YOUR_USERNAME.png?size=20" width="20" height="20"> [YOUR_USERNAME](https://github.com/YOUR_USERNAME)

   YOUR_PLUGIN_DESCRIPTION

   <details>
   <summary>Show Screenshots</summary>
   <p align="center">
     <img src="./Assets/YOUR_PLUGIN_NAME/SCREENSHOT1.png" alt="Screenshot 1" width="250">
     <img src="./Assets/YOUR_PLUGIN_NAME/SCREENSHOT2.png" alt="Screenshot 2" width="550">
   </p>
   </details>
```

---

### Core Plugin Badge

If your plugin is a **Core Plugin**, add this badge manually:

```md
![Core Plugin](https://img.shields.io/badge/Core%20Plugin-blue)
```

#### Example Core Plugin Entry
```markdown
- ### [PLUGIN_NAME](https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO)

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[PLUGIN_INDEX].releaseDate&label=Latest%20Release&color=BADGE_COLOR)](https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO/releases) ![Core Plugin](https://img.shields.io/badge/Core%20Plugin-blue) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/YOUR_USERNAME/YOUR_PLUGIN_REPO/total)](https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO/releases/download/LATEST_VERSION/YOUR_PLUGIN_NAME-LATEST_VERSION.jar)

   **Creator**: <img src="https://github.com/YOUR_USERNAME.png?size=20" width="20" height="20"> [YOUR_USERNAME](https://github.com/YOUR_USERNAME)

   YOUR_PLUGIN_DESCRIPTION
```

> [!IMPORTANT]  
> You do **not** need to modify the `badges.json` for core plugins. This badge is for visual display in the `PLUGINS.md` only.

---

### badges.json Plugin Example
```json
{
  "name": "PLUGIN_NAME",
  "url": "https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO",
  "releaseUrl": "https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO/releases",
  "latestReleaseUrl": "https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO/releases/download/LATEST_VERSION/YOUR_PLUGIN_NAME-LATEST_VERSION.jar",
  "releaseDate": "LATEST_RELEASE_DATE",
  "color": "BADGE_COLOR",
  "description": "YOUR_PLUGIN_DESCRIPTION",
  "creator": {
    "name": "YOUR_USERNAME",
    "url": "https://github.com/YOUR_USERNAME",
    "avatarUrl": "https://github.com/YOUR_USERNAME.png?size=20"
  },
  "screenshots": [
    {
      "type": "image",
      "url": "./Assets/YOUR_PLUGIN_NAME/SCREENSHOT1.png",
      "alt": "Screenshot 1",
      "width": 250
    },
    {
      "type": "image",
      "url": "./Assets/YOUR_PLUGIN_NAME/SCREENSHOT2.png",
      "alt": "Screenshot 2",
      "width": 550
    }
  ]
}
```

## Reporting Issues

If you find any typos, incorrect information, or have suggestions for improvements, submit an issue using the [Plugin Information Issue](https://github.com/RusherDevelopment/rusherhack-plugins/issues/new?template=plugin-information-issue.md).


> [!INFO]  
> Providing detailed info will help us fix issues faster and keep the plugin list accurate.

