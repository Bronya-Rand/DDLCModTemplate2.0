# Welcome to the New Modification Club!

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/K3K22K8SU)

Latest Versions: [2.4.9 (Android Supported Template)](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/releases/2.4.9) | [2.3.1-u8 (Non-Android Supported Template)](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/releases/2.3.1-u8)

Supported on: Ren'Py <u>6.99.12.4</u>, <u>7.3.5 - 7.4.5</u> and <u>7.4.9 - 7.4.10</u>

The **new** DDLC Mod Template is a mod template for the **original** Doki Doki Literature Club by GanstaKingofSA that adheres to [Team Salvato's IP Guidelines](http://teamsalvato.com/ip-guidelines/) for fan mods.
> This mod template will not work for Doki Doki Literature Club Plus. It does not work on Ren'Py 7.4.6-7.4.7 due to a bug that breaks DDLC transforms heavily. For more information visit this Github issue [here](https://github.com/renpy/renpy/issues/2860).

**The template is designed for Original DDLC fan games and mods that use DDLC assets. 
It is not meant for projects that does not use them, or as code to be copied to your non-DDLC project. 
Most code in this template are the IP of Team Salvato and may not be copied to non-DDLC fan projects or mods.**

### Getting Started for Beginners (Ren'Py 6)
1. Download and run the [Ren'Py 6.99.12 SDK](https://www.renpy.org/release/6.99.12). 
    > DDLC does not work with newer Ren'Py versions unless it's upgraded. See **Getting Started for Advanced Users (Ren'Py 7)** for upgrading DDLC to Ren'Py 7.
2. Go to releases to download the [latest build](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/releases) of the template.
3. Download DDLC from [DDLC.moe](http://ddlc.moe) or Steam & copy the *DDLC-1.1.1-pc* (`ddlc-mac` for <u>MacOS/OS X</u> or `Doki Doki Literature Club` for <u>Steam</u>) folder to the *renpy-6.99.12.4-sdk* folder. Rename the folder to your mod name.
4. Place the files withing the Mod Template's ZIP file into the DDLC folder you copied to. Accept any replaces if prompted. 
    > For MacOS/OS X, right click on `DDLC.app` within the *ddlc-mac* folder and click <u>Show Package Contents</u> then place the files within `Contents/Resources/autorun`. Accept any replaces if prompted. 
5. Launch the project in Ren'Py. It should compile and launch the game.
    > Sometimes this may not do anything or say a error happened. Click *Launch Project* again, and it should boot up.
6. Once you finished writing your script, navigate the Ren'Py Menu, and select *Build Distributions*. Uncheck all the options and check only `Ren'Py 6 DDLC Compliant Mod` and click <u>Build</u>. This will create a cross-platform .ZIP file with files for your mod.

### Getting Started for Advanced Users (Ren'Py 7)
Follow these steps to set up the template for Ren'Py 7.

1. Download and run the [Ren'Py 7.4.5 SDK](https://www.renpy.org/release/7.4.5)
    > Any files built in this version will be incompatible with Ren'Py 6.
2. Go to releases to download the [latest build](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/releases) of the template.
3. Download DDLC from http://ddlc.moe or Steam & copy the *DDLC-1.1.1-pc* (`ddlc-mac` for <u>MacOS/OS X</u> or `Doki Doki Literature Club` for <u>Steam</u>) folder to the *renpy-7.4.5-sdk* folder. Rename the folder to your mod name.
4. Place the files withing the Mod Template's ZIP file into the DDLC folder you copied to. Accept any replaces if prompted. 
    > For MacOS/OS X, right click on `DDLC.app` within the *ddlc-mac* folder and click <u>Show Package Contents</u> then place the files within `Contents/Resources/autorun`. Accept any replaces if prompted. 
5. Launch the project in Ren'Py. It should compile and launch the game.
    > Sometimes this may not do anything or say a error happened. Click *Launch Project* again, and it should boot up.
6. Once you finished writing your script, navigate the Ren'Py Menu, and select *Build Distributions*. Uncheck all the options and check only `Ren'Py 7 DDLC Compliant Mod` and click <u>Build</u>. This will create a cross-platform .ZIP file with files for your mod.

### Template Features
1. Build Packaging on Ren'Py 6 or 7!
2. Splash Screen when your mod is launched for the first time.
3. DDLC's exact RPY fiiles with explainations.
4. Customizable! Use this as a starting point for any ideas you wish to create.
5. MacOS and Linux `.sh` support.
6. Xcode Support! Open this project in Xcode and you can edit, build, and run your mod without opening the Ren'Py Launcher ever again! 
    > Note: You need to change your `RENPY_TOOL` location and the Ren'Py app location in the target scheme for Xcode. [Learn more &rsaquo;](XCODE.md)
7. [BETA] Pronoun Support! Allow users to identify with what pronoun they go by!
    > This works best with `He/Him`, `She/Her`, and `They/Them` pronouns but this can be expanded on as much as you like. Make sure to call `finishPronouns()` in your script after a pronoun is selected! See *pronoun_example.rpy* for a example on how to use this feature.

### Added Features
1. Terra's In-Depth Poem Game Guide!
2. Xcode Support for Mac OS/OS X by Alicerunsonfedora!
3. NVL Support thanks to Yagamirai01!
4. Ren'Py 7 Mod Package Support!
5. MacOS/OS X Building Support for Mac Users!
6. Linux `.sh` Building Support for Linux Users!
7. Better Blue Screens of Death! Make your own BSOD easily in-game now than ever on every operating system! (even Mac and Linux!)

### Returned Features
1. Ghost Menu (Dan's Spooky Easter Egg)
2. Sayori Kill Script (If you delete Sayori before the game starts a new game, a new screen takes over)
3. Monika Kill Script (If you delete Monika after the game loads the main menu and start a new game, a new script plays out)
4. Special Poems! (Random Special Poems appear when prompted)
5. Poem Responses! (Doki's respond to your custom poems!)
and more!

This template is included with [DDMMaker](https://github.com/GanstaKingofSA/DDLC-ModMaker/releases), a Ren'Py SDK to build only DDLC mods.

Copyright © 2019-2021 GanstaKingofSA. All rights reserved. Doki Doki Literature Club, the Doki Doki Literature Club code, is the property of Team Salvato (Dan Salvato LLC). Copyright © 2017 Team Salvato. All rights reserved.
