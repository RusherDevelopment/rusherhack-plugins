![RusherHacks Logo](./Assets/RusherHacks/rh_head.png)

# RusherHacks Plugin Collection

[![Pinned Plugins](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=$.pinnedPlugins.message&label=Pinned%20Plugins&color=green)](#plugins-list)
[![Non-Pinned Plugins](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=$.nonPinnedPlugins.message&label=Non-Pinned%20Plugins&color=blue)](#non-pinned-plugins)
[![Discord RH plugins-dev](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=$.discord.label&label=Discord&color=7289DA&logo=discord)](https://discord.com/channels/590970327870341143/1166486609479356516)
[![RusherHacks v2.0.5](https://img.shields.io/badge/RusherHacks-v2.0.5-purple?logo=data:image/png;base64,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)](https://rusherhack.org/changelog.html)

A list of plugins developed by various creators. This list is ordered from oldest to newest pinned messages in the plugins-dev channel.

## Table of Contents

- [Installation](#installation)
- [Plugins List](#plugins-list)
- [Non-Pinned Plugins](#non-pinned-plugins)
- [Plugin Examples/Info](#plugin-examplesinfo)
- [Contribute](#contribute)

## Installation

> Warning: DO NOT ENABLE PLUGINS IF YOU DO NOT KNOW WHAT YOU ARE DOING.
>
> To enable plugins in RusherHacks:
>
> 1. **Enable Plugins**: Add the JVM flag `-Drusherhack.enablePlugins=true` to your RusherHacks startup options.
>
> 2. **Install Plugins**:
>
>    - Download the desired plugin `.jar` files.
>    - Place them in the `.minecraft/rusherhack/plugins/` directory. You may need to create this folder if it does not exist.
>
> 3. **Reload Plugins**: Use the `*reload` command within RusherHacks to reload plugins.
>
> — John200410 \*_RusherHacks Owner_

## Plugins List

<!-- START PLUGINS LIST -->
<details>
  <summary>Show Plugins List</summary>

---

### [Example Plugin](https://github.com/RusherDevelopment/example-plugin) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[0].releaseDate&label=Latest%20Release&color=orange)](https://github.com/RusherDevelopment/example-plugin/releases) <br>

**Creator**: <img src="https://github.com/RusherDevelopment.png?size=20" width="20" height="20"> [RusherDevelopment](https://github.com/RusherDevelopment)

A basic example plugin demonstrating the structure and capabilities of RusherHacks plugins.

---

### [2b2t.vc Rusherhack](https://github.com/rfresh2/2b2t.vc-rusherhack) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[1].releaseDate&label=Latest%20Release&color=green)](https://github.com/rfresh2/2b2t.vc-rusherhack/releases) <br>

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

### [RusherHack Custom HUDElement](https://github.com/Aspect-404/RusherHack-CustomHUDElement) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[2].releaseDate&label=Latest%20Release&color=green)](https://github.com/Aspect-404/RusherHack-CustomHUDElement/releases) <br>

**Creator**: <img src="https://github.com/Aspect-404.png?size=20" width="20" height="20"> [Aspect-404](https://github.com/Aspect-404)

Make a customizable text HUD element for Minecraft utility mod RusherHack.

<details>
  <summary>Show Screenshots</summary>
  <p align="center">
    <img src="./Assets/RusherHack-CustomHUDElement/HudSettings.png" alt="Hud Setting" border="0" width="250">
    <img src="./Assets/RusherHack-CustomHUDElement/HudElement.png" alt="Hud Element" border="0" width="550">
  </p>
</details>

---

### [Auto Anvil Rename](https://github.com/IceTank/AutoAnvilRename) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[3].releaseDate&label=Latest%20Release&color=green)](https://github.com/IceTank/AutoAnvilRename/releases) <br>

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

### [Queue Manager](https://github.com/GabiRP/QueueManager) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[4].releaseDate&label=Latest%20Release&color=green)](https://github.com/GabiRP/QueueManager/releases) <br>

**Creator**: <img src="https://github.com/GabiRP.png?size=20" width="20" height="20"> [GabiRP](https://github.com/GabiRP)

Manages queue positions and notifies users of their status.

---

### [RusherHack Instance Info](https://github.com/John200410/rusherhack-instance-info) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[5].releaseDate&label=Latest%20Release&color=green)](https://github.com/John200410/rusherhack-instance-info/releases) <br>

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

### [OP Plugin](https://github.com/theoplegends/op-plugin) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[6].releaseDate&label=Latest%20Release&color=green)](https://github.com/theoplegends/op-plugin/releases) <br>

**Creator**: <img src="https://github.com/theoplegends.png?size=20" width="20" height="20"> [theoplegends](https://github.com/theoplegends)

Current features: Autopearl, JakeOrganCrash, HoleEscape, PaperCrash, TrapESP.

---

### [Stash Mover Plugin](https://github.com/xyzbtw/StashMoverPlugin) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[7].releaseDate&label=Latest%20Release&color=green)](https://github.com/xyzbtw/StashMoverPlugin/releases) <br>

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

### [Unified Module List](https://github.com/czho/unified-modulelist) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[8].releaseDate&label=Latest%20Release&color=orange)](https://github.com/czho/unified-modulelist/releases) <br>

**Creator**: <img src="https://github.com/czho.png?size=20" width="20" height="20"> [czho](https://github.com/czho)

Rusherhack HUD element that shows active modules from both meteorclient and rusherhack.

---

### [Container Tweaks](https://github.com/rfresh2/ContainerTweaks-rusherhack) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[9].releaseDate&label=Latest%20Release&color=green)](https://github.com/rfresh2/ContainerTweaks-rusherhack/releases) <br>

**Creator**: <img src="https://github.com/rfresh2.png?size=20" width="20" height="20"> [rfresh2](https://github.com/rfresh2)

Simple tweaks for quickly moving items in containers.

<details>
  <summary>Show Screenshots</summary>
  <p align="center">
    <img src="./Assets/ContainerTweaks/ModuleSettings.png" alt="Module" border="0" width="250">
  </p>
</details>

---

### [RusherHack Spotify Integration](https://github.com/John200410/rusherhack-spotify) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[10].releaseDate&label=Latest%20Release&color=green)](https://github.com/John200410/rusherhack-spotify/releases) <br>

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

### [Vanilla Elytra Flight](https://github.com/FBanna/Rusherhack-Vanilla-Efly) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[11].releaseDate&label=Latest%20Release&color=green)](https://github.com/FBanna/Rusherhack-Vanilla-Efly/releases) <br>

**Creator**: <img src="https://github.com/FBanna.png?size=20" width="20" height="20"> [FBanna](https://github.com/FBanna)

Highly customizable rusher hack elytra flight plugin.

---

### [RusherGUI](https://github.com/xyzbtw/rusherGUI) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[12].releaseDate&label=Latest%20Release&color=green)](https://github.com/xyzbtw/rusherGUI/releases) <br>

**Creator**: <img src="https://github.com/xyzbtw.png?size=20" width="20" height="20"> [xyzbtw](https://github.com/xyzbtw)

Rusherhack GUI example plugin.

---

### [Rusherhack BookBot](https://github.com/Aspect-404/Rusherhack-BookBot) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[13].releaseDate&label=Latest%20Release&color=green)](https://github.com/Aspect-404/Rusherhack-BookBot/releases) <br>

**Creator**: <img src="https://github.com/Aspect-404.png?size=20" width="20" height="20"> [Aspect-404](https://github.com/Aspect-404)

Rusherhack plugin for bookbot.

---

### [Shay's RusherTweaks](https://github.com/ShayBox/ShaysRusherTweaks) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[14].releaseDate&label=Latest%20Release&color=green)](https://github.com/ShayBox/ShaysRusherTweaks/releases) <br>

**Creator**: <img src="https://github.com/ShayBox.png?size=20" width="20" height="20"> [ShayBox](https://github.com/ShayBox)

A collection of small tweaks and improvements for the RusherHacks client.

---

### [Nuker](https://github.com/beanbag44/Nuker) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[15].releaseDate&label=Latest%20Release&color=green)](https://github.com/beanbag44/Nuker/releases) <br>

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

### [Hold Rusher](https://github.com/cherosin/hold-rusher) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[16].releaseDate&label=Latest%20Release&color=green)](https://github.com/cherosin/hold-rusher/releases) <br>

**Creator**: <img src="https://github.com/cherosin.png?size=20" width="20" height="20"> [cherosin](https://github.com/cherosin)

Adds a "Hold" flag for all modules, if active keybind will only be toggled while held.

---

### [No Walk Animation](https://github.com/Eonexe/NoWalkAnimation) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[17].releaseDate&label=Latest%20Release&color=green)](https://github.com/Eonexe/NoWalkAnimation/releases) <br>

**Creator**: <img src="https://github.com/Eonexe.png?size=20" width="20" height="20"> [Eonexe](https://github.com/Eonexe)

Removes the walking animation.

---

### [NBT Utils](https://github.com/kybe236/rusherhack-nbt-utils) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[18].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-nbt-utils/releases) <br>

**Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

Rusher nbt paste and copy.

---

### [Rusherhack Executer](https://github.com/kybe236/rusherhack-executer) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[19].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-executer/releases) <br>

**Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

Executes commands and resolves `<player>` to every player online.

---

### [F3 Spoof](https://github.com/Doogie13/f3-spoof) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[20].releaseDate&label=Latest%20Release&color=orange)](https://github.com/Doogie13/f3-spoof/releases) <br>

**Creator**: <img src="https://github.com/Doogie13.png?size=20" width="20" height="20"> [Doogie13](https://github.com/Doogie13)

Spoofs the F3 debug screen information.

---

### [Open Folder](https://github.com/kybe236/rusherhack-open-folder) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[21].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-open-folder/releases) <br>

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

### [Mace Kill](https://github.com/kybe236/rusherhack-mace-kill) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[22].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-mace-kill/releases) <br>

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

### [Weather Changing Plugin](https://github.com/Lokfid/WeatherChangingPlugin) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[23].releaseDate&label=Latest%20Release&color=green)](https://github.com/Lokfid/WeatherChangingPlugin/releases) <br>

**Creator**: <img src="https://github.com/Lokfid.png?size=20" width="20" height="20"> [Lokfid](https://github.com/Lokfid)

Allows players to change the weather in-game.

---

### [Middleclick Wind Charge](https://github.com/kybe236/rusherhack-middleclick-wind-charge) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[24].releaseDate&label=Latest%20Release&color=green)](https://github.com/kybe236/rusherhack-middleclick-wind-charge/releases) <br>

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

### [GarlicSight](https://github.com/GarlicRot/GarlicSight) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[25].releaseDate&label=Latest%20Release&color=green)](https://github.com/GarlicRot/GarlicSight/releases) <br>

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

### [LightningPop](https://github.com/GarlicRot/LightningPop) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[26].releaseDate&label=Latest%20Release&color=green)](https://github.com/GarlicRot/LightningPop/releases) <br>

**Creator**: <img src="https://github.com/GarlicRot.png?size=20" width="20" height="20"> [GarlicRot](https://github.com/GarlicRot)

A RusherHacks Plugin - Spawns Lightning On Totem Pops And Player Deaths - LightningPop.

<details>
  <summary>Show Screenshots</summary>
  <p align="center">
    <img src="./Assets/LightningPop/Module.png" alt="Module" border="0" width="250">
  </p>
</details>

---

### [AutoBucket](https://github.com/GarlicRot/AutoBucket) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[27].releaseDate&label=Latest%20Release&color=green)](https://github.com/GarlicRot/AutoBucket/releases) <br>

**Creator**: <img src="https://github.com/GarlicRot.png?size=20" width="20" height="20"> [GarlicRot](https://github.com/GarlicRot)

A RusherHacks Plugin - Auto Bucket Entities - AutoBucket.

<details>
  <summary>Show Screenshots</summary>
  <p align="center">
    <img src="./Assets/AutoBucket/module.png" alt="Module" border="0" width="250">
  </p>
</details>

---

### [rusherNodusTheme](https://github.com/bakjedev/rusherNodusTheme) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[28].releaseDate&label=Latest%20Release&color=green)](https://github.com/bakjedev/rusherNodusTheme/releases) <br>

**Creator**: <img src="https://github.com/bakjedev.png?size=20" width="20" height="20"> [bakjedev](https://github.com/bakjedev)

Nodus - Best theme evaAAAA. code is terrible. blame xyzbtw!

<details>
  <summary>Show Screenshots</summary>
  <p align="center">
    <img src="./Assets/rusherNodusTheme/NodusGUI.png" alt="Module" border="0" width="750">
  </p>
</details>

---

### [nhack-theme](https://github.com/h1tm4nqq/Nhack-theme) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[29].releaseDate&label=Latest%20Release&color=yellow)](https://github.com/h1tm4nqq/Nhack-theme/releases) <br>

**Creator**: <img src="https://github.com/h1tm4nqq.png?size=20" width="20" height="20"> [h1tm4nqq](https://github.com/h1tm4nqq)

A theme like Nhack 2015 for rh

---

### [RusherHack-BoatExecute](https://github.com/PhilipPanda/RusherHack-BoatExecute) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[30].releaseDate&label=Latest%20Release&color=green)](https://github.com/PhilipPanda/RusherHack-BoatExecute/releases) <br>

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

<!-- END PLUGINS LIST -->
</details>

## Non-Pinned Plugins

<!-- START NON-PINNED PLUGINS LIST -->
<details>
  <summary>Show Plugins List</summary>

---

### [NBT Viewer](https://github.com/Gentleman2292/NBT-viewer) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[31].releaseDate&label=Latest%20Release&color=blue)](https://github.com/Gentleman2292/NBT-viewer/releases) <br>

**Creator**: <img src="https://github.com/Gentleman2292.png?size=20" width="20" height="20"> [Gentleman2292](https://github.com/Gentleman2292)

A plugin to view NBT data in Minecraft.

<details>
  <summary>Show Screenshots</summary>
  <p align="center">
    <img src="./Assets/NBT-viewer/NBT-viewer.png" alt="NBT-viewer" border="0" width="750">
  </p>
</details>

---

### [Remote Control](https://github.com/kybe236/rusherhack-remote-controle) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[32].releaseDate&label=Latest%20Release&color=blue)](https://github.com/kybe236/rusherhack-remote-controle/releases) <br>

**Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

A plugin for remote controlling RusherHacks.

---

### [Speed Measure](https://github.com/Lokfid/RusherHackSpeedMeasure) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[33].releaseDate&label=Latest%20Release&color=red&link=https://github.com/Lokfid/RusherHackSpeedMeasure/releases)](https://github.com/Lokfid/RusherHackSpeedMeasure/releases) <br>

**Creator**: <img src="https://github.com/Lokfid.png?size=20" width="20" height="20"> [Lokfid](https://github.com/Lokfid)

A plugin to measure speed in RusherHacks.

**Original Creator**: <img src="https://github.com/IceTank.png?size=20" width="20" height="20"> [IceTank](https://github.com/IceTank)

---

### [TNT Bomber](https://github.com/kybe236/rusher-tnt-bomber) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[34].releaseDate&label=Latest%20Release&color=blue)](https://github.com/kybe236/rusher-tnt-bomber/releases) <br>

**Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

A plugin to automate TNT bombing in Minecraft.

---

### [No Render Entities](https://github.com/John200410/norender-entities) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[35].releaseDate&label=Latest%20Release&color=blue)](https://github.com/John200410/norender-entities/releases) <br>

**Creator**: <img src="https://github.com/John200410.png?size=20" width="20" height="20"> [John200410](https://github.com/John200410)

A plugin to disable rendering of entities.

---

### [RusherHack Messenger](https://github.com/Gentleman2292/rusherhack-messenger) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[36].releaseDate&label=Latest%20Release&color=blue)](https://github.com/Gentleman2292/rusherhack-messenger/releases) <br>

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

### [RusherHack Instance Info (Fork)](https://github.com/GarlicRot/rusherhack-instance-info) <br>

[![Latest Release Date](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=%24.plugins[37].releaseDate&label=Latest%20Release&color=blue)](https://github.com/GarlicRot/rusherhack-instance-info/releases) <br>

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

<!-- END NON-PINNED PLUGINS LIST -->
</details>

## Plugin Examples/Info

Here are some helpful resources and examples for developing RusherHacks plugins:

- [Example Plugin](https://github.com/RusherDevelopment/example-plugin): A basic example plugin demonstrating the structure and capabilities of RusherHacks plugins.
- [RusherGUI](https://github.com/xyzbtw/rusherGUI): An example plugin showcasing a custom GUI integration with RusherHacks.
- [RusherHacks API Javadocs](https://rusherhack.org/api-javadocs/): The official API documentation for RusherHacks, provides detailed information on available classes, methods, and usage.

## Contribute

If you have a RusherHacks plugin you'd like to add to this list, please submit a pull request with the plugin details! For more detailed instructions on how to contribute, please see the [Contributing Guide](./CONTRIBUTING.md).
