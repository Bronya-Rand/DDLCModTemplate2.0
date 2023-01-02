## Copyright 2019-2023 Azariel Del Carmen (GanstaKingofSA). All rights reserved.

# bsod.rpy
# This file contains the screen code to display a fake Blue Screen of death.

## BSOD screen ##################################################################\
##
## This screen is used to fake a BSOD/kernel panic on the players' computer 
## on all platforms (Mobile devices defaults to the Linux BSOD).
##
## Syntax:
##     bsodCode - The error code message you want to show the player. Defaults to 
##                DDLC_ESCAPE_PLAN_FAILED if no message is given.
##     bsodFile (Windows 7 Only) - The fake file name that caused the 
##                error. Defaults to libGLESv2.dll if no file name is given.
##     rsod (Windows 11 Only) - Swaps the Windows 11 BSOD with a RSOD.
##
## Examples:
##     show screen bsod("DOKI_DOKI", "renpy32.dll", False) 
##     show screen bsod("EILEEN_EXCEPTION_NOT_HANDLED", rsod=True) 

init python:
    cursor = 0

    def fakePercent(st, at, winver):

        if int(0 + (st * 5)) < 100:
            percent = int(0 + (st * 5))
        else:
            percent = 100

        if winver == 8:
            d = Text("we'll restart for you. (" + str(percent) + "% complete)\n", style="bsod_win8_text", size=28)
        else:
            d = Text(str(percent) + "% complete", style="bsod_win10_text", line_leading=20)

        if percent < 100:
            return d, renpy.random.randint(1, 3)
        else:
            return d, None

    def constantCursor(st, at):
        global cursor
        if cursor == 0:
            cursor = 1
            return Text("  _", style="bsod_linux_text"), 0.3
        else:
            cursor = 0
            return Text("   ", style="bsod_linux_text"), 0.3

    if renpy.windows:
        try: osVer = tuple(map(int, subprocess.run("powershell (Get-WmiObject -class Win32_OperatingSystem).Version", check=True, shell=True, stdout=subprocess.PIPE).stdout.split(b"."))) # Vista+
        except: osVer = tuple(map(int, platform.version().split("."))) or (5, 1, 2600) # XP returns JIC (but Ren'Py 8 doesn't even support XP...)

