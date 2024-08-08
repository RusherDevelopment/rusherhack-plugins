# Contributing to RusherHacks Plugin Collection

Thank you for considering contributing to the RusherHacks Plugin Collection! <br>
Your contributions are what make this project great.

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

## Example Plugin Layout

Replace 'Plugin Name', 'username', 'plugin-repo', and 'INDEX' with the appropriate values for each plugin. This template includes the badge that links to the latest release of the plugin.

```
### [Plugin Name](https://github.com/username/plugin-repo) <br>
[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[INDEX].releaseDate&label=Latest%20Release&color=green)](https://github.com/username/plugin-repo/releases) <br>

**Creator**: <img src="https://github.com/username.png?size=20" width="20" height="20"> [username](https://github.com/username)

A brief description of the plugin and its functionality.
```

<details>
  <summary>Explanation of INDEX</summary>
  The `INDEX` in the URL for the badge is the position of the plugin in the `badges.json` file. This index is used to retrieve the latest release date for the specific plugin from the JSON data. Make sure to replace `INDEX` with the appropriate number that corresponds to the plugin's position in the `badges.json` file. The first plugin in the list would have an `INDEX` of 0, the second would have an `INDEX` of 1, and so on.

For example, if your plugin is the third plugin in the `badges.json` file, you would replace `INDEX` with `2`.

</details>

---

## Reporting Issues

If you encounter any typos, errors, or have suggestions for improvements, please open an issue on the GitHub repository with as much detail as possible.
