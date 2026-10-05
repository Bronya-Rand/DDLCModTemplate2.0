# Copyright 2019-2026 Azariel Del Carmen (bronya_rand). All rights reserved.
# This file declares all the screens and styles in DDLC.

## Initialization
################################################################################

init offset = -1

init python:
    # Thanks RenpyTom! Borrowed from the Ren'Py Launcher
    def scan_translations():

        languages = renpy.known_languages()

        if not languages:
            return None

        rv = [(i, renpy.translate_string("{#language name and font}", i)) for i in languages ]
        rv.sort(key=lambda a : renpy.filter_text_tags(a[1], allow=[]).lower())

        rv.insert(0, (None, "English"))

        bound = math.ceil(len(rv)/2.)

        return (rv[:bound], rv[bound:2*bound])

    def textbox_frame(high_contrast=False, opaque=False, dots=True, glare=True, button_glare=False):
        alphamask = ("textbox_alphamask_opaque" if opaque else "textbox_alphamask")
        bg_glare = Crop((0,0,1.0,1.0), "textbox_highlight") if glare else Solid("#00000000")
        if button_glare and glare:
            bg_glare = Crop((0,0,1.0,1.0), Frame("gui/quick_button_highlight.png"))
        bg = Solid("#ffbde1")
        if high_contrast:
            bg = Solid("#39051d")
        elif dots:
            bg = Image("gui/textbox_tile.png", oversample=3)
        
        r = Fixed(
        Transform(AlphaMask(Fixed(Frame(bg, tile=True), bg_glare, fit_first=True), alphamask), xalign=0.5, yalign=0.5, zoom=1.002), 
        Frame(Image("gui/textbox_border.png", oversample=3), 42, 42)) 
        
        return r

image textbox_border:
    Frame(Image("gui/textbox_border.png", oversample=3), 42, 42)
image textbox_highlight:
    Image("gui/textbox_highlight.png", oversample=3, xalign=0.5, yalign=1.0)
image textbox_alphamask:
    Frame(Image("gui/textbox_alphamask.png", oversample=3), 42, 42)
image textbox_alphamask_opaque:
    Frame(Image("gui/textbox_alphamask_opaque.png", oversample=3), 42, 42)
image textbox_buttonglare:
    Fixed(Frame(Image("gui/textbox_tile.png", oversample=3), tile=True), Crop((0,0,1.0,1.0), Frame("gui/quick_button_highlight.png")), fit_first=True)

image textbox_background = textbox_frame()
image textbox_background_opaque = textbox_frame(opaque=True)
image textbox_background_hc = textbox_frame(high_contrast=True, glare=False)
image textbox_background_hc_opaque = textbox_frame(high_contrast=True, opaque=True, glare=False)
image rounded_frame_background = textbox_frame(dots=False)
image rounded_frame_background_opaque = textbox_frame(opaque=True, dots=False)
image rounded_frame_background_hc = textbox_frame(high_contrast=True, glare=False)
image rounded_frame_background_hc_opaque = textbox_frame(high_contrast=True, opaque=True, glare=False)

default translations = scan_translations()

# Enables the ability to add more settings in the game such as Uncensored Mode.
default extra_settings = True
# If you are using the Extras Menu feature, set this line to True.
default enable_extras_menu = False
# If you are going to use extra languages, set this to True.
default enable_languages = False

## Color Styles
################################################################################

# This controls the color of outlines in the game like
# text, say, navigation, labels and such.
define -2 text_outline_color = "#b59"

## Styles
################################################################################

style default:
    font gui.text_font
    size get_variable_size(gui.text_size, gui.max_text_size, gui.text_scale)
    color gui.text_color
    outlines get_scaled_outlines([(2, "#000000aa", 0, 0)], gui.text_size, gui.max_text_size, gui.text_scale)
    line_overlap_split 1
    line_spacing 1

style default_monika is normal:
    slow_cps 30

style edited is default:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines get_scaled_outlines([(10, "#000", 0, 0)], gui.text_size, gui.max_text_size, gui.text_scale)
    xpos gui.dialogue_xpos
    xanchor gui.dialogue_text_xalign
    xsize get_variable_size(gui.dialogue_width, gui.max_dialogue_width, gui.text_scale)
    ypos gui.dialogue_ypos
    text_align gui.dialogue_text_xalign
    layout ("subtitle" if gui.dialogue_text_xalign else "tex")

style normal is default:
    xpos gui.dialogue_xpos
    xanchor gui.dialogue_text_xalign
    xsize get_variable_size(gui.dialogue_width, gui.max_dialogue_width, gui.text_scale)
    ypos gui.dialogue_ypos

    text_align gui.dialogue_text_xalign
    layout ("subtitle" if gui.dialogue_text_xalign else "tex")

style input:
    color gui.accent_color

style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True

style splash_text:
    size get_variable_size(24, 36, gui.text_scale)
    color "#000"
    font gui.text_font
    text_align 0.5
    outlines []

style poemgame_button is button:
    xsize 226
    ysize 63

style poemgame_text:
    yalign 0.5
    font gui.halogen_font
    size get_variable_size(30, 36, gui.text_scale)
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines get_scaled_outlines([(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)], 30, 36, gui.text_scale)

style gui_text:
    font gui.interface_text_font
    color gui.interface_text_color
    size get_variable_size(gui.interface_text_size, gui.max_interface_text_size, gui.text_scale)

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.button_text_properties("button")
    size get_variable_size(gui.button_text_size, gui.max_button_text_size, gui.text_scale)
    yalign 0.5


style label_text is gui_text:
    color gui.accent_color
    size get_variable_size(gui.label_text_size, gui.max_label_text_size, gui.text_scale)

style prompt_text is gui_text:
    color gui.text_color
    size get_variable_size(gui.interface_text_size, gui.max_interface_text_size, gui.text_scale)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True


style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/slider/horizontal_hover_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True
    thumb_offset (8, 8)

