## This template version is 3.0.0. When asked to provide the template version
## you are using, give them this version number. 
### DO NOT REMOVE OR CHANGE THE ABOVE COMMENT. ###

## options.rpy

# This file customizes what your mod is and and how it starts and builds!

# This controls what your mod is called.
define config.name = "DDLC Mod Template"

# This controls whether you want your mod name to show in the main menu.
# If your mod name is big, it is suggested to turn this off.
define gui.show_name = True

# This controls the version number of your mod.
define config.version = "3.0.0"

# This adds information about your mod in the About screen.
# DDLC does not have a 'About' screen so you can leave this blank.
define gui.about = _("")

# This control the name of your mod build when you package your mod
# in the Ren'Py Launcher or DDMM (Doki Doki Mod Maker).
# Note:
#   The build name is ASCII only so no numbers, spaces, or semicolons.
#   Example: Doki Doki Yuri Time to DokiDokiYuriTime
define build.name = "DDLCModTemplateTwo"

# This configures whether your mod has sound effects.
define config.has_sound = True

# This configures whether your mod has music.
define config.has_music = True

# This configures whether your mod has voices.
define config.has_voice = False

# This configures what music will play when you launch your mod and in the 
# main menu.
define config.main_menu_music = audio.t1

# These variables control the transition effects of DDLC when entering and exiting
# a menu.
#   config.enter_transition controls the effect seen when entering the game menu.
#   config.exit_transition controls the effect when returning to the game.
#   Dissolve(X) dissolves the menu or last screen by X seconds.
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)

# This controls the transition effect of DDLC after loading the game.
define config.after_load_transition = None

# This controls the transition effect when your mod has reached the end of its' story.
define config.end_game_transition = Dissolve(.5)

# This controls the textbox that the characters use to speak.
#   "auto" sets the textbox to hide during scenes and show when a character speaks
#   "show" sets the textbox to show at all times
#   "hide" only shows dialogue when a character speaks.
define config.window = "auto"

# This controls the transition effects of the textbox.
#   config.window_show_transition controls the effect when the textbox is shown.
#   config.window_hide_transition controls the effect when the textbox is hidden.
#   Dissolve(X) dissolves the menu or last screen by X seconds.
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# This sets the text speed of your mod.
default preferences.text_cps = 50

# This controls the auto-text forward speed of your mod.
default preferences.afm_time = 15

# This controls the audio level of your mod.
default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75

# This controls the save folder name of your mod.
# Finding your Saves:
#   Windows: %AppData%/RenPy/
#   macOS: $HOME/Library/RenPy/ (Un-hide the Library Folder)
#   Linux: $HOME/.renpy/
define config.save_directory = "DDLCModTemplateTwo"

# This controls the window logo of your mod.
define config.window_icon = "gui/window_icon.png"

# This controls whether your mod allows the player to skip dialogue.
define config.allow_skipping = True

# This controls whether your mod saves automatically.
define config.has_autosave = False

# This controls whether you mod saves automatically when quitting the game.
define config.autosave_on_quit = False

# This controls the number of slots auto-save can use for saving the game.
define config.autosave_slots = 0

# This controls whether the player can rollback to the previous dialogue in-game.
define config.rollback_enabled = config.developer

# These variables controls the layers placement of screens, images, and more. 
# It is highly recommended to leave these variables alone.
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]
define config.image_cache_size = 64
define config.predict_statements = 50
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"

init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)

    # This function saves your mods' logo as a ICO file for Windows building with 
    # a custom icon.
    def saveIco(filepath):
        import pygame_sdl2
        
        bmp = os.path.join(renpy.config.basedir, "icon.bmp").replace("\\", "/")
        ico = os.path.join(renpy.config.basedir, "icon.ico").replace("\\", "/")

        surf = pygame_sdl2.image.load(os.path.join(
                renpy.config.gamedir, filepath
                ).replace("\\", "/")
            )
        trans = pygame_sdl2.transform.scale(surf, (64, 64))
        pygame_sdl2.image.save(trans, bmp)

        if os.path.exists(ico):
            os.remove(ico)

        os.rename(os.path.join(renpy.config.basedir, "icon.bmp").replace("\\", "/"), 
            os.path.join(renpy.config.basedir, "icon.ico").replace("\\", "/"))
        
        renpy.show_screen("dialog", message="Exported your mod logo as a icon successfully.", ok_action=Hide("dialog"))

## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:
    ## The following variables take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##  * matches all characters, except the directory separator.
    ##  ** matches all characters, including the directory separator.
    ##
    ## Examples:
    ##  "*.txt" matches txt files in the base directory.
    ##  "game/**.ogg" matches ogg files in the game directory or any of its
    ## subdirectories.
    ##  "**.psd" matches psd files anywhere in the project.

    # These variables declare the packages to build your mod that is Team Salvato
    # IPG compliant. Do not mess with these variables whatsoever.
    build.package(build.directory_name + "Mod",'zip','mod',description="Ren'Py 6 DDLC Compliant Mod")
    build.package(build.directory_name + "Renpy7Mod",'zip','windows linux mac renpy mod',description="Ren'Py 7 DDLC Compliant Mod")

    # These variables declare the archives that will be made to your packaged mod.
    # To add another archive, make a build.archive variable like in this example:
    build.archive("scripts", 'mod all')
    build.archive("mod_assets", 'mod all')

    # Do not touch these lines. This is so Ren'Py can add your mods' py file
    # and a special launcher for Linux and macOS to run your mod. 
    try: 
        build.renpy_patterns.remove(('renpy.py', ['all']))
        build.classify_renpy("renpy.py", "renpy all")
    except: pass
    
    try:
        build.early_base_patterns.remove(('*.sh', None))
        build.classify("LinuxLauncher.sh", "linux") ## Linux Launcher Script
        build.classify("*.sh", None)
    except: pass
    
    #############################################################
    # These variables classify packages for PC and Android platforms.
    # Make sure to add 'all' to your build.classify variable if you are planning
    # to build your mod on Android like in this example.
    #   Example: build.classify("game/**.pdf", "scripts all")
    
    build.classify("game/mod_assets/**", "mod_assets all")
    build.classify("game/**.rpyc", "scripts all")
    build.classify("game/README.md", None)
    build.classify("game/**.txt", "scripts all")
    build.classify("game/**.chr", "scripts all")
    build.classify("game/advanced_scripts/**","scripts all") ## Backwards Compatibility
    build.classify("game/tl/**", "scripts all") ## Translation Folder

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rpy', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa', None)
    build.classify('README.html','mod all')
    build.classify('README.linux', 'linux')
   
    # This sets' README.html as documentation
    build.documentation('README.html')

    build.include_old_themes = False
