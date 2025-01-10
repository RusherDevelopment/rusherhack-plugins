![RusherHack Logo](./Assets/RusherHacks/rh_head.png)

# RusherHack Plugin Collection

[![Total Plugins](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=$.totalPlugins.message&label=Total%20Plugins&color=green)](#plugins-list)
[![Discord RH plugins-dev](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=$.discord.label&label=Discord&color=7289DA&logo=discord)](https://discord.com/channels/590970327870341143/1166486609479356516)
[![RusherHack v2.0.5](https://img.shields.io/badge/RusherHack-v2.0.5-purple?logo=data:image/png;base64,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)](https://rusherhack.org/changelog.html)

### ⚠️ WARNING: None of the plugins here have been verified or are confirmed to be safe. Use at your own risk!
### ❗ NOTICE: The plugins listed here are not affiliated with Rusher Development LLC.

## Introduction

This repository is a collection of third-party plugins developed for the RusherHack Utility Mod. These plugins extend the functionality of RusherHack by adding new features and tools that can enhance your gameplay experience. Please note that the plugins provided here are not officially verified or endorsed by Rusher Development LLC.

## Table of Contents

- [Installation](#installation)
- [Plugin Examples/Info](#plugin-examplesinfo)
- [Dev Tools](#dev-tools)
- [Themes](#themes)
- [Plugins List](#plugins-list)
- [Reporting Issues](#reporting-issues)
- [Contribute](#contribute)

## Installation

*Plugins are currently only able to be loaded in developer mode.

*Eventually in rusherhack v2.1 there will be an in-game plugin manager and repository for verified plugins.

**⚠️ WARNING: DO NOT ENABLE PLUGINS IF YOU DO NOT KNOW WHAT YOU ARE DOING.**

Enabling plugins in rusherhack 2.0:
- Add the JVM flag `-Drusherhack.enablePlugins=true` to the game's JVM arguments.
- Create the directory `.minecraft/rusherhack/plugins/`

Installing plugins:
- Download the desired plugin(s) `.jar` files.
- Place them in the `.minecraft/rusherhack/plugins/` directory.

Plugins in the plugins folder will be loaded on startup. 
You can reload and load new plugins while in-game by using the `*reload` command

## Plugin Examples/Info

Here are some helpful resources and examples for developing RusherHack plugins:

- [Example Plugin](https://github.com/RusherDevelopment/example-plugin): A basic example plugin demonstrating the structure and capabilities of RusherHack plugins.
- [RusherGUI](https://github.com/xyzbtw/rusherGUI): An example plugin showcasing a custom theme with RusherHack.
- [RusherHack API Javadocs](https://javadocs.rusherhack.org): The official documentation for RusherHack's API, provides detailed information on available classes, methods, and usage.

## Dev Tools

<details>
  <summary>Badge Info</summary>
  
  - **Latest Release**: Clicking on this badge will take you to the releases page for the plugin.
  - **Downloads**: Clicking on the downloads badge will directly download the latest version of the plugin.
  
</details>

These tools can assist in managing and developing RusherHack plugins:

- ### [RHP](https://github.com/kybe236/rhp) <br>
  
  [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.devTools[0].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rhp/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rhp/total)](https://github.com/kybe236/rhp/releases/download/0.0.11/rhp.exe)<br>
  
  **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

  A package manager that installs RusherHack plugins for you and sets the needed flags.

## Themes

<!-- START PLUGINS LIST -->

- ### [rusherNodusTheme](https://github.com/bakjedev/rusherNodusTheme) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[0].releaseDate&label=Latest%20Release&color=green)](https://github.com/bakjedev/rusherNodusTheme/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/bakjedev/rusherNodusTheme/total)](https://github.com/bakjedev/rusherNodusTheme/releases/latest/download/rushergui-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/bakjedev.png?size=20" width="20" height="20"> [bakjedev](https://github.com/bakjedev)

   Nodus - Best theme evaAAAA. Code is terrible. Blame xyzbtw!

   <details>
     <summary>Show Screenshots</summary>
     <p align="center">
       <img src="./Assets/rusherNodusTheme/NodusGUI.png" alt="Module" border="0" width="750">
     </p>
   </details>

---

- ### [nhack Theme](https://github.com/h1tm4nqq/Nhack-theme) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[0].releaseDate&label=Latest%20Release&color=green)](https://github.com/h1tm4nqq/Nhack-theme/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/h1tm4nqq/Nhack-theme/total)](https://github.com/h1tm4nqq/Nhack-theme/releases/latest/download/rushergui-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/h1tm4nqq.png?size=20" width="20" height="20"> [h1tm4nqq](https://github.com/h1tm4nqq)

   A theme like Nhack 2015 for RH.

---

- ### [RusherGUI](https://github.com/xyzbtw/rusherGUI) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[1].releaseDate&label=Latest%20Release&color=green)](https://github.com/xyzbtw/rusherGUI/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/xyzbtw/rusherGUI/total)](https://github.com/xyzbtw/rusherGUI/releases/latest/download/rushergui-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/xyzbtw.png?size=20" width="20" height="20"> [xyzbtw](https://github.com/xyzbtw)

   An example plugin showcasing how to create custom themes with RusherHack.

## Plugins List

- ### [Example Plugin](https://github.com/RusherDevelopment/example-plugin) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[2].releaseDate&label=Latest%20Release&color=orange)](https://github.com/RusherDevelopment/example-plugin/releases) ![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/RusherDevelopment/example-plugin/total)<br>

   **Creator**: <img src="https://github.com/RusherDevelopment.png?size=20" width="20" height="20"> [RusherDevelopment](https://github.com/RusherDevelopment)

   A basic example plugin demonstrating the structure and capabilities of RusherHacks plugins.

---

- ### [2b2t.vc Rusherhack](https://github.com/rfresh2/2b2t.vc-rusherhack) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[3].releaseDate&label=Latest%20Release&color=green)](https://github.com/rfresh2/2b2t.vc-rusherhack/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/rfresh2/2b2t.vc-rusherhack/total)](https://github.com/rfresh2/2b2t.vc-rusherhack/releases/download/1.10/2b2t.vc-rusherhack-1.10.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[4].releaseDate&label=Latest%20Release&color=green)](https://github.com/Aspect-404/RusherHack-HudElement/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Aspect-404/RusherHack-HudElement/total)](https://github.com/Aspect-404/RusherHack-HudElement/releases/download/Release/HudElement.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[5].releaseDate&label=Latest%20Release&color=green)](https://github.com/IceTank/AutoAnvilRename/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/IceTank/AutoAnvilRename/total)](https://github.com/IceTank/AutoAnvilRename/releases/download/v0.1/AutoAnvilRename-v0.1.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[6].releaseDate&label=Latest%20Release&color=green)](https://github.com/GabiRP/QueueManager/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/GabiRP/QueueManager/total)](https://github.com/GabiRP/QueueManager/releases/latest/download/QueueManager.Rusher-1.0-SNAPSHOT.jar)<br>

   **Creator**: <img src="https://github.com/GabiRP.png?size=20" width="20" height="20"> [GabiRP](https://github.com/GabiRP)

   Manages queue positions and notifies users of their status.

---

- ### [RusherHack Instance Info](https://github.com/John200410/rusherhack-instance-info) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[7].releaseDate&label=Latest%20Release&color=green)](https://github.com/John200410/rusherhack-instance-info/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/John200410/rusherhack-instance-info/total)](https://github.com/John200410/rusherhack-instance-info/releases/download/v1.2.1/instance-info-1.2.1.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[8].releaseDate&label=Latest%20Release&color=green)](https://github.com/xyzbtw/StashMoverPlugin/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/xyzbtw/StashMoverPlugin/total)](https://github.com/xyzbtw/StashMoverPlugin/releases/tag/FINAL)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[9].releaseDate&label=Latest%20Release&color=orange)](https://github.com/czho/unified-modulelist/releases) ![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/czho/unified-modulelist/total)<br>

   **Creator**: <img src="https://github.com/czho.png?size=20" width="20" height="20"> [czho](https://github.com/czho)

   Rusherhack HUD element that shows active modules from both meteorclient and rusherhack.

---

- ### [Container Tweaks](https://github.com/rfresh2/ContainerTweaks-rusherhack) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[10].releaseDate&label=Latest%20Release&color=green)](https://github.com/rfresh2/ContainerTweaks-rusherhack/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/rfresh2/ContainerTweaks-rusherhack/total)](https://github.com/rfresh2/ContainerTweaks-rusherhack/releases/download/1.9/ContainerTweaks-rusherhack-1.9.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[11].releaseDate&label=Latest%20Release&color=green)](https://github.com/John200410/rusherhack-spotify/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/John200410/rusherhack-spotify/total)](https://github.com/John200410/rusherhack-spotify/releases/download/1.1.8/rusherhack-spotify-1.1.8.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[12].releaseDate&label=Latest%20Release&color=green)](https://github.com/FBanna/Rusherhack-Vanilla-Efly/releases) [![Download Latest Version](https://img.shields.io/github/downloads/FBanna/Rusherhack-Vanilla-Efly/total)](https://github.com/FBanna/Rusherhack-Vanilla-Efly/releases/download/1.1.0_1.20.4/FBanna.s-efly-1.20.4-1.1.0.jar)<br>

   **Creator**: <img src="https://github.com/FBanna.png?size=20" width="20" height="20"> [FBanna](https://github.com/FBanna)

   Highly customizable rusher hack elytra flight plugin.

---

- ### [Rusherhack BookBot](https://github.com/Aspect-404/Rusherhack-BookBot) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[13].releaseDate&label=Latest%20Release&color=green)](https://github.com/Aspect-404/Rusherhack-BookBot/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Aspect-404/Rusherhack-BookBot/total)](https://github.com/Aspect-404/Rusherhack-BookBot/releases/download/Release/BookBot.jar)<br>

   **Creator**: <img src="https://github.com/Aspect-404.png?size=20" width="20" height="20"> [Aspect-404](https://github.com/Aspect-404)

   Rusherhack plugin for bookbot.

---

- ### [Shay's RusherTweaks](https://github.com/ShayBox/ShaysRusherTweaks) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[14].releaseDate&label=Latest%20Release&color=green)](https://github.com/ShayBox/ShaysRusherTweaks/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/ShayBox/ShaysRusherTweaks/total)](https://github.com/ShayBox/ShaysRusherTweaks/releases/tag/0.10.2)<br>

   **Creator**: <img src="https://github.com/ShayBox.png?size=20" width="20" height="20"> [ShayBox](https://github.com/ShayBox)

   A collection of small tweaks and improvements for the RusherHacks client.

---

- ### [Nuker](https://github.com/beanbag44/Nuker) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[15].releaseDate&label=Latest%20Release&color=green)](https://github.com/beanbag44/Nuker/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/beanbag44/Nuker/total)](https://github.com/beanbag44/Nuker/releases/latest/download/nuker-1.0.9.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[16].releaseDate&label=Latest%20Release&color=green)](https://github.com/cherosin/hold-rusher/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/cherosin/hold-rusher/total)](https://github.com/cherosin/hold-rusher/releases/download/1.0.0/hold-rusher-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/cherosin.png?size=20" width="20" height="20"> [cherosin](https://github.com/cherosin)

   Adds a "Hold" flag for all modules, if active keybind will only be toggled while held.

---

- ### [No Walk Animation](https://github.com/Eonexe/NoWalkAnimation) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[17].releaseDate&label=Latest%20Release&color=green)](https://github.com/Eonexe/NoWalkAnimation/releases) [![Download Latest Version](https://img.shields.io/github/downloads/Eonexe/NoWalkAnimation/total)](https://github.com/Eonexe/NoWalkAnimation/releases/download/1.20.6/no-walk-animations-0.1.0.jar)<br>

   **Creator**: <img src="https://github.com/Eonexe.png?size=20" width="20" height="20"> [Eonexe](https://github.com/Eonexe)

   Removes the walking animation.

---

- ### [NBT Utils](https://github.com/kybe236/rusherhack-nbt-utils) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[18].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-nbt-utils/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusherhack-nbt-utils/total)](https://github.com/kybe236/rusherhack-nbt-utils/releases/latest/download/nbt-reader-0.1.0.jar)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   Rusher nbt paste and copy.

---

- ### [Rusherhack Executer](https://github.com/kybe236/rusherhack-executer) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[19].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-executer/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusherhack-executer/total)](https://github.com/kybe236/rusherhack-executer/releases/latest/download/kybes-executer-5.0.0.jar)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   Executes commands and resolves `<player>` to every player online.

---

- ### [F3 Spoof](https://github.com/Doogie13/f3-spoof) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[20].releaseDate&label=Latest%20Release&color=orange)](https://github.com/Doogie13/f3-spoof/releases) ![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Doogie13/f3-spoof/total)
   <br>

   **Creator**: <img src="https://github.com/Doogie13.png?size=20" width="20" height="20"> [Doogie13](https://github.com/Doogie13)

   Spoofs the F3 debug screen information.

---

- ### [Open Folder](https://github.com/kybe236/rusherhack-open-folder) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[21].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-open-folder/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusherhack-open-folder/total)](https://github.com/kybe236/rusherhack-open-folder/releases/latest/download/open-folder-0.0.9.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[22].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-mace-kill/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusherhack-mace-kill/total)](https://github.com/kybe236/rusherhack-mace-kill/releases/download/1.21.1%2C1.21/kybe-mace-killer-1.1.0.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[23].releaseDate&label=Latest%20Release&color=green)](https://github.com/Lokfid/WeatherChangingPlugin/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Lokfid/WeatherChangingPlugin/total)](https://github.com/Lokfid/WeatherChangingPlugin/releases/latest/download/WeatherPlugin-1.0.2.jar)<br>

   **Creator**: <img src="https://github.com/Lokfid.png?size=20" width="20" height="20"> [Lokfid](https://github.com/Lokfid)

   Allows players to change the weather in-game.

---

- ### [Middleclick Wind Charge](https://github.com/kybe236/rusherhack-middleclick-wind-charge) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[24].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-middleclick-wind-charge/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusherhack-middleclick-wind-charge/total)](https://github.com/kybe236/rusherhack-middleclick-wind-charge/releases/download/1.21-1.0.1/rusherhack-middleclick-wind-charge-1.0.1.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[25].releaseDate&label=Latest%20Release&color=green)](https://github.com/GarlicRot/GarlicSight/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/GarlicRot/GarlicSight/total)](https://github.com/GarlicRot/GarlicSight/releases/latest/download/Garlic-Sight-1.0.1.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[26].releaseDate&label=Latest%20Release&color=green)](https://github.com/GarlicRot/LightningPop/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/GarlicRot/LightningPop/total)](https://github.com/GarlicRot/LightningPop/releases/download/v1.0.3/LightningPop-1.0.3.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[27].releaseDate&label=Latest%20Release&color=green)](https://github.com/GarlicRot/AutoBucket/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/GarlicRot/AutoBucket/total)](https://github.com/GarlicRot/AutoBucket/releases/download/v1.0.4/AutoBucket-1.0.4.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[28].releaseDate&label=Latest%20Release&color=green)](https://github.com/PhilipPanda/RusherHack-BoatExecute/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/PhilipPanda/RusherHack-BoatExecute/total)](https://github.com/PhilipPanda/RusherHack-BoatExecute/releases/latest/download/boatexecute-1.20.4.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[29].releaseDate&label=Latest%20Release&color=green)](https://github.com/Gentleman2292/NBT-viewer/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Gentleman2292/NBT-viewer/total)](https://github.com/Gentleman2292/NBT-viewer/releases/latest/download/NBTViewer-plugin-1.2-release.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[30].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-remote-controle/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusherhack-remote-controle/total)](https://github.com/kybe236/rusherhack-remote-controle/releases/latest/download/remote-control-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin for remote controlling RusherHacks.

---

- ### [Speed Measure](https://github.com/Lokfid/RusherHackSpeedMeasure) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[31].releaseDate&label=Latest%20Release&color=green)](https://github.com/Lokfid/RusherHackSpeedMeasure/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Lokfid/RusherHackSpeedMeasure/total)](https://github.com/Lokfid/RusherHackSpeedMeasure/releases/latest/download/SpeedMeasure-1.0.1.jar)<br>

   **Creator**: <img src="https://github.com/Lokfid.png?size=20" width="20" height="20"> [Lokfid](https://github.com/Lokfid)

   A plugin to measure speed in RusherHacks.

   **Original Creator**: <img src="https://github.com/IceTank.png?size=20" width="20" height="20"> [IceTank](https://github.com/IceTank)

---

- ### [TNT Bomber](https://github.com/kybe236/rusher-tnt-bomber) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[32].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-tnt-bomber/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-tnt-bomber/total)](https://github.com/kybe236/rusher-tnt-bomber/releases/latest/download/tnt-nuker-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin to automate TNT bombing in Minecraft.

---

- ### [No Render Entities](https://github.com/John200410/norender-entities) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[33].releaseDate&label=Latest%20Release&color=green)](https://github.com/John200410/norender-entities/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/John200410/norender-entities/total)](https://github.com/John200410/norender-entities/releases/download/v1.0/norender-entities-1.0-SNAPSHOT.jar)<br>

   **Creator**: <img src="https://github.com/John200410.png?size=20" width="20" height="20"> [John200410](https://github.com/John200410)

   A plugin to disable rendering of entities.

---

- ### [RusherHack Messenger](https://github.com/Gentleman2292/rusherhack-messenger) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[34].releaseDate&label=Latest%20Release&color=green)](https://github.com/Gentleman2292/rusherhack-messenger/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Gentleman2292/rusherhack-messenger/total)](https://github.com/Gentleman2292/rusherhack-messenger/releases/latest/download/messenger-plugin-1.0.3.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[35].releaseDate&label=Latest%20Release&color=green)](https://github.com/GarlicRot/rusherhack-instance-info/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/GarlicRot/rusherhack-instance-info/total)](https://github.com/GarlicRot/rusherhack-instance-info/releases/latest/download/instance-info-1.3.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[36].releaseDate&label=Latest%20Release&color=green)](https://github.com/Lokfid/RusherHackNoteBot/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Lokfid/RusherHackNoteBot/total)](https://github.com/Lokfid/RusherHackNoteBot/releases/latest/download/NoteBotPlugin-1.0.2.jar)<br>

   **Creator**: <img src="https://github.com/Lokfid.png?size=20" width="20" height="20"> [Lokfid](https://github.com/Lokfid)

   A RusherHacks plugin for playing note blocks in Minecraft.

---

- ### [ShulkerViewer](https://github.com/xyzbtw/ShulkerViewer) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[37].releaseDate&label=Latest%20Release&color=green)](https://github.com/xyzbtw/ShulkerViewer/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/xyzbtw/ShulkerViewer/total)](https://github.com/xyzbtw/ShulkerViewer/releases/download/1.20.6/shulker-viewer-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/xyzbtw.png?size=20" width="20" height="20"> [xyzbtw](https://github.com/xyzbtw)

   A RusherHacks plugin to view the contents of Shulker boxes in the inventory.

---

- ### [RusherWebPlugin](https://github.com/Lokfid/RusherWebPlugin) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[38].releaseDate&label=Latest%20Release&color=green)](https://github.com/Lokfid/RusherWebPlugin/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Lokfid/RusherWebPlugin/total)](https://github.com/Lokfid/RusherWebPlugin/releases/latest/download/web-1.1.1.jar)<br>

   **Creator**: <img src="https://github.com/Lokfid.png?size=20" width="20" height="20"> [Lokfid](https://github.com/Lokfid)

   Web Browser for rh.

---

- ### [UpdatedNCPEfly](https://github.com/xyzbtw/UpdatedNCPEfly) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[39].releaseDate&label=Latest%20Release&color=green)](https://github.com/xyzbtw/UpdatedNCPEfly/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/xyzbtw/UpdatedNCPEfly/total)](https://github.com/xyzbtw/UpdatedNCPEfly/releases/download/release/NCP-ElytraFlight-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/xyzbtw.png?size=20" width="20" height="20"> [xyzbtw](https://github.com/xyzbtw)

   A plugin for an updated version of NCPEfly.

---

- ### [dc-chat-logger](https://github.com/kybe236/dc-chat-logger) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[40].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/dc-chat-logger/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/dc-chat-logger/total)](https://github.com/kybe236/dc-chat-logger/releases/download/3.0.0/dc-chat-logger-3.0.0.jar)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin for logging chat messages to discord.

---

- ### [rusherhack-nightvision-plugin](https://github.com/John200410/rusherhack-nightvision-plugin) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[41].releaseDate&label=Latest%20Release&color=green)](https://github.com/John200410/rusherhack-nightvision-plugin/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/John200410/rusherhack-nightvision-plugin/total)](https://github.com/John200410/rusherhack-nightvision-plugin/releases/download/v1.0.0/nightvision-1.0.0-1.21.jar)<br>

   **Creator**: <img src="https://github.com/John200410.png?size=20" width="20" height="20"> [John200410](https://github.com/John200410)

   A replacement for FullBright when using shaders.

---

- ### [AutoNetherite](https://github.com/xyzbtw/AutoNetherite) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[42].releaseDate&label=Latest%20Release&color=green)](https://github.com/xyzbtw/AutoNetherite/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/xyzbtw/AutoNetherite/total)](https://github.com/xyzbtw/AutoNetherite/releases/download/release/autonetherite-release.jar)<br>

   **Creator**: <img src="https://github.com/xyzbtw.png?size=20" width="20" height="20"> [xyzbtw](https://github.com/xyzbtw)

   A plugin that automates the process of upgrading gear to Netherite in Minecraft.

---

- ### [OldSignsPlugin](https://github.com/xyzbtw/OldSignsPlugin) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[43].releaseDate&label=Latest%20Release&color=green)](https://github.com/xyzbtw/OldSignsPlugin/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/xyzbtw/OldSignsPlugin/total)](https://github.com/xyzbtw/OldSignsPlugin/releases/download/release/oldsigns-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/xyzbtw.png?size=20" width="20" height="20"> [xyzbtw](https://github.com/xyzbtw)

   A plugin that brings back old sign functionalities in Minecraft.

---

- ### [StashHunter-rusherhack](https://github.com/CherkaSSH/StashHunter-rusherhack) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[44].releaseDate&label=Latest%20Release&color=green)](https://github.com/CherkaSSH/StashHunter-rusherhack/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/CherkaSSH/StashHunter-rusherhack/total)](https://github.com/CherkaSSH/StashHunter-rusherhack/releases/download/hehe2/StashHunter-rusherhack-1.0.1.jar)<br>

   **Creator**: <img src="https://github.com/CherkaSSH.png?size=20" width="20" height="20"> [CherkaSSH](https://github.com/CherkaSSH)

   A plugin to help locate stashes in Minecraft using RusherHack.

---

- ### [rusher-elytra-eta](https://github.com/kybe236/rusher-elytra-eta) <br>
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[45].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-elytra-eta/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-elytra-eta/total)](https://github.com/kybe236/rusher-elytra-eta/releases/download/1.0.0/rusher-elytra-eta-1.0.0.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[46].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-silent-close/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-silent-close/total)](https://github.com/kybe236/rusher-silent-close/releases/download/1.0.0/silent-close-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   Keeps Container GUI open

---

- ### [rusherhack-addons](https://github.com/miles352/rusherhack-addons) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[47].releaseDate&label=Latest%20Release&color=green)](https://github.com/miles352/rusherhack-addons/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/miles352/rusherhack-addons/total)](https://github.com/miles352/rusherhack-addons/releases/download/1.21.1/jefffmod-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/miles352.png?size=20" width="20" height="20"> [miles352](https://github.com/miles352)

   A collection of RusherHacks addons including:
   - **AFKBoostFly**: Enables boost flying while AFK by looking up and down to gain momentum.
   - **MapCopy**: Allows you to copy maps in your inventory.

---

- ### [rusher-gtranslate](https://github.com/kybe236/rusher-gtranslate) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[48].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-gtranslate/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-gtranslate/total)](https://github.com/kybe236/rusher-gtranslate/releases/download/1.0.0/kybe-gtranslate-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin that integrates Google Translate into RusherHack for translating chat messages.

---

- ### [rusher-matrix-nofall](https://github.com/kybe236/rusher-matrix-nofall) <br>
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[49].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-matrix-nofall/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-matrix-nofall/total)](https://github.com/kybe236/rusher-matrix-nofall/releases/download/1.0.0/kybe-nofall-1.0.0.jar) <br>
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)
  
   No Fall by setting isFalling flag in movement packets to false (tested on 6b6t).

---

- ### [rusher-autoportal](https://github.com/kybe236/rusher-autoportal) <br>
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[50].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-autoportal/releases) ![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-autoportal/total) <br>
   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)
  
   Automatically breaks blocks to place obsidian and activate the nether portal.

---

- ### [rusher-air-place](https://github.com/kybe236/rusher-air-place) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[51].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-air-place/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-air-place/total)](https://github.com/kybe236/rusher-air-place/releases/download/1.0.0/kybe-airplace-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin that allows placing blocks in the air in Minecraft.

---

- ### [rusher-hold-spamm-space](https://github.com/kybe236/rusher-hold-spamm-space) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[52].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-hold-spamm-space/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-hold-spamm-space/total)](https://github.com/kybe236/rusher-hold-spamm-space/releases/download/1.0.0.1/kybe-holdspace-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin that automatically spams or holds the space bar.

---

- ### [rusher-auto-bed-bomber](https://github.com/kybe236/rusher-auto-bed-bomber) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[53].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-auto-bed-bomber/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-auto-bed-bomber/total)](https://github.com/kybe236/rusher-auto-bed-bomber/releases/download/idk/kybe-auto-bed-bomb-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin that automates bed bombing in Minecraft.

---

- ### [rusher-crystal-spin](https://github.com/kybe236/rusher-crystal-spin) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[54].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-crystal-spin/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-crystal-spin/total)](https://github.com/kybe236/rusher-crystal-spin/releases/download/1.0.0/kybe-holdspace-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin that makes end crystals spin faster or slower.

---

- ### [AutoShear](https://github.com/oisin404/AutoShear) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[55].releaseDate&label=Latest%20Release&color=green)](https://github.com/oisin404/AutoShear/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/oisin404/AutoShear/total)](https://github.com/oisin404/AutoShear/releases/download/1.0.2/auto-shear-1.0.2.jar)<br>

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

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[56].releaseDate&label=Latest%20Release&color=green)](https://github.com/Lokfid/Rusher2b2tVelocity/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/Lokfid/Rusher2b2tVelocity/total)](https://github.com/Lokfid/Rusher2b2tVelocity/releases/download/1.0.0fixfix/VelocityPlus-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/Lokfid.png?size=20" width="20" height="20"> [Lokfid](https://github.com/Lokfid)

   A plugin that adds enhanced velocity control for RusherHacks on the 2b2t server.

---

- ### [rusher-autokit](https://github.com/kybe236/rusher-autokit) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[57].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-autokit/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-autokit/total)](https://github.com/kybe236/rusher-autokit/releases/download/1.0.0/kybe-autokit-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   A plugin that automatically equips your preferred kit.

---

- ### [AutoTorch](https://github.com/NinetyUnderScore/AutoTorch) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[58].releaseDate&label=Latest%20Release&color=green)](https://github.com/NinetyUnderScore/AutoTorch/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/NinetyUnderScore/AutoTorch/total)](https://github.com/NinetyUnderScore/AutoTorch/releases/download/Release/autotorch-plugin-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/NinetyUnderScore.png?size=20" width="20" height="20"> [NinetyUnderScore](https://github.com/NinetyUnderScore)

   Automatically places torches to light up areas in Minecraft.

---

- ### [Elytra Swap](https://github.com/cmg-divined/elytra-swap) <br>
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[59].releaseDate&label=Latest%20Release&color=orange)](https://github.com/cmg-divined/elytra-swap/releases) ![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/cmg-divined/elytra-swap/total)<br>
   **Creator**: <img src="https://github.com/cmg-divined.png?size=20" width="20" height="20"> [cmg-divined](https://github.com/cmg-divined)

   Automatically swaps fully repaired Elytras with damaged ones for efficient XP farm repairs.

---

- ### [HDisabler](https://github.com/CherkaSSH/hdisabler) <br>
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[60].releaseDate&label=Latest%20Release&color=orange)](https://github.com/CherkaSSH/hdisabler/releases) ![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/CherkaSSH/hdisabler/total)<br>
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
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[61].releaseDate&label=Latest%20Release&color=orange)](https://github.com/CherkaSSH/CoordFollower-plugin/releases) ![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/CherkaSSH/CoordFollower-plugin/total)<br>
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
   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[62].releaseDate&label=Latest%20Release&color=orange)](https://github.com/CherkaSSH/rusher-chess-tui/releases) ![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/CherkaSSH/rusher-chess-tui/total)<br>
   **Creator**: <img src="https://github.com/CherkaSSH.png?size=20" width="20" height="20"> [CherkaSSH](https://github.com/CherkaSSH)

     Chess module for RusherHacks, powered by [ChessLib](https://github.com/bhlangonijr/chesslib).

---

- ### [ActivatedSpawnerDetector](https://github.com/un0x9/ActivatedSpawnerDetector) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[63].releaseDate&label=Latest%20Release&color=green)](https://github.com/un0x9/ActivatedSpawnerDetector/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/un0x9/ActivatedSpawnerDetector/total)](https://github.com/un0x9/ActivatedSpawnerDetector/releases/download/v1.2.2/ActivatedSpawnerDetector-1.2.2.jar)<br>

   **Creator**: <img src="https://github.com/un0x9.png?size=20" width="20" height="20"> [un0x9](https://github.com/un0x9)

   Detects activated spawners and provides visual feedback in RusherHacks.

---

- ### [Rusher Discord Notifications](https://github.com/kybe236/rusher-discord-notifications) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[64].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusher-discord-notifications/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/kybe236/rusher-discord-notifications/total)](https://github.com/kybe236/rusher-discord-notifications/releases/download/1.0.0/discord-notifier-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

   Sends notifications from RusherHacks to a Discord channel.

---

- ### [AutoBonemeal](https://github.com/John200410/rusherhack-autobonemeal) <br>

   [![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Frusherdevelopment.github.io%2Frusherhack-plugins%2Fbadges.json&query=%24.plugins[65].releaseDate&label=Latest%20Release&color=green)](https://github.com/John200410/rusherhack-autobonemeal/releases) [![GitHub Downloads (all releases)](https://img.shields.io/github/downloads/John200410/rusherhack-autobonemeal/total)](https://github.com/John200410/rusherhack-autobonemeal/releases/download/v1.0.0/auto-bonemeal-1.0.0.jar)<br>

   **Creator**: <img src="https://github.com/John200410.png?size=20" width="20" height="20"> [John200410](https://github.com/John200410)

   A RusherHacks plugin for automatically applying bonemeal to crops.


<!-- END PLUGINS LIST -->

## Reporting Issues

If you encounter issues with any of the plugins listed here, please contact the plugin's creator or open an issue in their respective repository. 

For issues related to the collection repository itself, such as incorrect plugin information, broken links, or formatting errors, please use the [Plugin Information Issue](https://github.com/RusherDevelopment/rusherhack-plugins/issues/new?assignees=&labels=&template=plugin-information-issue.md&title=%5BISSUE%5D) tracker.

## Contribute

If you have a RusherHack plugin you'd like to add to this list, please submit a pull request with the plugin details! For more detailed instructions on how to contribute, please see the [Contributing Guide](./CONTRIBUTING.md).
