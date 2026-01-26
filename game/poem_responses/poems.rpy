# Copyright 2019-2026 Azariel Del Carmen (bronya_rand). All rights reserved.
# This file contains the Ren'Py code for displaying poems in DDLC.

# For the Python code, see `poems_ren.py` in the `py` directory.

screen poem(poem):
    style_prefix "poem"

    fixed:

        frame:
            style "poem_paper"

            add poem.paper:
                subpixel True align (0.5, 0.5)

        frame:
            background None
            
            hbox:
                viewport id "poem_vp":
                    draggable True
                    mousewheel True

                    add poem

                vbar value YScrollValue("poem_vp")
        
    if not persistent.first_poem:
        add "gui/poem_dismiss.png" xpos 1050 ypos 590
    
    key ["repeat_K_UP", "K_UP"] action Scroll("poem_vp", "vertical decrease", 20)
    key ["repeat_K_DOWN", "K_DOWN"] action Scroll("poem_vp", "vertical increase", 20)

    on "show" action SetVariable("poem_last_author", poem.author)

style poem_vscrollbar:
    xsize 20
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True

style poem_paper:
    modal True
    align (0.5, 0.5)

style poem_fixed:
    align (0.5, 0.5)
    xsize 720

style poem_frame:
    padding (4, 35)

style poem_hbox:
    xfill True

style yuri_text:
    font "gui/font/y1.ttf"
    size 32
    color "#000"
    outlines []

style yuri_text_3:
    font "gui/font/y3.ttf"
    size 18
    color "#000"
    outlines []
    kerning -8
    justify True

style natsuki_text:
    font "gui/font/n1.ttf"
    size 28
    color "#000"
    outlines []
    line_leading 1

style sayori_text:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []

style monika_text:
    font "gui/font/m1.ttf"
    size 46
    color "#000"
    outlines []

default poem_last_author = None

# Depreciation Warning
label showpoem(poem, **properties):
    python:
        text = "This feature is now depreciated. Please use " + ("'$ poem_db.show_poem(\"%s\", %s)'" % (poem, ", ".join("%s=%s" % (k, v) for k, v in properties.items())) if properties else "'$ poem_db.show_poem(\"%s\")'" % poem) + " instead.\nRefer to {u}poem_responses/py/poems_ren.py{/u} for more information."
    $ renpy.notify(text)
    return