screen bsod(bsodCode="DDLC_ESCAPE_PLAN_FAILED", bsodFile="libGLESv2.dll", rsod=False):

    layer "master"

    if renpy.windows:

        if osVer < (6, 2, 9200): # Windows 7
            
            add Solid("#000082")

            vbox:

                style_prefix "bsod_win7"

                text "A problem has been detected and Windows has been shut down to prevent damage to your computer."
                text "The problem seems to be caused by the following file: " + bsodFile.upper()
                text bsodCode.upper()
                text "If this is the first time you've seen this Stop error screen, restart your computer. If this screens appears again, follow these steps:"
                text "Check to make sure any new hardware or software is properly installed. If this is a new installation, ask your hardware or software manufacturer for any Windows updates you might need."
                text "If problems continue, disable or remove any newly installed hardware or software. Disable BIOS memory options such as caching or shadowing. If you need to use Safe Mode to remove or disable components, restart your computer, press F8 to select Advanced Startup Options, and then select Safe Mode."
                text "Technical information:"
                text "*** STOP: 0x00000051 (OXFD69420, 0x00000005, OXFBF92317" + ", 0x00000000)\n"
                text "*** " + bsodFile.upper() + "  -  Address FBF92317 base at FBF102721, Datestamp 3d6dd67c"

        elif osVer < (10, 0, 10240): # Windows 8/8.1
            
            add Solid("#1273aa")

            style_prefix "bsod_win8"

            vbox:

                xalign 0.5
                yalign 0.4

                text ":(" style "bsod_win8_sad_text"
                text "Your PC ran into a problem and needs to restart."
                text "We're just collecting some error info, and then"
                add DynamicDisplayable(fakePercent, 8)
                text "If you'd like to know more, you can search online later for this error: " + bsodCode.upper() style "bsod_win8_sub_text"

        else: # Windows 10, 11 and RSOD
            
            # After a silent update, Windows 11 now returns to a
            # Windows 10 BSOD color. We will remove the black for
            # blue now.
            if rsod:
                
                add Solid("#d40e0eff")
                python:
                    blackCol = "#f00"

            else:

                add Solid("#0078d7")
                python:
                    blackCol = "#0078d7"

            style_prefix "bsod_win10"

            vbox:

                xalign 0.2
                yalign 0.4

                text ":(" style "bsod_win10_sad_text"

                if osVer < (10, 0, 22000):
                    python:
                        bsodQRSize = 100

                    text "Your PC ran into a problem and needs to restart. We're"
                    text "just collecting some error info, and then we'll restart for"
                    text "you."

                else:
                    python:
                        bsodQRSize = 150

                    text "Your device ran into a problem and needs to restart."
                    text "We're just collecting some error info, and then we'll"
                    text "restart for you."

                add DynamicDisplayable(fakePercent, 10)

                hbox:
                    vbox:
                        text "" line_leading -3
                        add im.MatrixColor("mod_assets/mod_extra_images/bsod_qr_code.png", im.matrix.colorize(blackCol, "#fff"), ) at bsod_qrcode(bsodQRSize)
                    vbox:
                        xpos 0.04
                        vbox:
                            spacing 2
                            text "For more information about this issue and possible fixes, visit" style "bsod_win10_info_text" line_leading 30
                            text "https://www.windows.com/stopcode\n" style "bsod_win10_info_text"
                        null height 3
                        vbox:
                            spacing 4
                            text "If you call a support person, give them this info:" style "bsod_win10_sub_text"
                            text "Stop code: " + bsodCode.upper() style "bsod_win10_sub_text"
                            text "What failed: " + bsodFile.lower() style "bsod_win10_sub_text"
        
    elif renpy.macintosh:

        add Solid("#222")

        add im.MatrixColor("mod_assets/DDLCModTemplateLogo.png", im.matrix.desaturate() * im.matrix.brightness(-0.36)) at bsod_qrcode(440) xalign 0.5 yalign 0.54
        vbox:

            style_prefix "bsod_mac"
            xalign 0.53
            yalign 0.51

            text "You need to restart your computer. Hold down the Power\n"
            text "button until it turns off, then press the Power button again." line_spacing 25
            text "Redémarrez l'ordinateur. Enfoncez le bouton de démarrage\n"
            text "jusqu'à l'extinction, puis appuyez dessus une nouvelle fois." line_spacing 25
            text "Debe reiniciar el o rdenador. Mantenga pulsado el botón de\n"
            text "arranque hasta que se apague y luego vuelva a pulsarlo." line_spacing 25
            text "Sie müssen den Computer neu starten. Halten Sie den\n"
            text "Ein-/Ausschalter gedrückt bis das Gerät ausgeschaltet ist\n"
            text "und drücken Sie ihn dann erneut." line_spacing 25
            text "Devi riavviare il computer. Tieni premuto il pulsante di\n"
            text "accensione finché non si spegne, quindi premi di nuovo il\n"
            text "pulsante di accensione."

    else:

        add Solid("#000")

        vbox:
            style_prefix "bsod_linux"

            text "metaverse-pci.c:v[config.version] 5/22/2023 Metaverse Enterprise Solutions\n"
            text "  https://www.metaverse-enterprise.com/network/metaverse-pci.html"
            text "hd0: METAVERSE ENTERPRISE VIRTUAL HARDDISK, ATA DISK drive"
            text "sda0 at 0x1f0 - 0x1f7, 0x3f6 on irq 14"
            text "hdc: METAVERSE ENTERPRISE VIRTUAL CD-ROM, ATAPI CD/DVD-ROM drive"
            text "sr0 at 0x444 - 0x910, 0x211 on irq 15"
            text "fd0: METAVERSE ENTERPRISE VIRTUAL FLOPPY, ATA FLOPPY drive"
            text "ide2 at 0x7363-0x6e6565, 0x4569 on irq 16"
            text "ACPI: PCI Interrupt Link [[LNKC] ebabked at IRQ 10"
            text "ACPI: PCI Interrupt 0000:00:03:.0[[A] -> Link [[LNKC] -> GSI 10 (level, low) -> IRQ 10"
            text "eno1: Metaverse Enterprise LIB-0922 found at 0xc453, IRQ 10, 09:10:21:86:75:30"
            text "sda: max request size: 4MiB"
            text "sda: 2147483648 sectors (1 TB) w/256KiB Cache, CHS=178/255/63, (U)DMA"
            text "sda: sda1"
            text "sr0: ATAPI 16x CD-ROM drive, 2MB Cache, (U)DMA"
            text "Uniform CD-ROM driver Revision: [renpy.version_tuple]"
            text "Done."
            text "Begin: DDLC.so"
            text "Done."
            text "DDLC.so[[3352]: Faled to initialize steam: FileNotFoundError(\"Could not find module '/usr/app/ddlc/lib/py3-linux-x86_64/steam_api64.so') (or one of its dependencies). Try using the full path with constructor syntax.\")"
            text "DDLC.so[[3352]: nvdrs: Loaded, about to disable thread optimizations."
            text "DDLC.so[[3352]: nvdrs: Disabled thread optimizations."
            text "DDLC.so: SUCCESS."
            text "Done."
            text "Begin: DDLC.so -> linux-5.18"
            text "/init: /init: 151: " + bsodCode.upper() + ": 0xforce=panic"
            text "Kernel panic - not syncing: Attempted to kill init!"
            add DynamicDisplayable(constantCursor)

    add Solid("#000000") at bsod_transition

style bsod_win7_text is gui_text
style bsod_win7_text:
    font "C:/Windows/Fonts/lucon.ttf"
    antialias False
    size 13
    line_leading 15
    line_spacing -14
    xsize 1279
    outlines []

style bsod_win8_text is gui_text
style bsod_win8_text:
    font "C:/Windows/Fonts/segoeuil.ttf"
    size 25
    line_spacing 5
    xsize 600
    outlines []

style bsod_win8_sad_text is gui_text
style bsod_win8_sad_text is bsod_win8_text:
    size 128
    xpos -8

style bsod_win8_sub_text is gui_text
style bsod_win8_sub_text is bsod_win8_text:
    size 11

style bsod_win10_text is bsod_win8_text
style bsod_win10_text:
    font "C:/Windows/Fonts/segoeuil.ttf"
    size 28
    line_leading 2
    line_spacing -2
    xsize 800
    outlines []

style bsod_win10_info_text is bsod_win10_text
style bsod_win10_info_text:
    size 13

style bsod_win10_sad_text is bsod_win10_text
style bsod_win10_sad_text:
    size 140
    xpos -8

style bsod_win10_sub_text is bsod_win10_text
style bsod_win10_sub_text:
    size 11

style bsod_mac_text is gui_text
style bsod_mac_text:
    font gui.default_font
    size 28
    outlines []
    line_spacing -30

style bsod_linux_text is gui_text
style bsod_linux_text:
    font "gui/font/F25_Bank_Printer.ttf"
    size 15
    outlines []
    line_leading 5
            
transform bsod_transition:
    "black"
    0.1
    yoffset 250
    0.1
    yoffset 500
    0.1
    yoffset 750

transform bsod_qrcode(x):
    xysize(x,x)