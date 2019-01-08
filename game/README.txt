## DDLC Mod Template 2.0

The '.rpy' files in the game folder are copies of important script files found in DDLC's `scripts.rpa` archive that are necessary to change for the most basic modding projects.

All '.rpy' here are exact replicas of the '.rpy' files included in DDLC but with story specific game flow removed. This will allow you to tell the story you want to tell instead.

## Explanation of scripts

#### `options.rpy`

This file contains options that can be changed to customize your game. This file also includes the build options used when exporting your game for others to download.

#### `script.rpy`

This is used to call scripts and set defaults to the game on startup. It should not include any actual events or scripting; only logic and calling other labels. **This is the place to start for building your mod.**

#### `splash.rpy`

This splash screen is the first thing that DDLC will show the player. It also defines a lot of the behavior when first loading the game, such as checking for character files and jumping to scenes currently in progress.
