## Doki Doki Mod Template 2.0

The **new** DDLC Mod Template is a mod template for Doki Doki Literature Club by Azariel Del Carmen (GanstaKingofSA) that adheres to [Team Salvato's IP Guidelines](http://teamsalvato.com/ip-guidelines/) for fan mods.
> This project is unafilliated with Team Salvato.

## Features
1. Build Packaging on Ren'Py 6 or 7!
2. Team Salvato Compliant Splash Screen.
3. DDLC's exact RPY files with explainations.
5. macOS `.app` and Linux support via `LinuxLauncher.sh`.
6. Android Support! Now you can make your mod work* on mobile phones and tablets!
    > \* - Only if your mod uses simple script code or DDLC functions. More complicated code may require some adjustments to get working. See *guide.pdf* or visit the DDMC Discord for help if you can't get your mod to run.
7. Xcode Support! Open this project in Xcode and you can edit, build, and run your mod without opening the Ren'Py Launcher ever again! 
    > Note: You need to change your `RENPY_TOOL` location and the Ren'Py app location in the target scheme for Xcode. [Learn more &rsaquo;](XCODE.md)
8. [BETA] Pronoun Support! Allow players to identify with what pronoun they go by!
    > See *pronoun_example.rpy* in the `game` folder for a example on how to use this feature.
9. Better Blue Screens of Death! Make your own BSOD easily in-game on every operating system! 
10. Uncensored Mode! Allow more sensitive content to be shown in-game.
11. Let's Play Mode (Streamer Mode)! A better alternative to hide streamer information and more!
12. Gallery Menu! Allow players to see the work you have done in-game and export it*!
    > \* - Exporting may be disabled or set to watermark only in the code.
13. Achievements Menu! Set up achievements in your mod for players to complete your mod in full!
14. Different Menu Button Colors! Have different colored buttons in the menu prompt to your hearts content.
15. Automatic GUI Coloring! Color the GUI in the game to whatever you like without editing the asset files themselves! 
16. Export your mod logo as a ICO file for your executables! (Windows Only)
17. Terra's in-depth Poem Game guide!
18. NVL Support thanks to Yagamirai01!
19. Patches for several Ren'Py releases and Windows features.

### Returned Features
1. Ghost Menu. (Dan's spooky easter egg)
2. Sayori Kill Script. (If you delete Sayori before the game starts, a new screen takes over)
3. Monika Kill Script. (If you delete Monika after the game loads, a new script plays out)
4. Special Poems! (The random poems in DDLC that appear in Act 2)
5. Poem Responses! (The Doki's respond to your poems!)

## Changes

Version 3.0.0 (<u>Android Supported</u> Mod Template)
**Note**: Starting from 3.0.0, you may only use the DDLC Mod Template to create DDLC mods. You may not use it to make unofficial patches/fixes to DDLC.

- Achievements Menu! Set up achievements in your mod and notify the user of a unlocked achievement in-game!
- Gallery Menu! Showcase the art in your mod outside of the mod's story for players to see.
    > Players can export only backgrounds from the mod to use for a PC background. If you wish to not have this, remove the `E` textbutton in *gallery.rpy*
- Different Menu Button Colors! Have different colored buttons in the menu prompt to your hearts content.
    > Examples on how to use this are in *screens.rpy*
- Automatic GUI Coloring! Color the GUI in the game to whatever you like without editing the asset files themselves!
    > Examples and code to use this feature are in *splash.rpy* and *screens.rpy* respectively.
- Export your mod logo as a ICO file for your executables! (Windows Only)
- Uncensored Mode! Allow adult/sensitive content to players that wish to see the following content.
    > To hide uncensored details, refer to this example
```py
    if persistent.uncensored_mode:
        m "Uncensored Content"
    else:
        m "Censored Content"
```
- Let's Play Mode (Streamer Mode)! Protect dokitubers, streamers and more from having their information leaked (names, etc.) in-game!
    > To hide player info details, refer to this example
```py
    if persistent.lets_play:
        m "Hi MC!"
    else:
        m "Hi John!"
```

- Made a Linux/MacOS SH Launcher (*LinuxLauncher.sh*) to fix the `future.standard_library` issue that occurs from installing a Ren'Py 7 mod over DDLC.
- Fixed a bug where the poemgame under Ren'Py 6 will error out due to different syntax requirements.
- Patched the long causing Ren'Py 7.4.6-7.4.8 transform bug where several characters may not appear or transitions are broken in script.
- Patched the Ren'Py 7.4.9 menu animation bug where the menu polka-dots would reset themselves each time a menu button was clicked.

- Removed the *scripts.rpa* requirement from splash.rpy due to `defined twice` errors.
- Fixed process listing due to `wmic`'s depreciation in Windows 10 and 11 builds > 22000 and for MacOS/Linux support.
- Fixed Better BSODs due to `wmic`'s depreciation in Windows 10 and 11 builds > 22000.
- Updated template comments.