style vscrollbar_hc is vscrollbar:
    base_bar Frame("gui/scrollbar/vertical_poem_bar_hc.png", tile=False)
    thumb Frame("gui/slider/horizontal_hover_thumb_hc.png", left=6, top=6, tile=True)

style slider:
    ysize (34 if renpy.mobile else 18)
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Transform("gui/slider/horizontal_hover_thumb.png", zoom=(1.0 if renpy.mobile else 0.7), anchor=(0.5, 0.5))
    thumb_offset 8

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"
    thumb_offset (8, 8)

style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
    # background Frame(recolorize("gui/frame.png"), gui.frame_borders, tile=gui.frame_tile)

################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        text what id "what"

        if who is not None:

            window:
                style "namebox"
                text who id "who"

    # If there's a side image, display it above the text. Do not display
    # on the phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu


style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xsize get_variable_size(gui.dialogue_width, gui.max_dialogue_width, gui.text_scale) + (gui.dialogue_xpos * 2)
    yalign gui.textbox_yalign
    ysize get_variable_size(gui.textbox_height, gui.max_textbox_height, gui.text_scale)

    background "textbox_background"

style window_monika is window:
    background Transform("gui/textbox_monika.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    color gui.accent_color
    font gui.name_text_font
    size get_variable_size(gui.name_text_size, gui.max_name_text_size, gui.text_scale)
    xalign gui.name_xalign
    yalign 0.5
    outlines get_scaled_outlines([(3, text_outline_color, 0, 0), (1, text_outline_color, 1, 1)], gui.name_text_size, gui.max_name_text_size, gui.text_scale)

style say_dialogue:
    xpos gui.dialogue_xpos
    xanchor gui.dialogue_text_xalign
    xfill True
    ypos gui.dialogue_ypos
    xsize get_variable_size(gui.dialogue_width, gui.max_dialogue_width, gui.text_scale)
    text_align gui.dialogue_text_xalign
    layout ("subtitle" if gui.dialogue_text_xalign else "tex")

image ctc_image:
    subpixel True
    alpha 0.0
    xoffset -5
    Transform("gui/ctc.png", zoom=get_resolution_scale())
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat

image auto_ctc_base = Transform("gui/auto_ctc_base.png", zoom=get_resolution_scale())
image auto_ctc_fill = Transform("gui/auto_ctc_fill.png", zoom=get_resolution_scale())

transform auto_ctc_pos:
    zoom 0.7
    yalign 0.98
    xoffset -5
    alpha 0.0
    easeout 0.1 alpha 0.8
    on hide:
        easeout 0.1 alpha 0.0

screen ctc:
    fixed at auto_ctc_pos:
        style "ctc_fixed"

        if _preferences.afm_enable == True:
            add "auto_ctc_base" at auto_ctc_pos:
                fit "cover"
                align (0.5, 0.5)
            # add "auto_ctc_fill" at radial_alpha(wait_timer=get_automode_time()), auto_ctc_pos:
            #     fit "cover"
            #     align (0.5, 0.5)
        else:
            add "ctc_image" at auto_ctc_pos:
                fit "scale-up"
                align (0.5, 0.5)

style ctc_fixed:
    xalign gui.ctc_xalign
    xysize (round(50 * gui.ctc_zoom), round(50 * gui.ctc_zoom))

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## http://www.renpy.org/doc/html/screen_special.html#input

image input_caret:
    Solid(text_outline_color)
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

screen input(prompt):
    style_prefix "input"

    window:
        has vbox
        xpos gui.dialogue_xpos
        xanchor 0.5
        ypos gui.dialogue_ypos

        text prompt style "input_prompt"
        input id "input"


style input_prompt is default

style input_prompt:
    xmaximum gui.dialogue_width
    xalign gui.dialogue_text_xalign
    text_align gui.dialogue_text_xalign

style input:
    caret "input_caret"
    xmaximum gui.dialogue_width
    xalign 0.5
    text_align 0.5


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## New as of 3.0.0
##    - You may now pass through argurments to the menu options to colorize
##      your menu as you like. Add (kwargs=[color hex or style name]) to your
##      menu option name and you get different buttons! 
##
##      Examples: "Option 1 (kwargs=#00fbff)" | "Option 2 (kwargs=#00fbff, #6cffff)"
##
## http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:

        for i in items:
            
            if "kwargs=" in i.caption:

                $ kwarg = i.caption.split("(kwargs=")[-1].replace(")", "")
                $ caption = i.caption.replace(" (kwargs=" + kwarg + ")", "")

                if "#" in kwarg:
                    
                    $ kwarg = kwarg.replace(", ", ",").split(",")
                    
                    if len(kwarg) == 1:
                        $ kwarg.append('#ffe6f4')
                    
                    $ arg1 = kwarg[0]
                    $ arg2 = kwarg[-1]
                    
                    textbutton caption:
                        idle_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_idle_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, arg2)), gui.choice_button_borders)
                        hover_background Frame(im.MatrixColor(im.MatrixColor("gui/button/choice_hover_background.png", im.matrix.desaturate() * im.matrix.contrast(1.29) * im.matrix.colorize("#00f", "#fff") * im.matrix.saturation(120)), 
                            im.matrix.desaturate() * im.matrix.colorize(arg1, "#fff")), gui.choice_button_borders)
                        action i.action

                else:

                    textbutton caption:
                        style kwarg
                        action i.action

            else:

                textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    xsize get_variable_size(gui.choice_button_width, gui.max_choice_button_width, gui.text_scale)
    hover_sound (gui.hover_sound if not renpy.mobile else None)
    activate_sound gui.activate_sound

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    size get_variable_size(gui.choice_button_text_size, gui.max_choice_button_text_size, gui.text_scale)
    outlines []


init python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

screen rigged_choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action

    timer 1.0/30.0 repeat True action Function(RigMouse)


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    # Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        # Add an in-game quick menu.
        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 0.995

            #textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Load") action ShowMenu('load')
            #textbutton _("Q.Save") action QuickSave()
            #textbutton _("Q.Load") action QuickLoad()
            textbutton _("Settings") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
