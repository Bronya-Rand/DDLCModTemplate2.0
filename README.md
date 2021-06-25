# Welcome to the New Modification Club!

[![ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/K3K22K8SU)

The **new** DDLC Mod Template is a mod template for the **original** Doki Doki Literature Club by GanstaKingofSA that adheres to [Team Salvato's IP Guidelines](http://teamsalvato.com/ip-guidelines/) for fan mods. The last version the template was tested and working on Ren'Py <u>7.4.5</u>. 
> This mod template will not work for Doki Doki Literature Club Plus. Development of a mod template for Doki Doki Literature Club Plus will take some time to be done if it's possible to mod the game.

**The template is designed for Original DDLC fan games and mods that use DDLC assets. 
It is not meant for projects that does not use them, or as code to be copied to your non-DDLC project. 
Most code in this template are the IP of Team Salvato and may not be copied to non-DDLC fan projects or mods.**

> Android Support is only supported on Version **2.4.0** and higher. Refer to *guide.pdf* in the ZIP file for more information in those versions.

### Getting Started for Beginners (Ren'Py 6)
1. Download and run the [Ren'Py 6.99.12 SDK](https://www.renpy.org/release/6.99.12). 
    > DDLC does not work with newer Ren'Py versions unless it's upgraded. See **Getting Started for Advanced Users (Ren'Py 7)** for upgrading DDLC to Ren'Py 7.
2. Go to releases to download the [latest build](https://github.com/GanstaKingofSA/DDLCModTemplate2.0/releases) of the template.
3. Download DDLC from http://ddlc.moe or Steam & copy the *DDLC-1.1.1-pc* (`ddlc-mac` for <u>MacOS/OS X</u> or `Doki Doki Literature Club` for <u>Steam</u>) folder to the *renpy-6.99.12.4-sdk* folder. Rename the folder to your mod name.
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

### Getting Started For Android Porting/Modding
Refer to *guide.pdf* in your ZIP folder for more information, but make sure of these key points.
1. For Package Name in Ren'Py Launcher, use `com` with a period at the end, then <u>your name</u> with another period at the end, and the build name of your mod. 
    > For example, if your name is <u>Eileen</u> and your build name for your mod is `TheQuestion` in *options.rpy* (under `build.name`), it will be formatted like this: `com.eileen.thequestion`

More information about Android is listed in the Wiki or *guide.pdf*.

### Template Features
1. Build Packaging on Ren'Py 6 or 7!
2. Splash Screen when your mod is launched for the first time.
3. DDLC's exact RPY fiiles with explainations.
4. Customizable! Use this as a starting point for any ideas you wish to create.
5. MacOS/OS X and Linux `.app` and `.sh` support.
6. Full Android Support! Yes, everything DDLC (except `[currentuser]`) will work under Android.
    > Refer to *guide.pdf* for configuring your mod for Android.
7. Xcode Support! Open this project in Xcode and you can edit, build, and run your mod without opening the Ren'Py Launcher ever again! 
    > Note: You need to change your `RENPY_TOOL` location and the Ren'Py app location in the target scheme for Xcode. [Learn more &rsaquo;](XCODE.md)

### Added Features
1. Terra's In-Depth Poem Game Guide!
2. Xcode Support for Mac OS/OS X by Alicerunsonfedora!
3. NVL Support thanks to Yagamirai01!
4. Ren'Py 7 Mod Package Support!
5. MacOS/OS X `.app` Building Support for Mac Users!
6. Linux `.sh` Building Support for Linux Users!
7. Android Support for porting your mod or making a mod for PC and Android!

### Returned Features
1. Ghost Menu (Dan's Spooky Easter Egg)
2. Sayori Kill Script (If you delete Sayori before the game starts a new game, a new screen takes over)
3. Monika Kill Script (If you delete Monika after the game loads the main menu and start a new game, a new script plays out)
4. Special Poems! (Random Special Poems appear when prompted)
5. Poem Responses! (Doki's respond to your custom poems!)
and more!

This template is included with [DDMMaker](https://github.com/GanstaKingofSA/DDLC-ModMaker/releases), a Ren'Py SDK to build only DDLC mods.

Copyright © 2019-2021 GanstaKingofSA. All rights reserved. Doki Doki Literature Club, the Doki Doki Literature Club code, is the property of Team Salvato (Dan Salvato LLC). Copyright © 2017 Team Salvato. All rights reserved.
