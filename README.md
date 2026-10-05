# Welcome to the **New** Modification Club!

<p align="center">
  <img src=".github/IMAGES/ddlcmt-open-graph.png"/>
</p>

<p align="center">
   <a href="https://github.com/Bronya-Rand/DDLCModTemplate2.0/releases/latest">
      <img src=".github/IMAGES/download.png">
   </a>
</p>

## Table of Contents
- [Overview](#overview) 
- [Credit Requirements](#credit-requirements) 
- [Features](#features) 
- [Quick Start](#quick-start) 
- [Building & Distribution](#building--distribution)
- [Platform-Specific Notes](#platform-specific-notes)
- [Additional Resources](#additional-resources)
- [Credits](#credits)

## Overview

The DDLC Mod Template 2.0 is a comprehensive mod template for **Doki Doki Literature Club** by Azariel Del Carmen (bronya_rand) that fully adheres to [Team Salvato's IP Guidelines](http://teamsalvato.com/ip-guidelines/). 
Built for Ren'Py 8 (Ren'Py 8.0.0 - 8.5.4+), this template provides everything you need to create fan-made, cross-platform DDLC mods with modern features and optimized code.

> [!NOTE]
> **The DDLC Mod Template is not affiliated in any way with Team Salvato nor is it designed for "Doki Doki Literature Club Plus." Do not use the template nor its code for unofficial DDLC patches, fixes, etc.**

> [!NOTE] 
> For legacy Ren'Py support (Ren'Py 6.99.12 / Ren'Py 7.3.5 - 7.8.7), see the deprecated [Python 2](https://github.com/Bronya-Rand/DDLCModTemplate2.0/tree/python-2) branch of the mod template.

---

## Features

### Core Features

- **Team Salvato Compliant** - Includes required splashscreen (disclaimer), Android asset installation, and adheres to all IP guidelines for fan mods.
- **Python 3 & Ren'Py 8 Optimized** - Modern code for the latest Ren'Py.
- **Original DDLC Scripts Included** - Reference the original game scripts for learning purposes.
- **Cross-Platform Support** - Build for Windows, macOS, Linux, and Android.
- **Automatic GUI Coloring** - Customize GUI and menu button colors without editing assets.
- **Dynamic Super Resolution (DSR/DSP)** - Universal resolution template supporting custom resolutions.
- **Player Name Change** - Allow players to correct or change their name in-game.
- **Enhanced Console & Poem Responses** - Improved Monika console and cleaner poem response system.

### Gameplay Features

- **Uncensored Mode** - Option to show more sensitive content.
- **Let's Play Mode** - Protect personal information while streaming/recording.
- **NVL Support** - Full NVL (novel-style) dialogue support thanks to Yagamirai01.

### Returned DDLC Features

Classic DDLC features restored and improved:
- **Ghost Menu** - Dan's spooky easter egg.
- **Character Kill Scripts** - Sayori and Monika deletion scripts.
- **Special Poems** - Act 2 random poems _(now improved!)_.

### Optional Extras

> [!IMPORTANT]
> Download `DDLCModTemplate-X.X.X-Extras.zip` to access these optional features.

- **Better Blue Screens of Death** - Create custom BSODs on all platforms.
- **Gallery System** - Showcase your artwork and CGs.
- **[BETA] Discord Rich Presence** - Show mod activity on Discord.

---

## Quick Start
> [!NOTE]
> Before considering using Android assets/code in your mod, keep in mind that there is no "official" Android APK. Players will have a hard time finding a DDLC APK file from a trusted source unlike the PC version of the game. Consider whether you *really* need Android-specific features such as 1080p assets, fake captchas, virtual desktop, etc or if you can just use PC assets instead in your mod.

### Prerequisites
1. **[Ren'Py 8.X](https://www.renpy.org/latest.html)** 
2. **[DDLC (PC Version)](https://ddlc.moe/)** *(required)*
   > If you plan to use code/assets from the Android port of DDLC, you will need a copy of the Android DDLC APK as well as the PC version of DDLC.
3. **DDLC Android APK/XAPK** *(optional)*
   > Only required if your mod uses code or assets from the Android port of DDLC.
   > The PC version is **always** required, even if you only target Android.
3. **[This DDLC Mod Template](https://github.com/Bronya-Rand/DDLCModTemplate2.0/releases)**

### Installation Steps

1. **Extract Ren'Py** to a folder of your choice.
> [!WARNING]
> Do not extract Ren'Py to a cloud storage folder (e.g. Google Drive, OneDrive, etc.) as it will cause issues when testing your mod.

2. **Create a new folder** in the `renpy-8.X.X-sdk` folder and extract the DDLC Mod Template ZIP into it.

3. **Add the DDLC PC assets** *(required for all mods)*

   Open `ddlc-win.zip` and copy these RPA files into the mod template's `game` folder:
   - `audio.rpa`
   - `fonts.rpa`
   - `images.rpa`

   > [!IMPORTANT]
   > If these are missing, the template will fail to start with a `DDLCRPAsMissing` error. This applies to Android-targeted mods too.

4. **Add the DDLC Android assets** *(optional)*

   > Skip this step unless your mod uses Android-specific code or assets.

   Open the DDLC APK (or the nested `ff1.apk` inside an XAPK) and extract these folders from `assets/game` into the mod template's `game` folder:
   - `images`
   - `gui`
   - `fonts`
   - `bgm`
   - `sfx`

   > [!NOTE]
   > Don't copy any `.rpy` or `.rpyc` files from the APK. They duplicate labels already in the template and are not compatible with the template. They **will** cause errors.

5. **Launch the template**
   - Open the Ren'Py Launcher.
   - Select the DDLC Mod Template project.
   - Click _Launch Project_ to test it.

🎉 You're ready to start modding!

---

## Building & Distribution

When you're ready to release your mod:

### PC, macOS, and Linux

1. Open the **Ren'Py Launcher**.
2. Click on **Build Distributions**.
3. Under `Build Packages`, **uncheck everything** except **Ren'Py 8 DDLC Compliant Mod**.
4. Click **Build**.

This creates a cross-platform mod package ZIP file (marked with `-Renpy8-DDLCMod` in the filename) containing your mod files ready for distribution.

### Android

1. Open the **Ren'Py Launcher**.
2. Click on **Android**. The first time, this downloads RAPT (Ren'Py Android Packaging Tools). Once it finishes, click **Android** again.
4. Click on **Install SDK** to install the Android SDK (this may take a while).
5. Click on **Generate Keys** to generate a new Android Keystore.
5. Click **Configure** to set up your mod's Android configuration.
6. When prompted to select an app store, choose **Neither**.
7. Click **Build Package**.

> [!NOTE]
> Choose *Neither* because Team Salvato's IP Guidelines disallow mods on Google Play and the Amazon Appstore.

> [!TIP]
> If Gradle runs out of memory during the build, allocate more RAM in the configuration step. 3 GB is usually enough, but large mods may need more.

This creates an APK containing **only** your mod files. DDLC's assets are not included. Players supply them on first launch:

1. Install your mod's APK.
2. Obtain DDLC (see the table below).
3. Launch the mod and choose **PC** or **Android** on the setup screen.
4. Select the DDLC file. The mod extracts the assets and restarts automatically.

This only needs to be done once.

#### Which DDLC should players get?

| Your mod... | Tell players to get | They choose |
|---|---|---|
| Uses **no** Android-specific assets | DDLC PC version (`ddlc-win.zip`) | **PC** |
| Uses Android-specific assets | DDLC Android APK/XAPK | **Android** |

> [!WARNING]
> Always state which version players need in your mod's release notes. If your mod requires Android assets and a player extracts the PC version instead, the mod will fail to start on Android.

> [!TIP]
> Always test your mod thoroughly before building and distributing!

---

## Platform-Specific Notes

### Linux

Linux users must run mods using the included launcher script (at least once):

```bash
./LinuxLauncher.sh
```

### macOS

macOS support is included out of the box. Build distributions include macOS packages automatically.

---

## Credit Requirements

> [!IMPORTANT]
> **You MUST credit this template in your mod.** By default, a credits screen is enabled in-game (either in the Extras screen or as a standalone button). You can use the default implementation or choose one of the alternatives below.

### Default Credit Text

Include this in your mod's credits screen and/or `credits.txt` file:

```
This mod was made possible by bronya_rand's DDLC Mod Template 2.0: https://github.com/Bronya-Rand/DDLCModTemplate2.0
```

### Alternative Credit Methods

If you prefer a different approach, you may use one of these alternatives:

1. **Custom Splash Screen** - Feature the Team Salvato logo alongside a Bronya Rand logo ([available here](.github/IMAGES/Logos/)).
2. **Disclaimer Mention** - Add a line to your game's disclaimer: "This mod was made possible using bronya_rand's mod template".
3. **Presplash Screen** - Include a Bronya Rand logo ([available here](.github/IMAGES/Logos)) in your presplash.
4. **Custom Idea** - Contact me via Discord or Reddit with your proposed credit method for approval.

---

## Additional Resources

### Documentation

- 🎮 [Discord RPC Guide](./Documentation/Discord%20RPC%20Guide.pdf) - Set up Discord Rich Presence
- 📝 [New Poem Game Guide](./Documentation/New%20Poemgame%20Guide.pdf) - In-depth poem game documentation

### Community & Support

- 💬 **DDMC Discord** - Get help and share your mods with the community
- 🐛 **Issues** - Report bugs on [GitHub Issues](https://github.com/Bronya-Rand/DDLCModTemplate2.0/issues)
- ☕ **Support Development** - [Buy me a Ko-fi](https://ko-fi.com/K3K22K8SU)

---

## Credits

Thanks to the following people for their contributions to the DDLC Mod Template:

> [!NOTE]
> This list goes from the past to present.

- Dan Salvato (DDLC)
- renpytom (Ren'Py)
- MAS Team (template base before revamping)
- alicerunsonfedora (Xcode)
- Terra (In-depth poem game)
- Yagamirai01 (NVL)
- Alexxonder (Auto Color Adjustments)
- Elckarow (Python 3 updates, New poem responses/effects)
- NekoLaiS (Cryllic compatibility)
- The DDMC Community (Feature suggestions and feedback)
- Pseurae (Donation/Act 3 GL2 Fix)
- Lezalith (New Console (4.1.1+))
- RS/6000 (New Mod Template Logo (4.2.1+))
- Tulkas (Android Gestures)
- FiT (Weiss Chibi Branding Icon Design)
- Retronika (Supplemental code for the Gallery system)

---

<p align="center">
   <b>Copyright © 2019-2026 Azariel "Bronya Rand" Del Carmen (bronya_rand). All rights reserved. Doki Doki Literature Club, the Doki Doki Literature Club code, is the property of Team Salvato. Copyright © 2017 Team Salvato. All rights reserved.</b>
</p>
