# This file contains the content warning popup screen used in the mobile version of DDLC.

# The logic for displaying the content warning is handled in `content_warning_ren.py` in the `py` directory.
# To show a content warning, call the `show_content_warning(warning_text)` function.

default persistent.enable_content_warnings = False
default cw_prev_volume = preferences.get_mixer('music')

image cw_darken:
    Solid("#000")
    alpha 0.8

image cw_warning_icon = "wip/gui/cwicon.png"

screen content_warning_popup(warning_text):
    modal True
    zorder 200
    style_prefix "cw_popup"

    default cw_screen_shown = False

    frame at cw_fade:
        background "cw_darken"

    frame at cw_popup_fade:
        padding (50, 30)
        xalign 0.5
        yalign 0.5
        
        has vbox
        xminimum 500
        ymaximum 1.0
        spacing 20

        add "cw_warning_icon" xalign 0.5 zoom 0.3

        text "[warning_text!t]"
        
        textbutton _("OK"):
            sensitive cw_screen_shown
            action [Function(cw_restore_volume), Hide()]

    timer 3.0 action SetLocalVariable("cw_screen_shown", True)

style cw_popup_text is default:
    xalign 0.5
    outlines []
    color "#000"
    size get_variable_size(24, 32, 1.0)
    textalign 0.5

style cw_popup_frame:
    background Frame(Transform("wip/gui/cw_frame.png", zoom=1.0), 30, 30) 

style cw_popup_button is confirm_button:
    xalign 0.5
style cw_popup_button_text is confirm_button_text     

transform cw_fade:
    on show:
        alpha 0.0
        linear 0.5 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.5 alpha 0.0

transform cw_popup_fade:
    subpixel True
    on show:
        alpha 0.0
        yoffset 40
        parallel:
            easein_quad 0.4 alpha 1.0
        parallel:
            easein_quad 1.2 yoffset 0
    on hide:
        parallel:
            easeout_quad 0.4 alpha 0.0
        parallel:
            easeout_quad 1.2 yoffset 40