#init python:
#    config.overlay_screens.append("quick_menu")

default quick_menu = True

#style quick_button is default
#style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")
    activate_sound gui.activate_sound

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    size get_variable_size(gui.quick_button_text_size, gui.max_quick_button_text_size, gui.text_scale)
    outlines []

style quick_hbox:
    spacing get_variable_size(gui.quick_menu_spacing, gui.max_quick_menu_spacing, gui.text_scale)


################################################################################
# Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

init python:
    def FinishEnterName(start_game=True):
        if not player: 
            if renpy.mobile:
                renpy.hide_screen("name_input")
            return
        persistent.playername = player
        renpy.save_persistent()
        renpy.hide_screen("name_input")
        if launchGame:
            renpy.jump_out_of_context("start")

screen navigation():
    if main_menu:
        add "menu_nav"
    else:
        add "game_nav"

    vbox:
        style_prefix "navigation"

        if renpy.mobile:
            xpos gui.navigation_xpos
            spacing gui.max_navigation_spacing
        else:
            xpos get_variable_size(gui.max_navigation_xpos, gui.navigation_xpos, gui.text_scale)
            spacing get_variable_size(gui.navigation_spacing, gui.max_navigation_spacing, gui.text_scale)
        
        yanchor 1.0
        yalign 0.85
        xmaximum 200

        if not persistent.autoload or not main_menu:

            if main_menu:

                if persistent.playthrough == 1:
                    textbutton _("ŔŗñĮ¼»ŧþŀÂŻŕěōì«") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName))) at loc_text_fit
                else:
                    textbutton _("New Game") action If(persistent.playername, true=Start(), false=Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName))) at loc_text_fit

            else:

                textbutton _("History") action [ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)] at loc_text_fit

                textbutton _("Save Game") action [ShowMenu("save"), SensitiveIf(renpy.get_screen("save") == None)] at loc_text_fit

            textbutton _("Load Game") action [ShowMenu("load"), SensitiveIf(renpy.get_screen("load") == None)] at loc_text_fit

            if enable_extras_menu:
                textbutton _("Extras") action [ShowMenu("extras"), SensitiveIf(renpy.get_screen("extras") == None)] at loc_text_fit

            elif not main_menu:
                if persistent.playthrough != 3:
                    textbutton _("Main Menu") action MainMenu()
                else:
                    textbutton _("Main Menu") action NullAction()

            textbutton _("Settings") action [ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]

            if not enable_extras_menu:
                textbutton _("Credits") action ShowMenu("about")

            if _in_replay:
                textbutton _("End Replay") action EndReplay(confirm=True) at loc_text_fit

            if renpy.variant("pc"):

                ## Help isn't necessary or relevant to mobile devices.
                textbutton _("Help") action [Help("README.html"), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"))]

                ## The quit button is banned on iOS and unnecessary on Android.
                textbutton _("Quit") action Quit(confirm=not main_menu)
        else:
            timer 1.75 action Start("autoload_yurikill")


style navigation_button is gui_button
style navigation_button_text is gui_button_text:
    size (gui.max_button_text_size if renpy.mobile else get_variable_size(gui.button_text_size, gui.max_button_text_size, gui.text_scale))

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    ysize (54 if renpy.mobile else gui.button_height)
    hover_sound (gui.hover_sound if not renpy.mobile else None)
    activate_sound gui.activate_sound

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    layout "nobreak"
    font gui.riffic_font
    color "#fff"
    outlines get_scaled_outlines([(4, text_outline_color, 0, 0), (2, text_outline_color, 2, 2)], (gui.max_button_text_size if renpy.mobile else gui.button_text_size), gui.max_button_text_size, gui.text_scale)
    hover_outlines get_scaled_outlines([(4, "#fac", 0, 0), (2, "#fac", 2, 2)], (gui.max_button_text_size if renpy.mobile else gui.button_text_size), gui.max_button_text_size, gui.text_scale)
    insensitive_outlines get_scaled_outlines([(4, "#fce", 0, 0), (2, "#fce", 2, 2)], (gui.max_button_text_size if renpy.mobile else gui.button_text_size), gui.max_button_text_size, gui.text_scale)


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    if persistent.ghost_menu:
        add "white"
        add "menu_art_y_ghost"
        add "menu_art_n_ghost"
    else:
        add "menu_bg"
        add "menu_art_y"
        add "menu_art_n"
        frame

        ## The use statement includes another screen inside this one. The actual
        ## contents of the main menu are in the navigation screen.
        use navigation

    if gui.show_name:
        vbox:
            text "[config.name!t]":
                style "main_menu_title"
            text "[config.version!t]":
                style "main_menu_version"

    if not persistent.ghost_menu:
        add "menu_particles"
        add "menu_particles"
        add "menu_particles"
        add "menu_logo"
    if persistent.ghost_menu:
        add "menu_art_s_ghost"
        add "menu_art_m_ghost"
        
        if renpy.mobile:
            timer 4.0 action Show("fullscreen_return_button")
    else:
        if persistent.playthrough == 1 or persistent.playthrough == 2:
            add "menu_art_s_glitch"
        else:
            add "menu_art_s"
        add "menu_particles"
        if persistent.playthrough != 4:
            add "menu_art_m"
        add "menu_fade"

    key "K_ESCAPE" action Quit(confirm=False)

screen fullscreen_return_button:
    button:
        xysize (1.0, 1.0)
        action Jump("quit")

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text:
    color "#000000"
    size 16
    outlines []

style main_menu_frame:
    xsize 310
    yfill True

    background None

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    xalign 1.0

    layout "subtitle"
    text_align 1.0
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When this
## screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu_m():
    $ persistent.menu_bg_m = True
    add "gui/menu_bg_m.png"
    timer 0.3 action Hide("game_menu_m")

screen game_menu(title, scroll=None):

    # Add the backgrounds.
    if main_menu:
        add gui.main_menu_background
    else:
        key "mouseup_3" action Return()
        add gui.game_menu_background

    style_prefix "game_menu"

    use navigation

    frame:
        style "game_menu_outer_frame"

        has hbox

        frame:
            style "game_menu_navigation_frame"

        frame:
            style "game_menu_content_frame"

            # if renpy.get_screen("history"):
            #     background Frame("history_background")
            #     padding (10, 10)
            #     xsize 1.0

            if scroll == "viewport":

                viewport:
                    at vp_vert_scroll_mask
                    scrollbars "vertical"
                    vscrollbar_xoffset -30
                    mousewheel True
                    draggable True

                    side_yfill True

                    has vbox
                    transclude

            elif scroll == "vpgrid":

                vpgrid:
                    cols 1

                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    side_yfill True

                    transclude

            else:

                transclude

    if not main_menu and persistent.playthrough == 2 and not persistent.menu_bg_m and renpy.random.randint(0, 49) == 0 and persistent.content_warnings_enabled == False:
        on "show" action Show("game_menu_m")

    textbutton _("Return"):
        style "return_button"
        if renpy.mobile:
            xpos gui.navigation_xpos
        else:
            xpos get_variable_size(gui.max_navigation_xpos, gui.navigation_xpos, gui.text_scale)
        action Return()

    label title xoffset -16

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 30

    background None

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    font gui.riffic_font
    size gui.title_text_size
    color "#fff"
    outlines [(6, text_outline_color, 0, 0), (3, text_outline_color, 2, 2)]
    yalign 0.5

style return_button:
    xpos get_variable_size(gui.max_navigation_xpos, gui.navigation_xpos, gui.text_scale)
    yalign 1.0
    yoffset -30


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("Credits"), scroll="viewport"):

        style_prefix "about"

        window:
            xoffset 35
            has fixed:
                yfit True

            vbox:
                add Transform("mod_assets/DDLCModTemplateLogo.png", size=(200,200)) xalign .5

                null height 5
                
                label "[config.name!t]" xalign .5
                text _("Version [config.version!t]\n") xalign .5

                ## gui.about is usually set in options.rpy.
                if gui.about:
                    text "[gui.about!t]\n"

                ## Do not touch/remove these unless the © or – symbol isn't available in your font.
                ## You may add things above or below it.
                ## If you are not going with a splashscreen option, this first line MUST stay in the mod.
                text "Made with bronya_rand's {a=https://github.com/Bronya-Rand/DDLCModTemplate2.0}DDLC Mod Template 2.0{/a}\nCopyright © 2019-" + str(datetime.date.today().year) + " Azariel Del Carmen (bronya_rand). All rights reserved.\n"
                text "Doki Doki Literature Club. Copyright © 2017 Team Salvato. All rights reserved.\n"
                text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""

