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
20. [Python 3] Discord RPC support

### Returned Features
1. Ghost Menu. (Dan's spooky easter egg)
2. Sayori Kill Script. (If you delete Sayori before the game starts, a new screen takes over)
3. Monika Kill Script. (If you delete Monika after the game loads, a new script plays out)
4. Special Poems! (The random poems in DDLC that appear in Act 2)
5. Poem Responses! (The Doki's respond to your poems!)

## Changes

Version 4.0.2
- Fixed a bug where LinuxLauncher.sh crashes if a screenshot file is present.
- [Python 3] Fixed a bug in effects.rpy due to Python 3 division.
- [Python 2] Fixed a bug with the process list on Mac/Linux.
- Fixed a possible line bug due to Composite vs im.Composite.
- [Python 3] Added a try except for Discord RPC if Discord is not present.
- Bump Lockdown to 8.0.3/7.5.3.

