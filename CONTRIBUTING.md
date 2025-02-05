# Contributing to the RusherHacks Plugin Collection  

Thank you for your interest in contributing to the **RusherHacks Plugin Collection**!  
Your contributions help improve and expand the collection, making it more useful for everyone.  
Whether you're submitting a new plugin, fixing typos, or enhancing existing entries, your support is greatly appreciated.

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
   Open a pull request to the main repository. Go to the "Pull Requests" tab on the main repository. <br>
   <img src="./Assets/Contributing/PullRequestsTab.png" alt="Pull Request Tab" width="150"> <br>
   Click "New Pull Request". <br>
   <img src="./Assets/Contributing/NewPullRequest.png" alt="New Pull Request" width="150">
8. **Describe your changes**  
   Clearly describe the changes you have made and any relevant context in the pull request description.

## Example Plugin Entries

<details>
  <summary>Explanation of Placeholders</summary>
  
- **PLUGIN_NAME**: The name of your plugin  
- **YOUR_USERNAME**: Your GitHub username  
- **YOUR_PLUGIN_REPO**: The name of your plugin's GitHub repository  
- **PLUGIN_INDEX**: The index of your plugin in the `badges.json` file (0 for the first plugin, 1 for the second, etc.)  
- **BADGE_COLOR**:  
  - `"green"` if the plugin has a release  
  - `"red"` if the plugin has no release  
- **YOUR_PLUGIN_DESCRIPTION**: A brief description of your plugin  
- **LATEST_VERSION**: The version number of your latest release  
- **LATEST_RELEASE_DATE**: The date of your latest release in the format `YYYY-MM-DD`  
- **LATEST_RELEASE_URL**: The direct URL to the latest release `.jar` file  
- **SCREENSHOT1.png, SCREENSHOT2.png**: The filenames of your screenshot images  
- **SCREENSHOT1_DESCRIPTION, SCREENSHOT2_DESCRIPTION**: Brief descriptions of your screenshots  
- **CREATOR_NAME**: The display name of the plugin creator  
- **CREATOR_URL**: The GitHub profile URL of the creator  
- **CREATOR_AVATAR_URL**: The GitHub avatar URL of the creator (`https://github.com/YOUR_USERNAME.png?size=20`)
</details>


### **README.md Format**

#### **Without Screenshots**
```markdown
- ### [PLUGIN_NAME](https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO) <br>
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[PLUGIN_INDEX].releaseDate&label=Latest%20Release&color=BADGE_COLOR)](https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/YOUR_USERNAME/YOUR_PLUGIN_REPO/total)](https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO/releases/download/LATEST_VERSION/YOUR_PLUGIN_NAME-LATEST_VERSION.jar) <br>
   **Creator**: <img src="https://github.com/YOUR_USERNAME.png?size=20" width="20" height="20"> [YOUR_USERNAME](https://github.com/YOUR_USERNAME)

   YOUR_PLUGIN_DESCRIPTION
```

### README.md with Screenshots
```markdown
- ### [PLUGIN_NAME](https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO) <br>
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[PLUGIN_INDEX].releaseDate&label=Latest%20Release&color=BADGE_COLOR)](https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/YOUR_USERNAME/YOUR_PLUGIN_REPO/total)](https://github.com/YOUR_USERNAME/YOUR_PLUGIN_REPO/releases/download/LATEST_VERSION/YOUR_PLUGIN_NAME-LATEST_VERSION.jar) <br>
   **Creator**: <img src="https://github.com/YOUR_USERNAME.png?size=20" width="20" height="20"> [YOUR_USERNAME](https://github.com/YOUR_USERNAME)

   YOUR_PLUGIN_DESCRIPTION

   <details>
   <summary>Show Screenshots</summary>
   <p align="center">
      <img src="./Assets/YOUR_PLUGIN_NAME/SCREENSHOT1.png" alt="SCREENSHOT1_DESCRIPTION" border="0" width="250">
      <img src="./Assets/YOUR_PLUGIN_NAME/SCREENSHOT2.png" alt="SCREENSHOT2_DESCRIPTION" border="0" width="550">
   </p>
   </details>
```

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
            "alt": "SCREENSHOT1_DESCRIPTION",
            "width": 250
        },
        {
            "type": "image",
            "url": "./Assets/YOUR_PLUGIN_NAME/SCREENSHOT2.png",
            "alt": "SCREENSHOT2_DESCRIPTION",
            "width": 550
        }
    ]
}
```

## Reporting Issues

If you find any typos, incorrect information, or have suggestions for improvements, please submit a report using the [Plugin Information Issue](https://github.com/RusherDevelopment/rusherhack-plugins/issues/new?assignees=&labels=&template=plugin-information-issue.md&title=%5BISSUE%5D) template.  

### When reporting an issue, please include:
- A clear description of the problem
- The affected plugin name and version (if applicable)
- The incorrect information and the correct information (if known)
- Screenshots or links for reference (if applicable)  

Providing detailed information will help us resolve issues faster and keep the plugin list accurate.