style about_window is empty
style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    color "#000"
    outlines []
    text_align 0.5
    size gui.label_text_size

style about_text:
    color "#000"
    outlines []
    size gui.text_size
    text_align 0.5
    layout "subtitle"

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    idle_color gui.idle_color
    hover_color gui.hover_color
    hover_underline True

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

init python:
    def FileActionMod(name, page=None, **kwargs):
        if persistent.playthrough == 1 and not persistent.deleted_saves and renpy.current_screen().screen_name[0] == "load" and FileLoadable(name):
            return Show(screen="dialog", message="File error: \"characters/sayori.chr\"\n\nThe file is missing or corrupt.",
                ok_action=Show(screen="dialog", message="The save file is corrupt. Starting a new game.", ok_action=Function(renpy.full_restart, label="start")))
        elif persistent.playthrough == 3 and renpy.current_screen().screen_name[0] == "save":
            return Show(screen="dialog", message="There's no point in saving anymore.\nDon't worry, I'm not going anywhere.", ok_action=Hide("dialog"))
        else:
            return FileAction(name)


screen file_slots(title):

    default page_name_value = FilePageNameInputValue()

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            # The page name, which can be edited by clicking on a button.

            button:
                style "page_label"

                #key_events True
                xalign 0.5
                #action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileActionMod(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                #textbutton _("<") action FilePagePrevious(max=9, wrap=True)

                #textbutton _("{#auto_page}A") action FilePage("auto")

                #textbutton _("{#quick_page}Q") action FilePage("quick")

                # range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                #textbutton _(">") action FilePageNext(max=9, wrap=True)


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#666"
    outlines []

style mobile_slot_time_text is slot_button_text:
    size 24

screen viewframe_options(title):

    style_prefix "viewframe"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 2

            label title

            null height 10

            transclude

style viewframe_frame is confirm_frame
style viewframe_label is confirm_prompt:
    xalign 0.5
style viewframe_label_text is confirm_prompt_text
style viewframe_button is confirm_button
style viewframe_button_text is confirm_button_text
style viewframe_text is confirm_prompt_text:
    size 20
    yalign 0.7

## Windowed Resolutions
## Windowed Resolutions allow players to scale the game to different resolutions.
## Uncomment the below #'s to enable this.
# screen confirm_res(old_res):
    
#     ## Ensure other screens do not get input while this screen is displayed.
#     modal True

#     zorder 200

#     style_prefix "confirm"

#     add "gui/overlay/confirm.png"

#     frame:

#         vbox:
#             xalign .5
#             yalign .5
#             spacing 30

#             ## This if-else statement either shows a normal textbox or
#             ## glitched textbox if you are in Sayori's Death Scene and are
#             ## quitting the game.
#             # if in_sayori_kill and message == layout.QUIT:
#             #     add "confirm_glitch" xalign 0.5
#             # else:
#             label _("Would you like to keep these changes?"):
#                 style "confirm_prompt"
#                 xalign 0.5

#             add DynamicDisplayable(res_text_timer) xalign 0.5

