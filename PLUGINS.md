![RusherHack Logo](./Assets/RusherHacks/rh_head.png)

# Plugins List

[![Plugins](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=$.totalPlugins.message&label=Plugins&color=green)](#plugins-list)
[![RusherHack v2.0.6](https://img.shields.io/badge/RusherHack-v2.0.6-purple?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOsAAADqCAYAAABDVrJwAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAnnSURBVHhe7d0xjx1XGcbxnRUkQUE4Ekj+AqvUqaCMBClooKKAzhJtOiLRuIGIloiI0kTuEBIVoqDhK7ijc0NppUIoQWEt38yxZq3rdx5rX58z98w8c/+/6E1GzsyZOTPz+Pgc390d3n/v6nDR2Te+OUxbfT297t7Vi48+/mTa2r9Hjx5NW/v39798Nm31czn9F8DGEVbABGEFTOTDehjne7GwP+WxxnLTow9l2aW2KjGyAiYIK2CCsAImCCtgIh/WYZwZx6rVYwFAKZccCy/bwz3q0Qf1DmerEiMrYIKwAiYIK2CCsAIm1glrjwUARU32l7yWJdvqQd2PrVvyemNbre1lVb4njKyACcIKmCCsgAnCCphYPqyVk+fVLLnIoNpS1aKlvXhcj2cVz1mqxZLXG9tqbS9L3ZPEdTCyAiYIK2CCsAImCCtgYvGwDuNkOdZM+bVYexUXDl6xeJDW0l7tcS3iOXud100iD4ysgAnCCpggrICJ4YPvv7vnGePqfvWbP0xbR9Qd38Fc7unTp9NWP7/99YfT1kLUcxDP6ztvvzFt9cPICpggrIAJwgqYIKyACcK6pOO/+L8pJbtf1s1fpB/XVmz52pQNXy9hBUwQVsAEYQVMEFbABGFd0lqLE7ULVi3Xq45VVXttmCGsgAnCCpggrIAJwgqYIKxZe1wkiX16nX6pY1WdE7XAtiDCCpggrIAJwgqYIKyACcKadcKFg9XEPu2lX2s58QIbYQVMEFbABGEFTBBWwARhPWcnXhDZFNVXVT1ULuwRVsAEYQVMEFbABGEFTAzfe+ed2fT2cJjPeOXce8jNyA/hx58Ph9PP5GUfLsV5n4nZveiXai/K3qNMW8+J30rVvZN9TZxX7ZMl+7Dw9SrpexeoZ39Qz14YRL8Oz6aNhWR6z8gKmCCsgAnCCpggrIAJucDUIrN4kF6cUJP45IJNZoHldWT6oBYJ6s+Y70P1fup+iLZkx5ILc2lhEbJQizipPijZaxPtqTOo1uR+LfckYGQFTBBWwARhBUwQVsBE0wJT7YJNy+S8ZYFFLmJVfpoqex1qwUIudrTspyTuibxedUqxmJRdOMm+I7XPOvscstehtPRVHqnai8eKfRhZAROEFTBBWAEThBUwkV5gapmgx98S0os66pzJxYPaBYsi01fZg4ZzSgv3f9Ze9joU8Ymjiw5f+piReX5F+jlsBCMrYIKwAiYIK2Bi+O6dO7M/4Ms/yS/45/umeVyD6rldEfZrmRfJY9Vvm+qrTqb/viR5jngtS96P5xr2E0fqawla+pA9Z/ZZK6oHmfOqczKyAiYIK2CCsAImCCtgQn8oQs3Ps195oSbjcT812Re/bbR8f+HsooA8Q6Zf2b4Laq/swoa855WWXjhR9yTbhzX6mm5fHCvvnBr6Kr+/sLo2RlbABGEFTBBWwARhBUws/m1d5KQ97pec2LcsgCjqBwxlv1Kk9lp+/+mn09YtVPPJ9Q/ls08+nrb6+de/P5+2jogFFtlV8U7I92v67wuZ963I7qck39e07PUFjKyACcIKmCCsgAnCCphYPKxlUSBWlNmnKFPuWFnq2PKDjmaVvZZhuLWaxIttbE46cfvy/pZfD9Vy72btDeMziyX2m/V9LL3f+D9iCfK9EaX2G//P/LwJjKyACcIKmCCsgAnCCphoCqtaKFB1cflylSl7rHHmPasy8Y6lyHOqEsqvxlLXEkstHHRRTpMpJe4jO19v4eZke7Pn/Gz8xVBxn1LlSzxjqf2U7LOOt7eUOoeqWUcFRlbABGEFTBBWwARhBUzosMbJbqkyqY4lqMn4bHJf9gs1zrLnJajJuTpnVryO50eObcYq3yPquNR1dFFOk6kM2fl6qjl5n8rziSWUX53VuO9tzznuU0peh5A9NluqPVkhI+MvzkqHFcDmEFbABGEFTBBWwMSlmuzKmf04WY6ljlWT7Exl21LUftn2VKljZ5+UwYy6l0p8tUop5ehZiXPEUuQzFbLtqYtT51DtZWr816wYWQEThBUwQVgBE4QVMFG+aG02V1YT5fFfs1ITY3lsgmprdmFjZdtX7aljValjYynZ/c7d0eN8UVK5f7Gi8XnFUs9BlXr2ityv7BoqfQ5Rs30ERlbABGEFTBBWwARhBUwMH/zgXT2bPaH//PeraauvO99+c9rq5/pafNyp+x3v44uv/j9t9fP2m29MW319eX09bR058XNlZAVMEFbABGEFTBBWwARhLR+KibWksugQa8uy9yO7316t8FwJK2CCsAImCCtgYh9hbZk/rTD32LTs/VD7ZWsrWt6bFTCyAiYIK2CCsAImCCtgYh9h3fIixpYtvcCi2lO1FWbvDSMrYIKwAiYIK2CCsAIm1gnrlhcdOkh3P71jJbMFFkeD+KcWIytggrACJggrYIKwAibWCata2IgLKfXz8NNY8NpU96X0jtiE+I6MdRD/1GJkBUwQVsAEYQVMEFbAxPD+e1fdly3W+KE+xZ//9s9p6wyUBY4tOPFz/flPfjht9ZX+gVjqOVTeE0ZWwARhBUwQVsAEYQVM6LAefQLjRS2pTLBjtTj19QK1FnzXGVkBE4QVMEFYAROEFTChw7rgpLgLt+vdqz08hw33gZEVMEFYAROEFTBBWAEThHUNfOLqtFoWiTb8bAgrYIKwAiYIK2CCsAIm9hvWDS8UNC2AZNWeo/a4Lck++7X6mr2+gJEVMEFYAROEFTBBWAETfmHNTs7XWjzYiux9itRxqtay5HXEtlrby6p8NxlZAROEFTBBWAETq/xgqj/99R/TVl9XV1fTVj/37t2btjYgzskWfvIPHz6ctvp5/PjxtNXXL376o2nrFmoeXHnfGVkBE4QVMEFYAROEFTBBWM/JzV/A39SZOxwOs1pcvOcNpyCsgAnCCpggrIAJwgqY2E5Yj7/y4abg71uiTi35Lg3DMKsu4rUlT8vICpggrIAJwgqYIKyAie2EdcFPemBD/ifq1JZ+lyoXhF6p8voYWQEThBUwQVgBE4QVMEFYgdtULgi9lsQCFmEFTBBWwARhBUwQVsDEZZzXvmJui7dCrWWNB7bGOc9NYgGLkRUwQVgBE4QVMEFYARNtP0VOLTQkWvvdH3M/bUx90+WW75Pz4MGDaaufJ0+eTFv7d/fu3Wmrn/v3709bff3yZz+etvphZAVMEFbABGEFTBBWwERbWG8+bXFcC4rfgLllcanZzSd3bgrIiO9Nw7vDyAqYIKyACcIKmCCsgAnCmnXChbSz07LoUnvcWuJ70/DuEFbABGEFTBBWwARhBUwQVvTXsuhSe9wOEFbABGEFTBBWwARhBUz0Cavbp06ADWJkBUwQVsAEYQVM9AnrGf9FNlYQ10h2sk7CyAqYIKyACcIKmCCsgIWLi68BQPqYEKtSNCEAAAAASUVORK5CYII=)](https://rusherhack.org/changelog.html)

> [!WARNING]
> None of the plugins listed here have been verified or confirmed to be safe. Use at your own risk!

> [!IMPORTANT]
> These plugins are not affiliated with or endorsed by Rusher Development LLC.

Community-created plugins to extend RusherHack’s functionality.

## Plugins

Regular plugins extend RusherHack’s functionality without modifying Minecraft's internal behavior. Key features:

- Can be reloaded in-game using `*reload` in chat or `reload` in the RusherHack console (`~` key).
- Can be added or removed from the `.minecraft/rusherhack/plugins/` folder while the game is running.

## Core Plugins

Core plugins provide deeper integration with RusherHack by modifying Minecraft’s internals using mixins. Key differences:

- **Cannot be reloaded** using `*reload`.
- Must be placed in the `.minecraft/rusherhack/plugins/` folder before launching the game.

## Badge Info

> [!TIP]
> Badges provide quick access to plugin resources:
>
> - **Latest Release** – links to the plugin’s GitHub releases page.
> - **Downloads** – directly downloads the latest plugin `.jar` file.
> - **MC Version** – displays the supported Minecraft version range.

## Top 5 Downloaded Plugins

<details>
<summary>View Top 5 Plugins</summary>

| Name | Creator | Description | Downloads |
|------|---------|-------------|-----------|
| [RusherHack Spotify Integration](https://github.com/John200410/rusherhack-spotify) | <img src="https://github.com/John200410.png" width="20" style="vertical-align: middle;"> John200410 | Integrates Spotify music playback controls and status into the RusherHacks client. | ![GitHub Downloads](https://img.shields.io/github/downloads/John200410/rusherhack-spotify/total) |
| [Container Tweaks](https://github.com/rfresh2/ContainerTweaks-rusherhack) | <img src="https://github.com/rfresh2.png" width="20" style="vertical-align: middle;"> rfresh2 | Simple tweaks for quickly moving items in containers. | ![GitHub Downloads](https://img.shields.io/github/downloads/rfresh2/ContainerTweaks-rusherhack/total) |
| [Shay's RusherTweaks](https://github.com/ShayBox/ShaysRusherTweaks) | <img src="https://github.com/ShayBox.png" width="20" style="vertical-align: middle;"> ShayBox | A collection of small tweaks and improvements for the RusherHacks client. | ![GitHub Downloads](https://img.shields.io/github/downloads/ShayBox/ShaysRusherTweaks/total) |
| [Nuker](https://github.com/beanbag44/Nuker) | <img src="https://github.com/beanbag44.png" width="20" style="vertical-align: middle;"> beanbag44 | Epic nuker for nuking terrain. | ![GitHub Downloads](https://img.shields.io/github/downloads/beanbag44/Nuker/total) |
| [RusherHack Instance Info](https://github.com/John200410/rusherhack-instance-info) | <img src="https://github.com/John200410.png" width="20" style="vertical-align: middle;"> John200410 | Provides detailed information about the current instance. | ![GitHub Downloads](https://img.shields.io/github/downloads/John200410/rusherhack-instance-info/total) |
</details>

## Plugin List

> [!NOTE]
> The following plugins are community contributions. Always verify the source code and test plugins in a safe environment before using them in your main game.

> [!TIP]
> Use the **Outline** on the right side of this page to quickly navigate to a specific plugin. Alternatively, press **Ctrl + F** to search for a plugin name directly.

---

- ### [Example Plugin](https://github.com/RusherDevelopment/example-plugin) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[0].releaseDate&label=Latest%20Release&color=orange)](https://github.com/RusherDevelopment/example-plugin/releases) ![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/RusherDevelopment/example-plugin/total)<br>

   **Creator**: <img src="https://github.com/RusherDevelopment.png?size=20" width="20" height="20"> [RusherDevelopment](https://github.com/RusherDevelopment)

   A basic example plugin demonstrating the structure and capabilities of RusherHacks plugins.

---

- ### [2b2t.vc Rusherhack](https://github.com/rfresh2/2b2t.vc-rusherhack) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[1].releaseDate&label=Latest%20Release&color=green)](https://github.com/rfresh2/2b2t.vc-rusherhack/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/rfresh2/2b2t.vc-rusherhack/total)](https://github.com/rfresh2/2b2t.vc-rusherhack/releases/download/1.12/2b2t.vc-rusherhack-1.12.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[1].badge_version&label=MC%20Version&color=blueviolet)<br>

   **Creator**: <img src="https://github.com/rfresh2.png?size=20" width="20" height="20"> [rfresh2](https://github.com/rfresh2)

   A RusherHacks plugin designed for 2b2t.vc server use.

   <details>
     <summary>Show Screenshots</summary>
     <p align="center">
       <img src="./Assets/2b2t.vc Rusherhack/HudSettings.png" alt="Hud Setting" border="0" width="250">
       <img src="./Assets/2b2t.vc Rusherhack/HudDisplay.png" alt="Hud Display w/2b2t Queue" border="0" width="550">
     </p>
   </details>

---

- ### [RusherHack-HudElement](https://github.com/Aspect-404/RusherHack-HudElement) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[2].releaseDate&label=Latest%20Release&color=green)](https://github.com/Aspect-404/RusherHack-HudElement/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Aspect-404/RusherHack-HudElement/total)](https://github.com/Aspect-404/RusherHack-HudElement/releases/download/Release/HudElement.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[2].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/Aspect-404.png?size=20" width="20" height="20"> [Aspect-404](https://github.com/Aspect-404)

   Create a customizable HUD element for Minecraft utility mod RusherHack.

   <details>
     <summary>Show Screenshots</summary>
     <p align="center">
       <img src="./Assets/RusherHack-HudElement/HudSettings.png" alt="Hud Setting" border="0" width="250">
       <img src="./Assets/RusherHack-HudElement/HudElement.png" alt="Hud Element" border="0" width="550">
     </p>
   </details>

---

- ### [Auto Anvil Rename](https://github.com/IceTank/AutoAnvilRename) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[3].releaseDate&label=Latest%20Release&color=green)](https://github.com/IceTank/AutoAnvilRename/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/IceTank/AutoAnvilRename/total)](https://github.com/IceTank/AutoAnvilRename/releases/download/v0.1/AutoAnvilRename-v0.1.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[3].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/IceTank.png?size=20" width="20" height="20"> [IceTank](https://github.com/IceTank)

   Automates the renaming process in anvils.

   <details>
     <summary>Show Screenshots</summary>
     <p align="center">
       <img src="./Assets/AutoAnvilRename/Module.png" alt="Module" border="0" width="250">
       <img src="./Assets/AutoAnvilRename/ModuleInfo.png" alt="Module Info" border="0" width="450">
     </p>
   </details>

---

- ### [Queue Manager](https://github.com/GabiRP/QueueManager) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[4].releaseDate&label=Latest%20Release&color=green)](https://github.com/GabiRP/QueueManager/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/GabiRP/QueueManager/total)](https://github.com/GabiRP/QueueManager/releases/latest/download/QueueManager.Rusher-1.0-SNAPSHOT.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[4].badge_version&label=MC%20Version&color=blueviolet)<br>

   **Creator**: <img src="https://github.com/GabiRP.png?size=20" width="20" height="20"> [GabiRP](https://github.com/GabiRP)

   Manages queue positions and notifies users of their status.

---

- ### [RusherHack Instance Info](https://github.com/John200410/rusherhack-instance-info) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[5].releaseDate&label=Latest%20Release&color=green)](https://github.com/John200410/rusherhack-instance-info/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/John200410/rusherhack-instance-info/total)](https://github.com/John200410/rusherhack-instance-info/releases/download/v1.2.1/instance-info-1.2.1.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[5].badge_version&label=MC%20Version&color=blueviolet)<br>

   **Creator**: <img src="https://github.com/John200410.png?size=20" width="20" height="20"> [John200410](https://github.com/John200410)

   Provides detailed information about the current instance.

   <details>
     <summary>Show Screenshots</summary>
     <p align="center">
       <img src="./Assets/rusherhack-instance-info/Module.png" alt="Module" border="0" width="350">
       <img src="./Assets/rusherhack-instance-info/PlayerHead.png" alt="Player Head Info" border="0" width="250">
       <img src="./Assets/rusherhack-instance-info/WindowInfo.png" alt="Player Head Info" border="0" width="550">
     </p>
   </details>

---

- ### [Stash Mover Plugin](https://github.com/xyzbtw/StashMoverPlugin) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[6].releaseDate&label=Latest%20Release&color=green)](https://github.com/xyzbtw/StashMoverPlugin/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/xyzbtw/StashMoverPlugin/total)](https://github.com/xyzbtw/StashMoverPlugin/releases/download/FINAL/stashmover-release-1.20.4.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[6].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/xyzbtw.png?size=20" width="20" height="20"> [xyzbtw](https://github.com/xyzbtw)

   A plugin to move stashes using pearls.

   <details>
     <summary>Show Screenshots/Videos</summary>
     <p align="center">
       <a href="https://www.youtube.com/watch?v=gfnNFyRQavA">
         <img src="https://img.youtube.com/vi/gfnNFyRQavA/0.jpg" alt="Stash Mover Demo">
       </a>
     </p>
   </details>

---

- ### [Unified Module List](https://github.com/czho/unified-modulelist) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[7].releaseDate&label=Latest%20Release&color=orange)](https://github.com/czho/unified-modulelist/releases) ![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/czho/unified-modulelist/total)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[7].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/czho.png?size=20" width="20" height="20"> [czho](https://github.com/czho)

   Rusherhack HUD element that shows active modules from both meteorclient and rusherhack.

---

- ### [Container Tweaks](https://github.com/rfresh2/ContainerTweaks-rusherhack) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[8].releaseDate&label=Latest%20Release&color=green)](https://github.com/rfresh2/ContainerTweaks-rusherhack/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/rfresh2/ContainerTweaks-rusherhack/total)](https://github.com/rfresh2/ContainerTweaks-rusherhack/releases/download/1.11/ContainerTweaks-1.11%2B1.20-1.21.1.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[8].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/rfresh2.png?size=20" width="20" height="20"> [rfresh2](https://github.com/rfresh2)

   Simple tweaks for quickly moving items in containers.

   <details>
     <summary>Show Screenshots</summary>
     <p align="center">
       <img src="./Assets/ContainerTweaks/ModuleSettings.png" alt="Module" border="0" width="250">
     </p>
   </details>

---

- ### [RusherHack Spotify Integration](https://github.com/John200410/rusherhack-spotify) <br>  

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[9].releaseDate&label=Latest%20Release&color=green)](https://github.com/John200410/rusherhack-spotify/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/John200410/rusherhack-spotify/total)](https://github.com/John200410/rusherhack-spotify/releases/download/1.2.1/rusherhack-spotify-1.2.1.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[9].badge_version&label=MC%20Version&color=blueviolet)<br>

   **Creator**: <img src="https://github.com/John200410.png?size=20" width="20" height="20"> [John200410](https://github.com/John200410)  

   Integrates Spotify music playback controls and status into the RusherHacks client.  

   <details>  
     <summary>Show Screenshots</summary>  
     <p align="center">  
       <img src="./Assets/spotify/Module.png" alt="Module" border="0" width="250">  
       <img src="./Assets/spotify/HudElement.png" alt="Spotify Hud Element" border="0" width="450">  
     </p>  
   </details>

---

- ### [Vanilla Elytra Flight](https://github.com/FBanna/Rusherhack-Vanilla-Efly) <br>  

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[10].releaseDate&label=Latest%20Release&color=green)](https://github.com/FBanna/Rusherhack-Vanilla-Efly/releases) [![Download Latest Version](https://img.shields.io/github/downloads/FBanna/Rusherhack-Vanilla-Efly/total)](https://github.com/FBanna/Rusherhack-Vanilla-Efly/releases/download/2.1.2%2B1.21.4/FBanna.s-efly-2.1.2.jar)  
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[10].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/FBanna.png?size=20" width="20" height="20"> [FBanna](https://github.com/FBanna)  

   Highly customizable rusher hack elytra flight plugin.

---

- ### [Rusherhack BookBot](https://github.com/Aspect-404/Rusherhack-BookBot) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[11].releaseDate&label=Latest%20Release&color=green)](https://github.com/Aspect-404/Rusherhack-BookBot/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Aspect-404/Rusherhack-BookBot/total)](https://github.com/Aspect-404/Rusherhack-BookBot/releases/download/Release/BookBot.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[11].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/Aspect-404.png?size=20" width="20" height="20"> [Aspect-404](https://github.com/Aspect-404)

   Rusherhack plugin for bookbot.

---

- ### [Shay's RusherTweaks](https://github.com/ShayBox/ShaysRusherTweaks) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[12].releaseDate&label=Latest%20Release&color=green)](https://github.com/ShayBox/ShaysRusherTweaks/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/ShayBox/ShaysRusherTweaks/total)](https://github.com/ShayBox/ShaysRusherTweaks/releases/download/0.10.2/ShaysRusherPlugin-1.20.1-0.10.2.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[12].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/ShayBox.png?size=20" width="20" height="20"> [ShayBox](https://github.com/ShayBox)

   A collection of small tweaks and improvements for the RusherHacks client.

---

- ### [Nuker](https://github.com/beanbag44/Nuker) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[13].releaseDate&label=Latest%20Release&color=green)](https://github.com/beanbag44/Nuker/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/beanbag44/Nuker/total)](https://github.com/beanbag44/Nuker/releases)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[13].badge_version&label=MC%20Version&color=blueviolet)<br>

   **Creator**: <img src="https://github.com/beanbag44.png?size=20" width="20" height="20"> [beanbag44](https://github.com/beanbag44)

   Epic nuker for nuking terrain.

   <details>
     <summary>Show Screenshots/Videos</summary>
     <p align="center">
       <a href="https://www.youtube.com/watch?v=JUhgqLYdONs">
         <img src="https://img.youtube.com/vi/JUhgqLYdONs/0.jpg" alt="Nuker Demo">
       </a>
     </p>
   </details>

---

- ### [Hold Rusher](https://github.com/cherosin/hold-rusher) <br>  

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[14].releaseDate&label=Latest%20Release&color=green)](https://github.com/cherosin/hold-rusher/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/cherosin/hold-rusher/total)](https://github.com/cherosin/hold-rusher/releases/download/1.0.1/hold-rusher-1.0.1.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[14].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/cherosin.png?size=20" width="20" height="20"> [cherosin](https://github.com/cherosin)  

   Adds a "Hold" flag for all modules, if active keybind will only be toggled while held.

---

- ### [No Walk Animation](https://github.com/Eonexe/NoWalkAnimation) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[15].releaseDate&label=Latest%20Release&color=green)](https://github.com/Eonexe/NoWalkAnimation/releases) [![Download Latest Version](https://img.shields.io/github/downloads/Eonexe/NoWalkAnimation/total)](https://github.com/Eonexe/NoWalkAnimation/releases/download/1.20.6/no-walk-animations-0.1.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[15].badge_version&label=MC%20Version&color=blueviolet)<br>

   **Creator**: <img src="https://github.com/Eonexe.png?size=20" width="20" height="20"> [Eonexe](https://github.com/Eonexe)

   Removes the walking animation.

---

- ### [NBT Utils](https://github.com/kybe236/rusherhack-nbt-utils) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[16].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-nbt-utils/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusherhack-nbt-utils/total)](https://github.com/kybe236/rusherhack-nbt-utils/releases/latest/download/nbt-reader-0.1.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[16].badge_version&label=MC%20Version&color=blueviolet)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   Rusher nbt paste and copy.

---

- ### [Rusherhack Executer](https://github.com/kybe236/rusherhack-executer) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[17].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-executer/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusherhack-executer/total)](https://github.com/kybe236/rusherhack-executer/releases/latest/download/kybes-executer-5.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[17].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   Executes commands and resolves `<player>` to every player online.

---

- ### [F3 Spoof](https://github.com/Doogie13/f3-spoof) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[18].releaseDate&label=Latest%20Release&color=orange)](https://github.com/Doogie13/f3-spoof/releases) ![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Doogie13/f3-spoof/total)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[18].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/Doogie13.png?size=20" width="20" height="20"> [Doogie13](https://github.com/Doogie13)

   Spoofs the F3 debug screen information.

---

- ### [Open Folder](https://github.com/kybe236/rusherhack-open-folder) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[19].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-open-folder/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusherhack-open-folder/total)](https://github.com/kybe236/rusherhack-open-folder/releases/latest/download/open-folder-0.0.9.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[19].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   Opens the folder for the module with a button click.

   <details>
     <summary>Show Screenshots/Videos</summary>
     <p align="center">
       <a href="https://www.youtube.com/watch?v=m_O0ruTdto8">
         <img src="https://img.youtube.com/vi/m_O0ruTdto8/0.jpg" alt="Open Folder Demo">
       </a>
     </p>
   </details>

---

- ### [Mace Kill](https://github.com/kybe236/rusherhack-mace-kill) <br>  

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[20].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-mace-kill/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusherhack-mace-kill/total)](https://github.com/kybe236/rusherhack-mace-kill/releases/download/1.21.4/mace-kill-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[20].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)  

   One shot pretty much all mobs with a mace.  

   <details>  
     <summary>Show Screenshots/Videos</summary>  
     <p align="center">  
       <a href="https://www.youtube.com/watch?v=seP5OqcnFT4">  
         <img src="https://img.youtube.com/vi/seP5OqcnFT4/0.jpg" alt="Mace Kill Demo">  
       </a>  
     </p>  
   </details>

---

- ### [Weather Changing Plugin](https://github.com/Lokfid/WeatherChangingPlugin) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[21].releaseDate&label=Latest%20Release&color=green)](https://github.com/Lokfid/WeatherChangingPlugin/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Lokfid/WeatherChangingPlugin/total)](https://github.com/Lokfid/WeatherChangingPlugin/releases/latest/download/WeatherPlugin-1.0.2.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[21].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/Lokfid.png?size=20" width="20" height="20"> [Lokfid](https://github.com/Lokfid)

   Allows players to change the weather in-game.

---

- ### [Middleclick Wind Charge](https://github.com/kybe236/rusherhack-middleclick-wind-charge) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[22].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-middleclick-wind-charge/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusherhack-middleclick-wind-charge/total)](https://github.com/kybe236/rusherhack-middleclick-wind-charge/releases/download/1.21-1.0.1/rusherhack-middleclick-wind-charge-1.0.1.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[22].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   Allows you to throw windcharges with the middle mouse button and also jump at the same time so you can boost jump.

   <details>
     <summary>Show Screenshots/Videos</summary>
     <p align="center">
       <a href="https://www.youtube.com/watch?v=kaFZWN27RaY">
         <img src="https://img.youtube.com/vi/kaFZWN27RaY/0.jpg" alt="Middleclick Wind Charge Demo">
       </a>
     </p>
   </details>

---

- ### [GarlicSight](https://github.com/GarlicRot/GarlicSight) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[23].releaseDate&label=Latest%20Release&color=green)](https://github.com/GarlicRot/GarlicSight/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/GarlicRot/GarlicSight/total)](https://github.com/GarlicRot/GarlicSight/releases)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[23].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/GarlicRot.png?size=20" width="20" height="20"> [GarlicRot](https://github.com/GarlicRot)

   A RusherHacks Plugin - Crosshair Info - GarlicSight.

   <details>
     <summary>Show Screenshots</summary>
     <p align="center">
       <img src="./Assets/GarlicSight/hudinfo.png" alt="Hud Element" border="0" width="250">
       <img src="./Assets/GarlicSight/blockinfo.png" alt="Block Info" border="0" width="300">
       <img src="./Assets/GarlicSight/entityinfo.png" alt="Entity Info" border="0" width="300">
     </p>
   </details>

---

- ### [LightningPop](https://github.com/GarlicRot/LightningPop) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[24].releaseDate&label=Latest%20Release&color=green)](https://github.com/GarlicRot/LightningPop/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/GarlicRot/LightningPop/total)](https://github.com/GarlicRot/LightningPop/releases)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[24].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/GarlicRot.png?size=20" width="20" height="20"> [GarlicRot](https://github.com/GarlicRot)

   A RusherHacks Plugin - Spawns Lightning On Totem Pops And Player Deaths - LightningPop.

   <details>
     <summary>Show Screenshots</summary>
     <p align="center">
       <img src="./Assets/LightningPop/Module.png" alt="Module" border="0" width="250">
     </p>
   </details>

---

- ### [AutoBucket](https://github.com/GarlicRot/AutoBucket) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[25].releaseDate&label=Latest%20Release&color=green)](https://github.com/GarlicRot/AutoBucket/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/GarlicRot/AutoBucket/total)](https://github.com/GarlicRot/AutoBucket/releases)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[25].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/GarlicRot.png?size=20" width="20" height="20"> [GarlicRot](https://github.com/GarlicRot)

   A RusherHacks Plugin - Auto Bucket Entities - AutoBucket.

   <details>
     <summary>Show Screenshots</summary>
     <p align="center">
       <img src="./Assets/AutoBucket/module.png" alt="Module" border="0" width="250">
     </p>
   </details>

---

- ### [RusherHack-BoatExecute](https://github.com/PhilipPanda/RusherHack-BoatExecute) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[26].releaseDate&label=Latest%20Release&color=green)](https://github.com/PhilipPanda/RusherHack-BoatExecute/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/PhilipPanda/RusherHack-BoatExecute/total)](https://github.com/PhilipPanda/RusherHack-BoatExecute/releases/latest/download/boatexecute-1.20.4.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[26].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/PhilipPanda.png?size=20" width="20" height="20"> [PhilipPanda](https://github.com/PhilipPanda)

   A RusherHack module plugin for 1.20.4 that exploits boat movement packets to instantly kill all passengers.

   <details>
     <summary>Show Screenshots/Videos</summary>
     <p align="center">
       <a href="https://www.youtube.com/watch?v=h35gKz9ZQK4&t=31s">
         <img src="https://img.youtube.com/vi/h35gKz9ZQK4/0.jpg" alt="BoatExecute Demo">
       </a>
     </p>
   </details>

---

- ### [NBT Viewer](https://github.com/Gentleman2292/NBT-viewer) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[27].releaseDate&label=Latest%20Release&color=green)](https://github.com/Gentleman2292/NBT-viewer/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Gentleman2292/NBT-viewer/total)](https://github.com/Gentleman2292/NBT-viewer/releases/latest/download/NBTViewer-plugin-1.2-release.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[27].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/Gentleman2292.png?size=20" width="20" height="20"> [Gentleman2292](https://github.com/Gentleman2292)

   A plugin to view NBT data in Minecraft.

   <details>
     <summary>Show Screenshots</summary>
     <p align="center">
       <img src="./Assets/NBT-viewer/NBT-viewer.png" alt="NBT-viewer" border="0" width="750">
     </p>
   </details>

---

- ### [Remote Control](https://github.com/kybe236/rusherhack-remote-controle) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[28].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-remote-controle/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusherhack-remote-controle/total)](https://github.com/kybe236/rusherhack-remote-controle/releases/latest/download/remote-control-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[28].badge_version&label=MC%20Version&color=blueviolet)<br>
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin for remote controlling RusherHacks.

---

- ### [Speed Measure](https://github.com/Lokfid/RusherHackSpeedMeasure) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[29].releaseDate&label=Latest%20Release&color=green)](https://github.com/Lokfid/RusherHackSpeedMeasure/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Lokfid/RusherHackSpeedMeasure/total)](https://github.com/Lokfid/RusherHackSpeedMeasure/releases/latest/download/SpeedMeasure-1.0.1.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[29].badge_version&label=MC%20Version&color=blueviolet)<br>

   **Creator**: <img src="https://github.com/Lokfid.png?size=20" width="20" height="20"> [Lokfid](https://github.com/Lokfid)

   A plugin to measure speed in RusherHacks.

   **Original Creator**: <img src="https://github.com/IceTank.png?size=20" width="20" height="20"> [IceTank](https://github.com/IceTank)

---

- ### [TNT Bomber](https://github.com/kybe236/rusher-tnt-bomber) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[30].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-tnt-bomber/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-tnt-bomber/total)](https://github.com/kybe236/rusher-tnt-bomber/releases/latest/download/tnt-nuker-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[30].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin to automate TNT bombing in Minecraft.

---

- ### [No Render Entities](https://github.com/John200410/norender-entities) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[31].releaseDate&label=Latest%20Release&color=green)](https://github.com/John200410/norender-entities/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/John200410/norender-entities/total)](https://github.com/John200410/norender-entities/releases/download/v1.0/norender-entities-1.0-SNAPSHOT.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[31].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/John200410.png?size=20" width="20" height="20"> [John200410](https://github.com/John200410)

   A plugin to disable rendering of entities.

---

- ### [RusherHack Messenger](https://github.com/Gentleman2292/rusherhack-messenger) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[32].releaseDate&label=Latest%20Release&color=green)](https://github.com/Gentleman2292/rusherhack-messenger/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Gentleman2292/rusherhack-messenger/total)](https://github.com/Gentleman2292/rusherhack-messenger/releases/latest/download/messenger-plugin-1.0.3.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[32].badge_version&label=MC%20Version&color=blueviolet)<br>

   **Creator**: <img src="https://github.com/Gentleman2292.png?size=20" width="20" height="20"> [Gentleman2292](https://github.com/Gentleman2292)

   A messaging plugin for RusherHacks.

   <details>
     <summary>Show Screenshots/Videos</summary>
     <p align="center">
       <a href="https://rusherhack.org/i/14z9f6ewlu.mp4">
         <img src="./Assets/rusherhack-messenger/rusherhack-messenger-demo.jpg" alt="rusherhack-messenger Demo">
       </a>
     </p>
   </details>

---

- ### [RusherHack Instance Info (Fork)](https://github.com/GarlicRot/rusherhack-instance-info) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[33].releaseDate&label=Latest%20Release&color=green)](https://github.com/GarlicRot/rusherhack-instance-info/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/GarlicRot/rusherhack-instance-info/total)](https://github.com/GarlicRot/rusherhack-instance-info/releases/latest/download/instance-info-1.3.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[33].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/GarlicRot.png?size=20" width="20" height="20"> [GarlicRot](https://github.com/GarlicRot)

   A forked version of the [original plugin](https://github.com/John200410/rusherhack-instance-info) with custom settings.

   <details>
     <summary>Show Screenshots</summary>
     <p align="center">
       <img src="./Assets/rusherhack-instance-info-fork/Module.png" alt="Module" border="0" width="350">
       <img src="./Assets/rusherhack-instance-info-fork/PlayerHead.png" alt="Player Head Info" border="0" width="250">
       <img src="./Assets/rusherhack-instance-info-fork/WindowInfo.png" alt="Player Head Info" border="0" width="550">
     </p>
   </details>

---

- ### [RusherHack NoteBot](https://github.com/Lokfid/RusherHackNoteBot) <br>  

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[34].releaseDate&label=Latest%20Release&color=green)](https://github.com/Lokfid/RusherHackNoteBot/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Lokfid/RusherHackNoteBot/total)](https://github.com/Lokfid/RusherHackNoteBot/releases/download/1.0.3/NoteBotPlugin-1.0.3.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[34].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/Lokfid.png?size=20" width="20" height="20"> [Lokfid](https://github.com/Lokfid)  

   A RusherHacks plugin for playing note blocks in Minecraft.

---

- ### [ShulkerViewer](https://github.com/xyzbtw/ShulkerViewer) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[35].releaseDate&label=Latest%20Release&color=green)](https://github.com/xyzbtw/ShulkerViewer/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/xyzbtw/ShulkerViewer/total)](https://github.com/xyzbtw/ShulkerViewer/releases/download/1.20.6/shulker-viewer-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[35].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/xyzbtw.png?size=20" width="20" height="20"> [xyzbtw](https://github.com/xyzbtw)

   A RusherHacks plugin to view the contents of Shulker boxes in the inventory.

---

- ### [RusherWebPlugin](https://github.com/Lokfid/RusherWebPlugin) <br>  

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[36].releaseDate&label=Latest%20Release&color=green)](https://github.com/Lokfid/RusherWebPlugin/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Lokfid/RusherWebPlugin/total)](https://github.com/Lokfid/RusherWebPlugin/releases/download/1.2/web-1.2.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[36].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/Lokfid.png?size=20" width="20" height="20"> [Lokfid](https://github.com/Lokfid)  

   Web Browser for rh.

---

- ### [UpdatedNCPEfly](https://github.com/xyzbtw/UpdatedNCPEfly) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[37].releaseDate&label=Latest%20Release&color=green)](https://github.com/xyzbtw/UpdatedNCPEfly/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/xyzbtw/UpdatedNCPEfly/total)](https://github.com/xyzbtw/UpdatedNCPEfly/releases/download/release/NCP-ElytraFlight-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[37].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/xyzbtw.png?size=20" width="20" height="20"> [xyzbtw](https://github.com/xyzbtw)

   A plugin for an updated version of NCPEfly.

---

- ### [dc-chat-logger](https://github.com/kybe236/dc-chat-logger) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[38].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/dc-chat-logger/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/dc-chat-logger/total)](https://github.com/kybe236/dc-chat-logger/releases/download/3.0.0/dc-chat-logger-3.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[38].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin for logging chat messages to discord.

---

- ### [rusherhack-nightvision-plugin](https://github.com/John200410/rusherhack-nightvision-plugin) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[39].releaseDate&label=Latest%20Release&color=green)](https://github.com/John200410/rusherhack-nightvision-plugin/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/John200410/rusherhack-nightvision-plugin/total)](https://github.com/John200410/rusherhack-nightvision-plugin/releases/download/v1.0.0/nightvision-1.0.0-1.21.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[39].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/John200410.png?size=20" width="20" height="20"> [John200410](https://github.com/John200410)

   A replacement for FullBright when using shaders.

---

- ### [AutoNetherite](https://github.com/xyzbtw/AutoNetherite) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[40].releaseDate&label=Latest%20Release&color=green)](https://github.com/xyzbtw/AutoNetherite/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/xyzbtw/AutoNetherite/total)](https://github.com/xyzbtw/AutoNetherite/releases/download/release/autonetherite-release.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[40].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/xyzbtw.png?size=20" width="20" height="20"> [xyzbtw](https://github.com/xyzbtw)

   A plugin that automates the process of upgrading gear to Netherite in Minecraft.

---

- ### [OldSignsPlugin](https://github.com/xyzbtw/OldSignsPlugin) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[41].releaseDate&label=Latest%20Release&color=green)](https://github.com/xyzbtw/OldSignsPlugin/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/xyzbtw/OldSignsPlugin/total)](https://github.com/xyzbtw/OldSignsPlugin/releases/download/release/oldsigns-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[41].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/xyzbtw.png?size=20" width="20" height="20"> [xyzbtw](https://github.com/xyzbtw)

   A plugin that brings back old sign functionalities in Minecraft.

---

- ### [StashHunter-rusherhack](https://github.com/CherkaSSH/StashHunter-rusherhack) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[42].releaseDate&label=Latest%20Release&color=green)](https://github.com/CherkaSSH/StashHunter-rusherhack/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/CherkaSSH/StashHunter-rusherhack/total)](https://github.com/CherkaSSH/StashHunter-rusherhack/releases/download/hehe2/StashHunter-rusherhack-1.0.1.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[42].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/CherkaSSH.png?size=20" width="20" height="20"> [CherkaSSH](https://github.com/CherkaSSH)

   A plugin to help locate stashes in Minecraft using RusherHack.

---

- ### [rusher-elytra-eta](https://github.com/kybe236/rusher-elytra-eta) <br>
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[43].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-elytra-eta/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-elytra-eta/total)](https://github.com/kybe236/rusher-elytra-eta/releases/download/1.0.0/rusher-elytra-eta-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[43].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A rusherhack plugin that allows you to see the ETA of all Elytras in the player's inventory.

   <details>
    <summary>Show Screenshots</summary>
     <p align="center">
      <img src="./Assets/rusher-elytra-eta/HudElement.png" alt="The hud Element" border="0" width="250">
    </p>
   </details>

---

- ### [rusher-silent-close](https://github.com/kybe236/rusher-silent-close) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[44].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-silent-close/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-silent-close/total)](https://github.com/kybe236/rusher-silent-close/releases/download/1.0.0/silent-close-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[44].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   Keeps Container GUI open

---

- ### [rusherhack-addons](https://github.com/miles352/rusherhack-addons) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[45].releaseDate&label=Latest%20Release&color=green)](https://github.com/miles352/rusherhack-addons/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/miles352/rusherhack-addons/total)](https://github.com/miles352/rusherhack-addons/releases/download/1.21.1/jefffmod-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[45].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/miles352.png?size=20" width="20" height="20"> [miles352](https://github.com/miles352)

   A collection of RusherHacks addons including:
   - **AFKBoostFly**: Enables boost flying while AFK by looking up and down to gain momentum.
   - **MapCopy**: Allows you to copy maps in your inventory.

---

- ### [rusher-gtranslate](https://github.com/kybe236/rusher-gtranslate) <br>  

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[46].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-gtranslate/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-gtranslate/total)](https://github.com/kybe236/rusher-gtranslate/releases/download/2.0.0/gtranslate-v2-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[46].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)  

   A plugin that integrates Google Translate into RusherHack for translating chat messages.

---

- ### [rusher-matrix-nofall](https://github.com/kybe236/rusher-matrix-nofall) <br>
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[47].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-matrix-nofall/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-matrix-nofall/total)](https://github.com/kybe236/rusher-matrix-nofall/releases/download/1.0.0/kybe-nofall-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[47].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)
  
   No Fall by setting isFalling flag in movement packets to false (tested on 6b6t).

---

- ### [rusher-autoportal](https://github.com/kybe236/rusher-autoportal) <br>  

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[48].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-autoportal/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-autoportal/total)](https://github.com/kybe236/rusher-autoportal/releases/download/1.20.6-1.21.1/kybe-portal-maker-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[48].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)  

   Automatically breaks blocks to place obsidian and activate the nether portal.

---

- ### [rusher-air-place](https://github.com/kybe236/rusher-air-place) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[49].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-air-place/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-air-place/total)](https://github.com/kybe236/rusher-air-place/releases/download/1.0.0/kybe-airplace-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[49].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin that allows placing blocks in the air in Minecraft.

---

- ### [rusher-hold-spamm-space](https://github.com/kybe236/rusher-hold-spamm-space) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[50].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-hold-spamm-space/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-hold-spamm-space/total)](https://github.com/kybe236/rusher-hold-spamm-space/releases/download/1.0.0.1/kybe-holdspace-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[50].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin that automatically spams or holds the space bar.

---

- ### [rusher-auto-bed-bomber](https://github.com/kybe236/rusher-auto-bed-bomber) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[51].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-auto-bed-bomber/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-auto-bed-bomber/total)](https://github.com/kybe236/rusher-auto-bed-bomber/releases/download/idk/kybe-auto-bed-bomb-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[51].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin that automates bed bombing in Minecraft.

---

- ### [rusher-crystal-spin](https://github.com/kybe236/rusher-crystal-spin) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[52].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-crystal-spin/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-crystal-spin/total)](https://github.com/kybe236/rusher-crystal-spin/releases/download/1.0.0/kybe-holdspace-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[52].badge_version&label=MC%20Version&color=blueviolet)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin that makes end crystals spin faster or slower.

---

- ### [AutoShear](https://github.com/oisin404/AutoShear) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[53].releaseDate&label=Latest%20Release&color=green)](https://github.com/oisin404/AutoShear/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/oisin404/AutoShear/total)](https://github.com/oisin404/AutoShear/releases/download/1.0.2/auto-shear-1.0.2.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[53].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/oisin404.png?size=20" width="20" height="20"> [oisin404](https://github.com/oisin404)

   A plugin that automates shearing in Minecraft.

   <details>
     <summary>Show Video</summary>
     <p align="center">
       <a href="https://youtu.be/44b4QO6l1Pc"><img src="https://img.youtube.com/vi/44b4QO6l1Pc/0.jpg" alt="Video Tutorial" width="300"></a>
     </p>
   </details>

---

- ### [Rusher2b2tVelocity](https://github.com/Lokfid/Rusher2b2tVelocity) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[54].releaseDate&label=Latest%20Release&color=green)](https://github.com/Lokfid/Rusher2b2tVelocity/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Lokfid/Rusher2b2tVelocity/total)](https://github.com/Lokfid/Rusher2b2tVelocity/releases/download/1.0.0fixfix/VelocityPlus-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[54].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/Lokfid.png?size=20" width="20" height="20"> [Lokfid](https://github.com/Lokfid)

   A plugin that adds enhanced velocity control for RusherHacks on the 2b2t server.

---

- ### [rusher-autokit](https://github.com/kybe236/rusher-autokit) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[55].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-autokit/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-autokit/total)](https://github.com/kybe236/rusher-autokit/releases/download/1.0.0/kybe-autokit-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[55].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin that automatically equips your preferred kit.

---

- ### [AutoTorch](https://github.com/NinetyUnderScore/AutoTorch) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[56].releaseDate&label=Latest%20Release&color=green)](https://github.com/NinetyUnderScore/AutoTorch/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/NinetyUnderScore/AutoTorch/total)](https://github.com/NinetyUnderScore/AutoTorch/releases/download/Release/autotorch-plugin-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[56].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/NinetyUnderScore.png?size=20" width="20" height="20"> [NinetyUnderScore](https://github.com/NinetyUnderScore)

   Automatically places torches to light up areas in Minecraft.

---

- ### [Elytra Swap](https://github.com/cmg-divined/elytra-swap) <br>
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[57].releaseDate&label=Latest%20Release&color=orange)](https://github.com/cmg-divined/elytra-swap/releases) ![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/cmg-divined/elytra-swap/total)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[57].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/cmg-divined.png?size=20" width="20" height="20"> [cmg-divined](https://github.com/cmg-divined)

   Automatically swaps fully repaired Elytras with damaged ones for efficient XP farm repairs.

---

- ### [HDisabler](https://github.com/CherkaSSH/hdisabler) <br>
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[58].releaseDate&label=Latest%20Release&color=orange)](https://github.com/CherkaSSH/hdisabler/releases) ![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/CherkaSSH/hdisabler/total)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[58].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/CherkaSSH.png?size=20" width="20" height="20"> [CherkaSSH](https://github.com/CherkaSSH)
  
   2b2t fast bypass.
  
   <details>
   <summary>Show Screenshots</summary>
  <p align="center">
    <img src="./Assets/HDisabler/HDisabler.png" alt="Hud Setting" border="0" width="250">
  </p>
   </details>

---

- ### [CoordFollower](https://github.com/CherkaSSH/CoordFollower-plugin) <br>
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[59].releaseDate&label=Latest%20Release&color=orange)](https://github.com/CherkaSSH/CoordFollower-plugin/releases) ![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/CherkaSSH/CoordFollower-plugin/total)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[59].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/CherkaSSH.png?size=20" width="20" height="20"> [CherkaSSH](https://github.com/CherkaSSH)

   A plugin that allows you to save, manage, and follow coordinates with ease.

   <details>
  <summary>Show Usage Instructions</summary>
  <ul>
    <li><strong>add</strong>: Adds coordinates to the list.  
        <br> - Use <code>add</code> to add your current coordinates.  
    </li>
    <li><strong>del</strong>: Deletes coordinates from the list.  
        <br> - Use <code>del &lt;n&gt;</code> to delete the coordinate at position <code>n</code>.  
        <br> - Use <code>del</code> without parameters to delete the last coordinate in the list.  
    </li>
    <li><strong>list</strong>: Displays all saved coordinates.</li>
    <li><strong>save/load</strong>: Saves or loads the coordinate list to/from an encrypted file.  
        <br> - Files are saved as <code>name.coords</code>.  
        <br> - Files are encrypted using a password (<code>pass</code>).
    </li>
  </ul>
</details>

---

- ### [Rusher Chess TUI](https://github.com/CherkaSSH/rusher-chess-tui) <br>
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[60].releaseDate&label=Latest%20Release&color=orange)](https://github.com/CherkaSSH/rusher-chess-tui/releases) ![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/CherkaSSH/rusher-chess-tui/total)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[60].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/CherkaSSH.png?size=20" width="20" height="20"> [CherkaSSH](https://github.com/CherkaSSH)

     Chess module for RusherHacks, powered by [ChessLib](https://github.com/bhlangonijr/chesslib).

---

- ### [ActivatedSpawnerDetector](https://github.com/un0x9/ActivatedSpawnerDetector) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[61].releaseDate&label=Latest%20Release&color=green)](https://github.com/un0x9/ActivatedSpawnerDetector/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/un0x9/ActivatedSpawnerDetector/total)](https://github.com/un0x9/ActivatedSpawnerDetector/releases/download/v1.2.2/ActivatedSpawnerDetector-1.2.2.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[61].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/un0x9.png?size=20" width="20" height="20"> [un0x9](https://github.com/un0x9)

   Detects activated spawners and provides visual feedback in RusherHacks.

---

- ### [Rusher Discord Notifications](https://github.com/kybe236/rusher-discord-notifications) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[62].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-discord-notifications/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-discord-notifications/total)](https://github.com/kybe236/rusher-discord-notifications/releases/download/1.0.0/discord-notifier-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[62].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   Sends notifications from RusherHacks to a Discord channel.

---

- ### [AutoBonemeal](https://github.com/John200410/rusherhack-autobonemeal) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[63].releaseDate&label=Latest%20Release&color=green)](https://github.com/John200410/rusherhack-autobonemeal/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/John200410/rusherhack-autobonemeal/total)](https://github.com/John200410/rusherhack-autobonemeal/releases/download/v1.0.0/auto-bonemeal-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[63].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/John200410.png?size=20" width="20" height="20"> [John200410](https://github.com/John200410)

   A RusherHacks plugin for automatically applying bonemeal to crops.

---

- ### [Rocket3](https://github.com/PK268/Rocket3) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[64].releaseDate&label=Latest%20Release&color=green)](https://github.com/PK268/Rocket3/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/PK268/Rocket3/total)](https://github.com/PK268/Rocket3/releases/download/v1.2.0/rocket3-1.2.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[64].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/PK268.png?size=20" width="20" height="20"> [PK268](https://github.com/PK268)

   A RusherHacks plugin for crafting duration 3 rockets.

---

- ### [GarlicBreeder](https://github.com/GarlicRot/GarlicBreeder) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[65].releaseDate&label=Latest%20Release&color=green)](https://github.com/GarlicRot/GarlicBreeder/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/GarlicRot/GarlicBreeder/total)](https://github.com/GarlicRot/GarlicBreeder/releases/download/v1.0.0/GarlicBreeder-1.20.4.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[65].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/GarlicRot.png?size=20" width="20" height="20"> [GarlicRot](https://github.com/GarlicRot)

   A RusherHacks plugin that automates the breeding of mobs in Minecraft.

---

- ### [Rusher Item Saver](https://github.com/kybe236/rusher-item-saver) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[66].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-item-saver/releases) 
   [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-item-saver/total)](https://github.com/kybe236/rusher-item-saver/releases/download/multiversion/item-saver-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[66].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A RusherHacks plugin that saves items from being lost.

---

- ### [RusherHack Mace Swap](https://github.com/kybe236/rusherhack-mace-swap) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[67].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-mace-swap/releases) 
   [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusherhack-mace-swap/total)](https://github.com/kybe236/rusherhack-mace-swap/releases/download/fix1/mace-swap-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[67].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A RusherHacks plugin that automatically swaps to a mace when attacking.

---

- ### [Example Core Plugin](https://github.com/RusherDevelopment/example-core-plugin)

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[69].releaseDate&label=Latest%20Release&color=red)](https://github.com/RusherDevelopment/example-core-plugin/releases) ![Core Plugin](https://img.shields.io/badge/Core%20Plugin-blue) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/RusherDevelopment/example-core-plugin/total)](https://github.com/RusherDevelopment/example-core-plugin/releases/download/v1.0.0/example-core-plugin-1.0.0.jar)  

   **Creator**: <img src="https://github.com/RusherDevelopment.png?size=20" width="20" height="20"> [RusherDevelopment](https://github.com/RusherDevelopment)  

   A core plugin example demonstrating mixin support in RusherHack.

---

- ### [CrystalModifierRH](https://github.com/xyzbtw/CrystalModifierRH)

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[69].releaseDate&label=Latest%20Release&color=red)](https://github.com/xyzbtw/CrystalModifierRH) ![Core Plugin](https://img.shields.io/badge/Core%20Plugin-blue) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/xyzbtw/CrystalModifierRH/total)](https://github.com/xyzbtw/CrystalModifierRH/releases)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[69].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/xyzbtw.png?size=20" width="20" height="20"> [xyzbtw](https://github.com/xyzbtw)  

   A plugin for modifying the rendering of end crystals in Minecraft using mixins in RusherHack.

---

- ### [Tablist Hats](https://github.com/rfresh2/TablistHats-rusherhack)

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[70].releaseDate&label=Latest%20Release&color=green)](https://github.com/rfresh2/TablistHats-rusherhack/releases) ![Core Plugin](https://img.shields.io/badge/Core%20Plugin-blue) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/rfresh2/TablistHats-rusherhack/total)](https://github.com/rfresh2/TablistHats-rusherhack/releases/download/1.0/TablistHats-1.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[70].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/rfresh2.png?size=20" width="20" height="20"> [rfresh2](https://github.com/rfresh2)  

   Enables hat layer rendering for player heads on the tablist, even if the player isn't in render distance.

   <details>
     <summary>Show Screenshot</summary>
     <p align="center">
       <img src="https://i.imgur.com/HEfpmLw.png" alt="Tablist Hats Example" border="0" width="300">
     </p>
   </details>

---

- ### [NoSound](https://github.com/John200410/nosound)

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[71].releaseDate&label=Latest%20Release&color=red)](https://github.com/John200410/nosound) ![Core Plugin](https://img.shields.io/badge/Core%20Plugin-blue) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/John200410/nosound/total)](https://github.com/John200410/nosound/releases)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[71].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/John200410.png?size=20" width="20" height="20"> [John200410](https://github.com/John200410)  

   A core plugin that disables specific in-game sounds in RusherHack.

---

- ### [RusherHack Coord Spoofer](https://github.com/kybe236/rusherhack-coord-spoofer)

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[72].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-coord-spoofer/releases) ![Core Plugin](https://img.shields.io/badge/Core%20Plugin-blue) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusherhack-coord-spoofer/total)](https://github.com/kybe236/rusherhack-coord-spoofer/releases/download/1.21%2B/coord-spoofer-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[72].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)  

   A core plugin for spoofing player coordinates in RusherHack.

---

- ### [Rusher Auto Item Frame Dupe](https://github.com/kybe236/rusher-auto-item-frame-dupe)  

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[73].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-auto-item-frame-dupe/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-auto-item-frame-dupe/total)](https://github.com/kybe236/rusher-auto-item-frame-dupe/releases/download/1.21.1-1.21.4/rusher-auto-item-frame-dupe-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[73].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)  

   A plugin for automating item frame duplication in RusherHack.

---

- ### [RusherMoji](https://github.com/Lokfid/RusherMoji)  

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[74].releaseDate&label=Latest%20Release&color=green)](https://github.com/Lokfid/RusherMoji/releases) ![Core Plugin](https://img.shields.io/badge/Core%20Plugin-blue) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Lokfid/RusherMoji/total)](https://github.com/Lokfid/RusherMoji/releases/download/1.0.4/emoji-1.0.4.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[74].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/Lokfid.png?size=20" width="20" height="20"> [Lokfid](https://github.com/Lokfid)  

   A core plugin for adding custom emoji functionality in RusherHack.

---


- ### [RusherHack Piston Pusher](https://github.com/kybe236/rusherhack-piston-pusher)  

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[75].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-piston-pusher/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusherhack-piston-pusher/total)](https://github.com/kybe236/rusherhack-piston-pusher/releases/download/1.21.4/crystal-pusher-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[75].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)  

   A plugin that automates pushing end crystals with pistons to attack players in RusherHack.

---

- ### [RusherUtils](https://github.com/0tterware/RusherUtils)  

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[76].releaseDate&label=Latest%20Release&color=green)](https://github.com/0tterware/RusherUtils/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/0tterware/RusherUtils/total)](https://github.com/0tterware/RusherUtils/releases/download/v0.1/rusher-utils-0.1-1.21.4.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[76].badge_version&label=MC%20Version&color=blueviolet)<br>
   
   **Creator**: <img src="https://github.com/0tterware.png?size=20" width="20" height="20"> [0tterware](https://github.com/0tterware)  

   RusherUtils automates Wither and TNT tasks with HUD counters for RusherHack.  

   <details>  
     <summary>Show Screenshots/Videos</summary>  
     <p align="center">  
       <a href="https://www.youtube.com/watch?v=yv-WR1HddAw">  
         <img src="https://img.youtube.com/vi/yv-WR1HddAw/0.jpg" alt="RusherUtils Demo">  
       </a>  
     </p>  
   </details>

---

- ### [Rusher Grown ESP](https://github.com/kybe236/rusher-grown-esp)  

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[77].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-grown-esp/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-grown-esp/total)](https://github.com/kybe236/rusher-grown-esp/releases/latest/download/grown-esp-1.0.0.jar)<br>
   ![MC Version](https://img.shields.io/badge/dynamic/json?url=https://rusherdevelopment.github.io/rusherhack-plugins/plugin-mc-versions.json&query=$[77].badge_version&label=MC%20Version&color=blueviolet)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)  

   ESP plugin for RusherHack that highlights grown crops and useful farm blocks.

---

[![Back to Top](https://img.shields.io/badge/↑-Back%20to%20Top-blue?style=flat)](#plugins-list)

