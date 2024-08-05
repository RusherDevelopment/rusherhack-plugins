![RusherHacks Logo](https://raw.githubusercontent.com/RusherDevelopment/example-plugin/master/src/main/resources/exampleplugin/graphics/rh_head.png)

# RusherHacks Plugin Collection

[![Pinned Plugins](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=$.pinnedPlugins.message&label=Pinned%20Plugins&color=green)](#plugins-list)
[![Non-Pinned Plugins](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=$.nonPinnedPlugins.message&label=Non-Pinned%20Plugins&color=blue)](#non-pinned-plugins)
[![Discord RH plugins-dev](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=$.discord.label&label=Discord&color=7289DA&logo=discord)](https://discord.com/channels/590970327870341143/1166486609479356516)
[![RusherHacks v2.0.5](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgarlicrot.github.io%2FRusherHacks-Plugin-Collection%2Fbadges.json&query=$.rusherHacks.message&label=RusherHacks&color=blue&logoSvg=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOsAAADqCAYAAABDVrJwAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAnnSURBVHhe7d0xjx1XGcbxnRUkQUE4Ekj+AqvUqaCMBClooKKAzhJtOiLRuIGIloiI0kTuEBIVoqDhK7ijc0NppUIoQWEt38yxZq3rdx5rX58z98w8c/+/6E1GzsyZOTPz+Pgc390d3n/v6nDR2Te+OUxbfT297t7Vi48+/mTa2r9Hjx5NW/v39798Nm31czn9F8DGEVbABGEFTOTDehjne7GwP+WxxnLTow9l2aW2KjGyAiYIK2CCsAImCCtgIh/WYZwZx6rVYwFAKZccCy/bwz3q0Qf1DmerEiMrYIKwAiYIK2CCsAIm1glrjwUARU32l7yWJdvqQd2PrVvyemNbre1lVb4njKyACcIKmCCsgAnCCphYPqyVk+fVLLnIoNpS1aKlvXhcj2cVz1mqxZLXG9tqbS9L3ZPEdTCyAiYIK2CCsAImCCtgYvGwDuNkOdZM+bVYexUXDl6xeJDW0l7tcS3iOXud100iD4ysgAnCCpggrICJ4YPvv7vnGePqfvWbP0xbR9Qd38Fc7unTp9NWP7/99YfT1kLUcxDP6ztvvzFt9cPICpggrIAJwgqYIKyACcK6pOO/+L8pJbtf1s1fpB/XVmz52pQNXy9hBUwQVsAEYQVMEFbABGFd0lqLE7ULVi3Xq45VVXttmCGsgAnCCpggrIAJwgqYIKxZe1wkiX16nX6pY1WdE7XAtiDCCpggrIAJwgqYIKyACcKadcKFg9XEPu2lX2s58QIbYQVMEFbABGEFTBBWwARhPWcnXhDZFNVXVT1ULuwRVsAEYQVMEFbABGEFTAzfe+ed2fT2cJjPeOXce8jNyA/hx58Ph9PP5GUfLsV5n4nZveiXai/K3qNMW8+J30rVvZN9TZxX7ZMl+7Dw9SrpexeoZ39Qz14YRL8Oz6aNhWR6z8gKmCCsgAnCCpggrIAJucDUIrN4kF6cUJP45IJNZoHldWT6oBYJ6s+Y70P1fup+iLZkx5ILc2lhEbJQizipPijZaxPtqTOo1uR+LfckYGQFTBBWwARhBUwQVsBE0wJT7YJNy+S8ZYFFLmJVfpoqex1qwUIudrTspyTuibxedUqxmJRdOMm+I7XPOvscstehtPRVHqnai8eKfRhZAROEFTBBWAEThBUwkV5gapmgx98S0os66pzJxYPaBYsi01fZg4ZzSgv3f9Ze9joU8Ymjiw5f+piReX5F+jlsBCMrYIKwAiYIK2Bi+O6dO7M/4Ms/yS/45/umeVyD6rldEfZrmRfJY9Vvm+qrTqb/viR5jngtS96P5xr2E0fqawla+pA9Z/ZZK6oHmfOqczKyAiYIK2CCsAImCCtgQn8oQs3Ps195oSbjcT812Re/bbR8f+HsooA8Q6Zf2b4Laq/swoa855WWXjhR9yTbhzX6mm5fHCvvnBr6Kr+/sLo2RlbABGEFTBBWwARhBUws/m1d5KQ97pec2LcsgCjqBwxlv1Kk9lp+/+mn09YtVPPJ9Q/ls08+nrb6+de/P5+2jogFFtlV8U7I92v67wuZ963I7qck39e07PUFjKyACcIKmCCsgAnCCphYPKxlUSBWlNmnKFPuWFnq2PKDjmaVvZZhuLWaxIttbE46cfvy/pZfD9Vy72btDeMziyX2m/V9LL3f+D9iCfK9EaX2G//P/LwJjKyACcIKmCCsgAnCCphoCqtaKFB1cflylSl7rHHmPasy8Y6lyHOqEsqvxlLXEkstHHRRTp)](https://rusherhack.org/changelog.html)
<!-- TODO: Fix custom logo not showing up For RusherHacks-->


A list of RusherHacks plugins developed by various creators. This list is ordered from oldest to newest pinned messages in the plugins-dev channel.

## Table of Contents
- [Installation](#installation)
- [Plugins List](#plugins-list)
- [Non Pinned Plugins](#non-pinned-plugins)
- [Plugin Examples/Info](#plugin-examplesinfo)
- [Contribute](#contribute)

## Installation

**Warning:** DO NOT ENABLE PLUGINS IF YOU DO NOT KNOW WHAT YOU ARE DOING.

To enable plugins in RusherHacks:

1. **Enable Plugins**: Add the JVM flag `-Drusherhack.enablePlugins=true` to your RusherHacks startup options.

2. **Install Plugins**:
   - Download the desired plugin `.jar` files.
   - Place them in the `.minecraft/rusherhack/plugins/` directory. You may need to create this folder if it does not exist.

3. **Reload Plugins**: Use the `*reload` command within RusherHacks to reload plugins.

## Plugins List

<details>
  <summary>Show Plugins List</summary>

### [Example Plugin](https://github.com/RusherDevelopment/example-plugin)
**Creator**: <img src="https://github.com/RusherDevelopment.png?size=20" width="20" height="20"> [RusherDevelopment](https://github.com/RusherDevelopment)

A basic example plugin demonstrating the structure and capabilities of RusherHacks plugins.

---

### [2b2t.vc Rusherhack](https://github.com/rfresh2/2b2t.vc-rusherhack)
**Creator**: <img src="https://github.com/rfresh2.png?size=20" width="20" height="20"> [rfresh2](https://github.com/rfresh2)

A RusherHacks plugin designed for 2b2t.vc server use.

---

### [RusherHack Custom HUDElement](https://github.com/Aspect-404/RusherHack-CustomHUDElement)
**Creator**: <img src="https://github.com/Aspect-404.png?size=20" width="20" height="20"> [Aspect-404](https://github.com/Aspect-404)

Make a customizable text HUD element for Minecraft utility mod RusherHack.

---

### [Auto Anvil Rename](https://github.com/IceTank/AutoAnvilRename)
**Creator**: <img src="https://github.com/IceTank.png?size=20" width="20" height="20"> [IceTank](https://github.com/IceTank)

Automates the renaming process in anvils.

---

### [Queue Manager](https://github.com/GabiRP/QueueManager)
**Creator**: <img src="https://github.com/GabiRP.png?size=20" width="20" height="20"> [GabiRP](https://github.com/GabiRP)

Manages queue positions and notifies users of their status.

---

### [RusherHack Instance Info](https://github.com/John200410/rusherhack-instance-info)
**Creator**: <img src="https://github.com/John200410.png?size=20" width="20" height="20"> [John200410](https://github.com/John200410)

Provides detailed information about the current instance.

---

### [OP Plugin](https://github.com/theoplegends/op-plugin)
**Creator**: <img src="https://github.com/theoplegends.png?size=20" width="20" height="20"> [theoplegends](https://github.com/theoplegends)

*Current features as of 21 February 2024:<br>
Autopearl = aims downwards and throws a pearl so you can phase into blocks<br>
JakeOrganCrash = crash exploit that crashes jakeorgans server<br>
HoleEscape = escapes out of 1x1 holes or 2x1 holes<br>
PaperCrash = old paper server crash exploit try 2200-3000 levels<br>
TrapESP = wip<br>

---

### [Stash Mover Plugin](https://github.com/xyzbtw/StashMoverPlugin)
**Creator**: <img src="https://github.com/xyzbtw.png?size=20" width="20" height="20"> [xyzbtw](https://github.com/xyzbtw)

A plugin to move stashes using pearls.

---

### [Unified Module List](https://github.com/czho/unified-modulelist)
**Creator**: <img src="https://github.com/czho.png?size=20" width="20" height="20"> [czho](https://github.com/czho)

Rusherhack hudelement that shows active modules from both meteorclient and rusherhack.

---

### [Container Tweaks](https://github.com/rfresh2/ContainerTweaks-rusherhack)
**Creator**: <img src="https://github.com/rfresh2.png?size=20" width="20" height="20"> [rfresh2](https://github.com/rfresh2)

Simple tweaks for quickly moving items in containers.

---

### [RusherHack Spotify Integration](https://github.com/John200410/rusherhack-spotify/releases)
**Creator**: <img src="https://github.com/John200410.png?size=20" width="20" height="20"> [John200410](https://github.com/John200410)

Integrates Spotify music playback controls and status into the RusherHacks client.

---

### [Vanilla Elytra Flight](https://github.com/FBanna/Rusherhack-Vanilla-Efly)
**Creator**: <img src="https://github.com/FBanna.png?size=20" width="20" height="20"> [FBanna](https://github.com/FBanna)

Highly customizable rusher hack efly plugin.

---

### [RusherGUI](https://github.com/xyzbtw/rusherGUI)
**Creator**: <img src="https://github.com/xyzbtw.png?size=20" width="20" height="20"> [xyzbtw](https://github.com/xyzbtw)

Rusherhack GUI example plugin.

---

### [Rusherhack BookBot](https://github.com/Aspect-404/Rusherhack-BookBot)
**Creator**: <img src="https://github.com/Aspect-404.png?size=20" width="20" height="20"> [Aspect-404](https://github.com/Aspect-404)

Rusherhack plugin for bookbot.

---

### [Shay's RusherTweaks](https://github.com/ShayBox/ShaysRusherTweaks)
**Creator**: <img src="https://github.com/ShayBox.png?size=20" width="20" height="20"> [ShayBox](https://github.com/ShayBox)

A collection of small tweaks and improvements for the RusherHacks client.

---

### [Nuker](https://github.com/beanbag44/Nuker/)
**Creator**: <img src="https://github.com/beanbag44.png?size=20" width="20" height="20"> [beanbag44](https://github.com/beanbag44)

Epic nuker for nuking terrain.

---

### [Hold Rusher](https://github.com/cherosin/hold-rusher)
**Creator**: <img src="https://github.com/cherosin.png?size=20" width="20" height="20"> [cherosin](https://github.com/cherosin)

Adds a "Hold" flag for all modules, if active keybind will only be toggled while held.

---

### [No Walk Animation](https://github.com/Eonexe/NoWalkAnimation)
**Creator**: <img src="https://github.com/Eonexe.png?size=20" width="20" height="20"> [Eonexe](https://github.com/Eonexe)

Removes the walking animation.

---

### [NBT Utils](https://github.com/kybe236/rusherhack-nbt-utils)
**Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

Rusher nbt paste and copy.

---

### [Rusherhack Executer](https://github.com/kybe236/rusherhack-executer)
**Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

Executes commands and resolves `<player>` to every player online.

---

### [F3 Spoof](https://github.com/Doogie13/f3-spoof)
**Creator**: <img src="https://github.com/Doogie13.png?size=20" width="20" height="20"> [Doogie13](https://github.com/Doogie13)

Spoofs the F3 debug screen information.

---

### [Open Folder](https://github.com/kybe236/rusherhack-open-folder)
**Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

Opens the folder for the module with a button click.

---

### [Mace Kill](https://github.com/kybe236/rusherhack-mace-kill)
**Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

One shot pretty much all mobs with a mace.

---

### [Weather Changing Plugin](https://github.com/Lokfid/WeatherChangingPlugin)
**Creator**: <img src="https://github.com/Lokfid.png?size=20" width="20" height="20"> [Lokfid](https://github.com/Lokfid)

Allows players to change the weather in-game.

---

### [Middleclick Wind Charge](https://github.com/kybe236/rusherhack-middleclick-wind-charge)
**Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

Rusherhack middleclick windcharge plugin<br>
Allows you to throw windcharges with middle mouse button and also jump at the same time so you can boost jump.

---

### [GarlicSight](https://github.com/GarlicRot/GarlicSight)
**Creator**: <img src="https://github.com/GarlicRot.png?size=20" width="20" height="20"> [GarlicRot](https://github.com/GarlicRot)

A RusherHacks Plugin - Crosshair Info - GarlicSight.

---

### [LightningPop](https://github.com/GarlicRot/LightningPop)
**Creator**: <img src="https://github.com/GarlicRot.png?size=20" width="20" height="20"> [GarlicRot](https://github.com/GarlicRot)

A RusherHacks Plugin - Spawns Lightning On Totem Pops And Player Deaths - LightningPop.

---

### [AutoBucket](https://github.com/GarlicRot/AutoBucket)
**Creator**: <img src="https://github.com/GarlicRot.png?size=20" width="20" height="20"> [GarlicRot](https://github.com/GarlicRot)

A RusherHacks Plugin - Auto Bucket Entities - AutoBucket

---

</details>

## Non Pinned Plugins

<details>
  <summary>Show Non Pinned Plugins</summary>

### [NBT Viewer](https://github.com/Gentleman2292/NBT-viewer)
**Creator**: <img src="https://github.com/Gentleman2292.png?size=20" width="20" height="20"> [Gentleman2292](https://github.com/Gentleman2292)

A plugin to view NBT data in Minecraft.

---

### [Remote Control](https://github.com/kybe236/rusherhack-remote-controle)
**Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

A plugin for remote controlling RusherHacks.

---

### [Speed Measure](https://github.com/Lokfid/RusherHackSpeedMeasure)
**Creator**: <img src="https://github.com/Lokfid.png?size=20" width="20" height="20"> [Lokfid](https://github.com/Lokfid)

A plugin to measure speed in RusherHacks.

---

### [TNT Bomber](https://github.com/kybe236/rusher-tnt-bomber)
**Creator**: <img src="https://github.com/kybe236.png?size=20" width="20" height="20"> [kybe236](https://github.com/kybe236)

A plugin to automate TNT bombing in Minecraft.

---

### [No Render Entities](https://github.com/John200410/norender-entities)
**Creator**: <img src="https://github.com/John200410.png?size=20" width="20" height="20"> [John200410](https://github.com/John200410)

A plugin to disable rendering of entities.

---

### [RusherHack Messenger](https://github.com/Gentleman2292/rusherhack-messenger)
**Creator**: <img src="https://github.com/Gentleman2292.png?size=20" width="20" height="20"> [Gentleman2292](https://github.com/Gentleman2292)

A messaging plugin for RusherHacks.

---

</details>

## Plugin Examples/Info

Here are some helpful resources and examples for developing RusherHacks plugins:

- [Example Plugin](https://github.com/RusherDevelopment/example-plugin): A basic example plugin demonstrating the structure and capabilities of RusherHacks plugins.
- [RusherGUI](https://github.com/xyzbtw/rusherGUI): An example plugin showcasing a custom GUI integration with RusherHacks.
- [RusherHacks API Javadocs](https://rusherhack.org/api-javadocs/): The official API documentation for RusherHacks, providing detailed information on available classes, methods, and usage.

## Contribute

If you have a RusherHacks plugin you'd like to add to this list, please submit a pull request with the plugin details!