#             hbox:
#                 xalign 0.5
#                 spacing 100

#                 ## This if-else statement disables quitting from the quit box
#                 ## if you are in Sayori's Death Scene, else normal box.
#                 # if in_sayori_kill and message == layout.QUIT:
#                 #     textbutton _("Yes") action NullAction()
#                 #     textbutton _("No") action Hide("confirm")
#                 # else:
#                 textbutton _("Yes") action Hide("confirm_res")
#                 textbutton _("No") action [Function(renpy.set_physical_size, old_res), Hide("confirm_res")]
    
#     timer 5.0 action [Function(renpy.set_physical_size, old_res), Hide("confirm_res")]

# init python:
#     def res_text_timer(st, at):
#         if st <= 5.0:
#             time_left = str(round(5.0 - st))
#             return Text(time_left, style="confirm_prompt"), 0.1
#         else: return Text("0", style="confirm_prompt"), 0.0

#     def set_physical_resolution(res):
#         old_res = renpy.get_physical_size()
#         renpy.set_physical_size(res)
#         renpy.show_screen("confirm_res", old_res=old_res)

# screen display_options():

#     style_prefix "viewframe"

#     modal True

#     zorder 150

#     use viewframe_options(_("Display Resolutions")):

#         default scale = renpy.get_physical_size()

#         vbox:
#             xmaximum 500
#             ysize 120
#             viewport:
#                 style_prefix "radio"
#                 scrollbars "vertical"
#                 mousewheel True
#                 draggable True
#                 has vbox

#                 textbutton "1280x720" action SetScreenVariable("scale", (1280, 720))
#                 textbutton "1600x900" action SetScreenVariable("scale", (1600, 900))

#         null height 10

#         hbox:
#             xalign 0.5
#             spacing 100

#             textbutton _("Reset") action [Hide("display_options"), Function(renpy.reset_physical_size)]
#             textbutton _("Set") action [Hide("display_options"), Function(set_physical_resolution, scale)]

image slider_volume_icon_min:
    ("gui/slider_volume_icon_min.png" if not persistent.high_contrast else "gui/slider_volume_icon_hc_min.png")
image slider_volume_icon_max:
    ("gui/slider_volume_icon_max.png" if not persistent.high_contrast else "gui/slider_volume_icon_hc_max.png")

image slider_autopace_icon_min:
    ("gui/slider_autopace_icon_min.png" if not persistent.high_contrast else "gui/slider_autopace_icon_hc_min.png")
image slider_autopace_icon_max:
    ("gui/slider_autopace_icon_max.png" if not persistent.high_contrast else "gui/slider_autopace_icon_hc_max.png")

image slider_textsize_icon_min:
    ("gui/slider_textsize_icon_min.png" if not persistent.high_contrast else "gui/slider_textsize_icon_hc_min.png")
image slider_textsize_icon_max:
    ("gui/slider_textsize_icon_max.png" if not persistent.high_contrast else "gui/slider_textsize_icon_hc_max.png")

screen display_preferences(music_volume, sound_volume, voice_volume):
    vbox:
        fixed:
            ysize 200
            
            if not renpy.mobile:
                vbox:
                    style_prefix "radio"
                    xalign 0.0
                    label _("Display")
                    textbutton _("Windowed") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")
                    # textbutton _("More") action Show("display_options")

            vbox:
                style_prefix "slider"
                xalign (1.0 if not renpy.mobile else 0.0)
                ysize 1.0

                if config.has_music:
                    label _("Music Volume")

                    side "c l r":
                        bar:
                            value ScreenVariableValue("music_volume", range=1.0, offset=0, step=0.1, force_step=True, style="slider")
                            changed preferences.set_mixer("music", music_volume)
                        add "slider_volume_icon_min" yalign 0.5 zoom 0.5
                        add "slider_volume_icon_max" yalign 0.5 zoom 0.5

                if config.has_sound:
                    label _("Sound Volume")

                    side "c l r":
                        bar:
                            value ScreenVariableValue("sound_volume", range=1.0, offset=0, step=0.1, force_step=True, style="slider")
                            changed preferences.set_mixer("sfx", sound_volume)
                        add "slider_volume_icon_min" yalign 0.5 zoom 0.5
                        add "slider_volume_icon_max" yalign 0.5 zoom 0.5

                    if config.sample_sound:
                        textbutton _("Test") action Play("sound", config.sample_sound)
                
                if config.has_voice:
                    label _("Voice Volume")

                    side "c l r":
                        bar:
                            value ScreenVariableValue("voice_volume", range=1.0, offset=0, step=0.1, force_step=True, style="slider")
                            changed preferences.set_mixer("voice", voice_volume)
                        add "slider_volume_icon_min" yalign 0.5 zoom 0.5
                        add "slider_volume_icon_max" yalign 0.5 zoom 0.5

                    if config.sample_voice:
                        textbutton _("Test") action Play("voice", config.sample_voice)

                if config.has_music or config.has_sound or config.has_voice:
                    null height gui.pref_spacing

                    textbutton _("Mute All"):
                        action Preference("all mute", "toggle")
                        style "mute_all_button"

