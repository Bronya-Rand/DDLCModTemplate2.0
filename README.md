# Welcome to the New Modification Club!

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/K3K22K8SU)

The **new** DDLC Mod Template is a mod template for Doki Doki Literature Club by GanstaKingofSA that adheres to [Team Salvato's IP Guidelines](http://teamsalvato.com/ip-guidelines/) for fan mods.

**The DDLC Mod Template is meant for DDLC fan games and mods that use DDLC assets. 
It is not meant for projects that does not use them, or as code to be copied to your non-DDLC project. 
Most code in this template are the IP of Team Salvato and may not be copied to non-DDLC fan projects or mods.**

> For a tutorial, download the packaged tutorial `DDLCModTemplate-2.X.X-Tutorial.zip` under **[Releases](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/releases)**. Only available after version **2.3.0** and tutorial builds may have a delay of being released after the version has come out.

### Getting Started for Beginners (Ren'Py 6)

1. Download and run the [Ren'Py 6.99.12 SDK](https://www.renpy.org/release/6.99.12). **(NOTE: DDLC does not work with newer Ren'Py versions unless upgraded, see below.)**
2. Go to releases to download the [latest build](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/releases) of the template.
3. Place the files inside a folder (preferrably your mod name or `game`) where you extracted Ren'Py to inside of `renpy-6.99.12.4-sdk`.
4. Download the DDLC files, available for free at http://ddlc.moe or Steam & paste `audio.rpa`, `images.rpa`, `fonts.rpa`, and `scripts.rpa` inside the ZIP under DDLC-1.1.1-pc/game or Doki Doki Literature Club/game (Steam) into the /game directory of where you made your template folder.
5. Launch the project in Ren'Py. It should launch the game.
6. Once you finished writing your script, navigate the Ren'Py menu & select "Build Distributions." Uncheck all and check "Ren'Py 6 DDLC Compliant Mod" and build the mod. This will create a cross-platform .ZIP file with files for your mod.

### Getting Started for Advanced Users (Ren'Py 7)
Follow these steps to set up the template for Ren'Py 7.

1. Download and run the [Ren'Py 7.3.5 SDK](https://www.renpy.org/release/7.3.5) **(NOTE: Any files built in this version is incompatible with Ren'Py 6)**
2. Go to releases to download the [latest build](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/releases) of the template.
3. Place the files inside a folder (preferrably your mod name or `game`) where you extracted Ren'Py to inside of `renpy-7.3.5-sdk`.
4. Download the DDLC files, available for free at http://ddlc.moe or Steam & paste `audio.rpa`, `images.rpa`, `fonts.rpa`, and `scripts.rpa` inside the ZIP under DDLC-1.1.1-pc/game or Doki Doki Literature Club/game (Steam) into the /game directory of where you made your template folder.
5. Launch the project in Ren'Py. It should launch the game.
6. Once you finished writing your script, navigate the Ren'Py menu & select "Build Distributions." Uncheck all and check "Ren'Py 7 DDLC Compliant Mod" and build the mod. This will create a cross-platform .ZIP file with files for your mod.

### Template Features
1. Build Packaging on Ren'Py 6 or 7!
2. Splash screen when your mod is launched for the first time with a pre-made mod disclaimer.
3. DDLC's exact RPY fiiles with explainations.
4. Customizable! Use this as a starting point for any ideas you wish to create.
5. MacOS/OS X and Linux `.app` and `.sh` support.
6. Xcode Support! Open this project in Xcode and you can edit, build, and run your mod without opening the Ren'Py Launcher ever again! 
> Note: You need to change your `RENPY_TOOL` location and the Ren'Py app location in the target scheme for Xcode. [Learn more &rsaquo;](XCODE.md)

### Added Features
1. Terra's In-Depth Poem Game Guide!
2. Xcode Support for Mac OS/OS X by Alicerunsonfedora!
3. NVL Support!
4. Ren'Py 7 Mod Package Support!
5. MacOS/OS X `.app` Building Support for Mac Users!
6. Linux `.sh` Building Support for Linux Users!

### Returned Features
1. Ghost Menu (Dan's Spooky Easter Egg)
2. Sayori Kill Script (If you delete Sayori before the game starts a new game, new screen takes over)
3. Monika Kill Script (If you delete Monika after the game loads the main menu and start a new game, a new script plays out)
4. Special Poems! (Random Special Poems appear when prompted)
5. Exact `splash.rpy` and `screens.rpy` from DDLC.
6. Poem Responses! (Doki's respond to your custom poems!)
and more!

This template is included with [DDMMaker](https://github.com/GanstaKingofSA/DDLC-ModMaker/releases), a Ren'Py SDK to build only DDLC mods.
