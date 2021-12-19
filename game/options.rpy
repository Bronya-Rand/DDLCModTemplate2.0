# Options.rpy
## This template's version is 2.5.0. When asked to provide the version of the template
## you are using, give them this version number. DO NOT REMOVE OR CHANGE THIS COMMENT.

# This is the name of your mod!
# Change "DDLC Mod Template" to your mod name (e.g. "Doki Doki Yuri Time")
define config.name = "DDLC Mod Template"

# This controls whether you want your mod name to show in the main menu.
# If your mod name is long, it is suggested to turn this off.
define gui.show_name = True

# This is where you will put in the version of your mod.
# If you have multiple versions of your mod, this will be pretty useful to change.
# If you are starting out, set this to "1.0"
define config.version = "2.5.0"

# This adds information about your mod in the About section.
# DDLC does not have a about section, so you can leave this blank.
define gui.about = _("")

# This is the name of your build that the Ren'Py SDK will read.
# The build name is ASCII only so no numbers, spaces, semicolons, or very special characters.
# Example: Doki Doki Yuri Time to DokiDokiYuriTime
define build.name = "DDLCModTemplateTwo"

# This configures whether the sound volume slider should be displayed or not.
# It is best to leave this set to True by default.
define config.has_sound = True

# This configures whether the music volume slider should be displayed or not.
# It is best to leave this set to True by default.
define config.has_music = True

# This configures whether the voice volume slider should be displayed or not.
# If you use voices with `play voice` in your mod, set this to True, else leave it at False.
define config.has_voice = False

# This configures what song/music will play in the main menu.
# audio.t1 is the Doki Doki Literature Club Main Menu Music.
# If you want to change this, change the "t1" to the song you want.
define config.main_menu_music = audio.t1

# These two settings control the transition effects of the game on the game menu.
# Dissolve(.2) is the transition effect you see.
# config.enter_transition controls the effect seen when entering the game menu.
# config.exit_transition controls the effect when returning to the game.
define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)

# This controls the transition effect of the game when loading a saved game.
# By default, this is set to None and you can customize what transition you want to show.
# If you are unsure about this setting, leave it as is.
define config.after_load_transition = None

# This controls the transition effect of the game when it (the script) "ended".
# Dissolve(.5) is the transition effect you see.
define config.end_game_transition = Dissolve(.5)

# This controls how the textbox that the characters use to speak is displayed.
# "auto" sets the textbox to hide during scenes and show when a character speaks
# "show" sets the textbox to show at all times
# "hide" only shows dialogue when a character speaks.
define config.window = "auto"

# This controls the transition effects of the textbox.
# Dissolve(.2) is the transition effect you see.
# config.window_show_transition controls the effect when the textbox is shown.
# config.window_hide_transition controls the effect when the textbox is hidden.
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)

# This sets the text speed of your mod.
# By default this is set to 50. 
# Increasing this number will speed up text while decreasing the number slows down text speed.
# 0 is instant text display.
default preferences.text_cps = 50

# This controls the auto-forward speed
# 15 is DDLC's default speed.
# You can change it from 0 to 30
default preferences.afm_time = 15

# This controls the audio level of your mod.
# Increasing this will make the music louder while decreasing will make it quieter.
# SFX controls the sound effects volume.
default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75

# This controls the save directory of your mod.
# Change "DDLCModTemplateTwo" to (preferedly) your mod's name
# Windows directory for saves: %AppData%/RenPy/
# macOS directory for saves: $HOME/Library/RenPy/ (Un-hide the Library Folder)
# Linux directory for saves: $HOME/.renpy/
define config.save_directory = "DDLCModTemplateTwo"

# This controls the window icon of your mod.
# By default this defaults to the DDLC icon.
define config.window_icon = "gui/window_icon.png"

# This controls whether your mod allows skipping dialogue.
define config.allow_skipping = True

# This controls whether your mod saves automatically.
define config.has_autosave = False

# This controls whether you mod saves when quitting the game.
define config.autosave_on_quit = False

# This controls the number of slots auto-saving can use.
define config.autosave_slots = 0

# This controls the layers for screens, images, and more. 
# You are advised to leave this alone.
define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]

# These are also stuffs to leave alone.
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["front"]
define config.gl_test_image = "white"

init python:
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1]) # Prevent the game from saving in too many locations
    renpy.game.preferences.pad_enabled = False
    def replace_text(s): # Converts the dashes in texts to the special dash character
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check(): # Prevents the player from opening the game menu if quick_menu is False
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)

    import pygame_sdl2
    import os

    def saveIco(filepath): # Exports your mod logo as a icon
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

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    # Code to Package your mod to a ZIP in Ren'Py
    build.package(build.directory_name + "Mod",'zip','mod',description="Ren'Py 6 DDLC Compliant Mod")
    build.package(build.directory_name + "Renpy7Mod",'zip','windows linux mac renpy mod',description="Ren'Py 7 DDLC Compliant Mod")

    build.archive("scripts", 'mod all')
    build.archive("mod_assets", 'mod all')

    ## Do not touch this. This is so Ren'Py can add the .sh file 
    ## for Linux/Mac to run your mod.
    try:
        build.renpy_patterns.remove((u'renpy.py', [u'all']))
    except:
        pass
    build.classify_renpy("renpy.py", "renpy all")
    
    #############################################################

    # To classify packages for both pc and android, make sure to add all to it like so
    # Example: build.classify("game/**.pdf", "scripts all")
    
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
    # Dan stuff
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)
    build.classify('**.rpa', None)
    build.classify('README.html','mod all')

    # Set's README.html as documentation
    build.documentation('README.html')

    build.include_old_themes = False