screen language_preferences():
    vbox:
        hbox:
            style_prefix "slider"
            box_wrap False

            vbox:
                label _("Text Speed")

                side "c l r":
                    bar value FieldValue(_preferences, "text_cps", style="slider", range=180, step=30, force_step=True, max_is_zero=False, offset=20):
                        alt "Text Speed"
                    add "slider_autopace_icon_min" yalign 0.5 zoom 0.5
                    add "slider_autopace_icon_max" yalign 0.5 zoom 0.5

                label _("Auto-Forward Speed")

                side "c l r":
                    bar value FieldValue(_preferences, "afm_time", style="slider", range=18, step=3, force_step=True, offset=1):
                        bar_invert True
                    add "slider_autopace_icon_min" yalign 0.5 zoom 0.5
                    add "slider_autopace_icon_max" yalign 0.5 zoom 0.5
                
                label _("Text Size")

                side "c l r":
                    bar value FieldValue(_preferences, "text_scale", style="slider", range=0.5, offset=0.5, step=0.25, force_step=True):
                        released gui.SetPreference("text_scale", preferences.text_scale)
                        alt "Text Size"
                    add "slider_textsize_icon_min" yalign 0.5 zoom 0.5
                    add "slider_textsize_icon_max" yalign 0.5 zoom 0.5

            vbox:
                xsize 1.0
                if renpy.mobile:
                    style_prefix "radio"
                    label _("Allow Skipping")
                    textbutton _("Previously Read Text Only") action Preference("skip", "seen")
                    textbutton _("All Text") action Preference("skip", "all")
                else:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")

        # null height 40

        # if persistent.high_contrast == True:
        #     add "gui/long_divider_dark_hc.png":
        #         xzoom 0.65
        #         yzoom 0.80
        #         xoffset 30
        # else:
        #     add "gui/long_divider_dark.png":
        #         xzoom 0.65
        #         yzoom 0.80
        #         xoffset 30
            
        # null height 14

        # label _("Language")

        # hbox:
        #     xsize 1.0

        ## TODO: Language selection dropdown/menu

screen accessibility_preferences():
    viewport id "settings_accessibility_viewport":
        # at vp_vert_scroll_mask
        draggable True
        mousewheel True
        ysize 1.0
        has vbox
        null height 20

        vbox:
            style_prefix "check"
            xsize 1.0

            textbutton _("Content Warnings") action ToggleField(persistent, "show_content_warnings", True, False) alt _("Enable Content Warnings")
            text _("Enables content warnings that will appear before scenes with disturbing subject matter.") style "pref_hint_text"
            textbutton _("High Contrast Textboxes") action [ToggleField(persistent, "high_contrast", True, False), Function(gui.rebuild)] alt _("High Contrast Textboxes")
            text _("Replaces the dialogue box with a darker variant, making dialogue easier to read.") style "pref_hint_text"
            textbutton _("Reduce Textbox Transparency") action [ToggleField(persistent, "reduce_transparency", True, False), Function(gui.rebuild)] alt _("Reduce Textbox Transparency")
            text _("Makes the dialogue box opaque, making dialogue easier to read.") style "pref_hint_text"
            textbutton _("Alternate Poem Font") action ToggleField(persistent, "use_alt_poem_font", True, False) alt _("Use Alternate Poem Font") 
            text _("Switches handwritten fonts in characters' poems with an easier-to-read font.") style "pref_hint_text"

        null height 20

    vbar value YScrollValue("settings_accessibility_viewport") xpos 1.0 xoffset -10 style ("vscrollbar" if not persistent.high_contrast else "vscrollbar_hc")

screen template_preferences():
    vbox:
        hbox:
            box_wrap False

            vbox:
                style_prefix "name"
                label _("Player Name")
            
                null height 3
            
                if player == "":
                    text _("No Name Set") xalign 0.5
                else:
                    text "[player]" xalign 0.5
            
                textbutton _("Change Name") action Show(screen="name_input", message="Please enter your name", ok_action=Function(FinishEnterName, launchGame=False)):
                    text_style "navigation_button_text"
        
            python:
                has_discord_module = True
                try:
                    RPC
                except NameError:
                    has_discord_module = False

            if not renpy.mobile and has_discord_module:
                vbox:
                    style_prefix "name"
                    label _("Discord RPC")

                    python:
                        connect_status = _("Disconnected")
                        if not persistent.enable_discord:
                            connect_status = _("Disabled")
                        if RPC.rpc_connected:
                            connect_status = _("Connected")
                    
                    null height 3

                    text "[connect_status]" xalign 0.5

                    python:
                        enable_text = _("Enable")
                        if persistent.enable_discord:
                            enable_text = _("Disable")

                    textbutton enable_text action [ToggleField(persistent, "enable_discord"), 
                        If(persistent.enable_discord, Function(RPC.disconnect), Function(RPC.connect))]:
                            text_style "navigation_button_text"
                    if persistent.enable_discord and not RPC.rpc_connected:
                        textbutton _("Reconnect") action Function(RPC.connect):
                            text_style "navigation_button_text"

    # null height 80

style name_label is pref_label
style name_label_text is pref_label_text
style name_text is radio_button_text:
    color ("#000" if not persistent.high_contrast else "#ffdfee")

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

init python:
    def vp_vert_scroll_mask(d):
        return AlphaMask(d, Frame("gui/viewport-vertical-fade.png", 0, 13))

image pref_background:
    textbox_frame(high_contrast=persistent.high_contrast, opaque=persistent.reduce_transparency, dots=False, glare=False)

screen preferences():
    tag menu
    
    ## These default variables keep track of the current tab and volume levels.
    default music_volume = preferences.get_mixer("music")
    default sound_volume = preferences.get_mixer("sfx")
    default voice_volume = preferences.get_mixer("voice")
    default current_tab = "display"
    on "show" action [SetScreenVariable("music_volume", preferences.get_mixer("music")),  SetScreenVariable("sound_volume", preferences.get_mixer("sfx")), SetScreenVariable("voice_volume", preferences.get_mixer("voice"))]   

    if renpy.mobile:
        $ cols = 2
    else:
        $ cols = 4

    use game_menu(_("Settings")):
        side "t c":
            hbox:
                xalign 0.5
                button:
                    style ("pref_active_tab_button" if current_tab == "display" else "pref_tab_button")
                    action SetScreenVariable("current_tab", "display")
                    left_padding 10
                    has side 'l c'

                    if renpy.mobile:
                        add ("gui/pref_display_icon_mobile_selected.png" if current_tab == "display" else "gui/pref_display_icon_mobile.png"):
                            yalign 0.75
                            zoom 0.5
                    else:
                        add ("gui/pref_display_icon_selected.png" if current_tab == "display" else "gui/pref_display_icon.png"):
                            yalign 0.75
                            zoom 0.5
                    label (_("Audio") if renpy.mobile else _("Display & Sound")) yalign 0.0 text_size (24 if renpy.mobile else 18) at loc_text_fit style "pref_tab_label"
                button:
                    style ("pref_active_tab_button" if current_tab == "language" else "pref_tab_button")
                    action SetScreenVariable("current_tab", "language")
                    has side 'l c'
                    add ("gui/pref_language_icon_selected.png" if current_tab == "language" else "gui/pref_language_icon.png"):
                        yalign 0.75
                        zoom 0.5
                    label _("Language & Text") yalign 0.0 text_size (24 if renpy.mobile else 18) at loc_text_fit style "pref_tab_label"
                button:
                    style ("pref_active_tab_button" if current_tab == "accessibility" else "pref_tab_button")
                    action SetScreenVariable("current_tab", "accessibility")
                    has side 'l c'
                    add ("gui/pref_accessibility_icon_selected.png" if current_tab == "accessibility" else "gui/pref_accessibility_icon.png"):
                        yalign 0.75
                        zoom 0.5
                    label _("Accessibility") yalign 0.0 text_size (24 if renpy.mobile else 18) at loc_text_fit style "pref_tab_label"
                button:
                    style ("pref_active_tab_button" if current_tab == "bronya" else "pref_tab_button")
                    action SetScreenVariable("current_tab", "bronya")
                    has side 'l c'
                    add ("gui/pref_bronya_icon_selected.png" if current_tab == "bronya" else "gui/pref_bronya_icon.png"):
                        yalign 0.75
                        zoom 0.5
                    label _("Mod Template") yalign 0.0 text_size (24 if renpy.mobile else 18) at loc_text_fit style "pref_tab_label"
            
            frame:
                padding (30, 30)
                background "pref_background"

                showif current_tab == "display":
                    use display_preferences(music_volume, sound_volume, voice_volume)
                elif current_tab == "language":
                    use language_preferences
                elif current_tab == "accessibility":
                    use accessibility_preferences
                elif current_tab == "bronya":
                    use template_preferences
                            
    text "v[config.version]":
        xalign 1.0 yalign 1.0
        xoffset -10 yoffset -10
        style "main_menu_version"

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    font gui.riffic_font
    size get_variable_size(24, 28, gui.text_scale)
    color "#fff"
    outlines (get_scaled_outlines([(3, text_outline_color, 0, 0), (1, text_outline_color, 1, 1)], 24, 28, gui.text_scale) if not persistent.high_contrast else get_scaled_outlines([(2, gui.hc_label_outline_color, 0, 0), (1, gui.hc_label_outline_color, 1, 1)], 24, 28, gui.text_scale))
    yalign 1.0

style pref_tab_button:
    xysize (get_pref_tab_button_width(), 60)
    yalign 1.0
    background Frame("gui/namebox-deselected.png", 3, 3)
    hover_sound (gui.hover_sound if not renpy.mobile else None)
    activate_sound gui.activate_sound
    yoffset 9
style pref_active_tab_button is pref_tab_button:
    background Frame("gui/namebox-selected.png", 3, 3)
    yoffset 0
style pref_tab_label is pref_label
style pref_tab_label_text is pref_label_text:
    outlines [(4, text_outline_color, 0, 0), (1, text_outline_color, 1, 1)]
    layout "nobreak"

style pref_header_label is pref_label
style pref_header_label_text is pref_label_text:
    size get_variable_size(28, 38, gui.text_scale)
    outlines get_scaled_outlines([(4, text_outline_color, 0, 0), (1, text_outline_color, 1, 1)], 28, 38, gui.text_scale)

style pref_hint_text:
    font gui.halogen_font
    size get_variable_size(24, 30, gui.text_scale)
    outlines []
    color (text_outline_color if not persistent.high_contrast else "#ffdfee")
    xoffset get_variable_size(40, 60, gui.text_scale)
    xmaximum 800

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing get_variable_size(gui.pref_button_spacing, gui.max_pref_button_spacing, gui.text_scale)

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    # yminimum get_variable_size(24, 32, gui.text_scale)
    # ymaximum get_variable_size(48, 64, gui.text_scale)

style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/Halogen.ttf"
    outlines []


style check_vbox:
    spacing get_variable_size(gui.pref_button_spacing, gui.max_pref_button_spacing, gui.text_scale)

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"
    # ysize get_variable_size(24, 32, gui.text_scale)

style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/Halogen.ttf"
    outlines []


style slider_slider:
    xsize 350
    base_bar ("gui/scrollbar/horizontal_poem_bar_short.png" if not persistent.high_contrast else "gui/scrollbar/horizontal_poem_bar_short_hc.png")
    thumb ("gui/slider/horizontal_hover_thumb.png" if not persistent.high_contrast else "gui/slider/horizontal_hover_thumb_hc.png")
    yalign 0.5

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450

## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():
    tag menu
    
    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
        style_prefix "history"
       
        for h in _history_list:
            
            window:
                ## This lays things out properly if history_height is None.
                has fixed
                yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False
                        
                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                text h.what:
                    ypos (gui.history_text_ypos if h.who else gui.history_name_ypos)
            null height get_variable_size(12, 15)

        if not _history_list:
            label _("The dialogue history is empty.")

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text is namebox_label:
    min_width gui.history_name_width
    text_align gui.history_name_xalign
    xalign 0.0
    layout "nobreak"

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

#screen help():
#
#    tag menu
#
#    default device = "keyboard"
#
#    use game_menu(_("Help"), scroll="viewport"):
#
#        style_prefix "help"
#
#        vbox:
#            spacing 15
#
#            hbox:
#
#                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
#                textbutton _("Mouse") action SetScreenVariable("device", "mouse")
#
#                if GamepadExists():
#                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")
#
#            if device == "keyboard":
#                use keyboard_help
#            elif device == "mouse":
#                use mouse_help
#            elif device == "gamepad":
#                use gamepad_help
#
#
#screen keyboard_help():
#
#    hbox:
#        label _("Enter")
#        text _("Advances dialogue and activates the interface.")
#
#    hbox:
#        label _("Space")
#        text _("Advances dialogue without selecting choices.")
#
#    hbox:
#        label _("Arrow Keys")
#        text _("Navigate the interface.")
#
#    hbox:
#        label _("Escape")
#        text _("Accesses the game menu.")
#
#    hbox:
#        label _("Ctrl")
#        text _("Skips dialogue while held down.")
#
#    hbox:
#        label _("Tab")
#        text _("Toggles dialogue skipping.")
#
#    hbox:
#        label _("Page Up")
#        text _("Rolls back to earlier dialogue.")
#
#    hbox:
#        label _("Page Down")
#        text _("Rolls forward to later dialogue.")
#
#    hbox:
#        label "H"
#        text _("Hides the user interface.")
#
#    hbox:
#        label "S"
#        text _("Takes a screenshot.")
#
#    hbox:
#        label "V"
#        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")
#
#
#screen mouse_help():
#
#    hbox:
#        label _("Left Click")
#        text _("Advances dialogue and activates the interface.")
#
#    hbox:
#        label _("Middle Click")
#        text _("Hides the user interface.")
#
#    hbox:
#        label _("Right Click")
#        text _("Accesses the game menu.")
#
#    hbox:
#        label _("Mouse Wheel Up\nClick Rollback Side")
#        text _("Rolls back to earlier dialogue.")
#
#    hbox:
#        label _("Mouse Wheel Down")
#        text _("Rolls forward to later dialogue.")
#
#
#screen gamepad_help():
#
#    hbox:
#        label _("Right Trigger\nA/Bottom Button")
#        text _("Advance dialogue and activates the interface.")
#
#    hbox:
#        label ("Left Trigger\nLeft Shoulder")
#        text _("Roll back to earlier dialogue.")
#
#    hbox:
#        label _("Right Shoulder")
#        text _("Roll forward to later dialogue.")
#
#    hbox:
#        label _("D-Pad, Sticks")
#        text _("Navigate the interface.")
#
#    hbox:
#        label _("Start, Guide")
#        text _("Access the game menu.")
#
#    hbox:
#        label _("Y/Top Button")
#        text _("Hides the user interface.")
#
#    textbutton _("Calibrate") action GamepadCalibrate()
#
#
#style help_button is gui_button
#style help_button_text is gui_button_text
#style help_label is gui_label
#style help_label_text is gui_label_text
#style help_text is gui_text
#
#style help_button:
#    properties gui.button_properties("help_button")
#    xmargin 8
#
#style help_button_text:
#    properties gui.button_text_properties("help_button")
#
#style help_label:
#    xsize 250
#    right_padding 20
#
#style help_label_text:
#    size gui.text_size
#    xalign 1.0
#    text_align 1.0



################################################################################
## Additional screens
################################################################################

screen name_input(message, ok_action):
    ## Ensure other screens do not get input while this screen is displayed.
    modal True
    zorder 200
    style_prefix "confirm"

    default inv = VariableInputValue("player")

    add "gui/overlay/confirm.png"
    if renpy.mobile:
        key "K_RETURN" action [inv.Disable(), Play("sound", gui.activate_sound), ok_action]
    else:
        key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    if renpy.mobile:
        button:
            xysize (1.0, 1.0)
            action [inv.Disable(), Function(FinishEnterName)]
    frame:
        if renpy.mobile:
            yalign 0.0
            yoffset 10

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            fixed:
                fit_first True
                yminimum 10

                xalign 0.5
                input default "" value VariableInputValue("player") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
                if renpy.mobile:
                    button:
                        action inv.Enable()
                        xysize (get_variable_size(280, 400, gui.text_scale), 90)
                        align (0.5, 0.5)

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("OK") action ok_action

screen dialog(message, ok_action):
    ## Ensure other screens do not get input while this screen is displayed.
    modal True
    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        has vbox
        xalign .5
        yalign .5
        spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat

## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## http://www.renpy.org/doc/html/screen_special.html#confirm
screen confirm(message, yes_action, no_action):
    ## Ensure other screens do not get input while this screen is displayed.
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        has vbox
        xalign .5
        yalign .5
        spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    #key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound (gui.hover_sound if not renpy.mobile else None)
    activate_sound gui.activate_sound

style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator
screen fake_skip_indicator():
    use skip_indicator

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    if not renpy.mobile:
        frame:
            has hbox
            spacing 6

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size get_variable_size(gui.notify_text_size, gui.max_notify_text_size, gui.text_scale)

style skip_triangle:
    # We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    # glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size gui.notify_text_size

## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## http://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")

screen choose_language():
    default local_lang = _preferences.language
    default chosen_lang = _preferences.language

    modal True
    style_prefix "radio"

    add "gui/overlay/confirm.png"

    frame:
        style "confirm_frame"

        vbox:
            xalign .5
            yalign .5
            xsize 760
            spacing 30

            label renpy.translate_string(_("{#in language font}Please select a language"), local_lang):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign .5
                for tran in translations:
                    vbox:
                        for tlid, tlname in tran:
                            textbutton tlname:
                                xalign .5
                                action SetScreenVariable("chosen_lang", tlid)
                                hovered SetScreenVariable("local_lang", tlid)
                                unhovered SetScreenVariable("local_lang", chosen_lang)

            $ lang_name = renpy.translate_string("{#language name and font}", local_lang)
            
            hbox:
                xalign 0.5
                spacing 100

                textbutton renpy.translate_string(_("{#in language font}Select"), local_lang):
                    style "confirm_button"
                    action [Language(chosen_lang), SetField(persistent, "has_chosen_language", True), Return()]

translate None strings:
    old "{#language name and font}"
    new "English"

label choose_language:
    call screen choose_language
    return