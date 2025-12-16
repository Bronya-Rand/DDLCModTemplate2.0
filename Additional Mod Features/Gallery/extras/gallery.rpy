# Copyright 2019-2025 Azariel Del Carmen (bronya_rand). All rights reserved.
# This file contains the screen code for the Gallery Menu.
# The code is designed to work with Ren'Py 8 and uses the `_ren.py` approach for Python code.

# For the Python code, see `gallery_ren.py` in the `py` directory.
default persistent.unlocked_gallery_images = []
default persistent.full_image_view = False

screen gallery:
    tag menu

    python:
        gallery_img_count = gallery_db.get_image_count()
        gallery_imgs = gallery_db.get_images()

    use game_menu(_("Gallery")):
        fixed:
            vpgrid:
                id "gallery_list_vpgrid"
                rows math.ceil(gallery_img_count / 3.0)
                if gallery_img_count > 3:
                    cols 3
                else:
                    cols gallery_img_count

                spacing 25
                mousewheel True
                xalign 0.5
                yalign 0.5

                for (index, gi) in enumerate(gallery_imgs):
                    vbox:
                        if gi.is_unlocked():
                            imagebutton: 
                                idle gi.get_small_image()   
                                action [Function(gallery_db.set_image_index, index), ShowMenu("preview_gallery_image"), With(Dissolve(0.5))]
                            text gi.get_image_name():
                                xalign 0.5
                                color "#555"
                                outlines []
                                size 14
                        else:
                            imagebutton: 
                                idle "mod_assets/mod_extra_images/galleryLock.png"
                                action Show("dialog", message="This image is locked. Continue playing [config.name] to unlock this image.", ok_action=Hide("dialog"))
                            text "Locked": 
                                xalign 0.5
                                color "#999"
                                outlines []
                                size 14
            
            vbar value YScrollValue("gallery_list_vpgrid") xalign 0.99 ysize 560

screen preview_gallery_image():
    tag menu

    default gallery_zoom = 1.0
    default gallery_offsx = 0
    default gallery_offsy = 0
    default display_alt = False

    python:
        img_data = gallery_db.get_image()

        alt_img_data = None
        if display_alt and img_data.has_alt_images():
            alt_img_data = gallery_db.get_alt_image()

        yoffs = 0 if persistent.full_image_view else 40
    
    if img_data.get_image_background():
        add img_data.get_image_background()
    if not display_alt:
        add img_data.get_image() yoffset yoffs fit "cover" xsize config.screen_width ysize config.screen_height
    else:
        add alt_img_data.get_image() yoffset yoffs fit "cover" xsize config.screen_width ysize config.screen_height
    
    if not persistent.full_image_view:
        hbox:
            add Solid("#fcf") size(config.screen_width, 40)

        hbox:
            ypos 0.005
            xalign 0.5 
            text "[img_data.get_image_name() if not display_alt or not img_data.has_alt_images() else alt_img_data.get_image_name()]":
                color "#000"
                outlines[]
                size 24

        hbox:
            ypos 0.005
            xalign 0.98
            if img_data.get_image_artist():
                textbutton "?":
                    text_style "navigation_button_text"
                    action Show("dialog", message="Artist: " + img_data.get_image_artist() if not display_alt or not img_data.has_alt_images() else alt_img_data.get_image_artist(), ok_action=Hide("dialog"))

            textbutton "E":
                text_style "navigation_button_text"
                action Function(img_data.export_image)

            textbutton "X":
                text_style "navigation_button_text"
                action [ShowMenu("gallery"), Function(gallery_db.reset_navigation)]
        
        if len(img_data.get_image_description()) > 0:
            frame:
                style "default"
                xalign 0.5
                yalign 1.0
                xmaximum 1000  # Max width before wrapping
                xpadding 50    # Left and right padding within the frame
                ypadding 20
                background "#eee8"
                at Transform(yoffset=-20)

                text img_data.get_image_description():
                    xalign 0.5
                    text_align 0.5
                    size 18
                    color "#000"
                    outlines []

        textbutton "<":
            text_style "navigation_button_text"
            xalign 0.0
            yalign 0.5
            action [SetScreenVariable("display_alt", False), Function(gallery_db.prev_image)]

        textbutton ">":
            text_style "navigation_button_text"
            xalign 1.0
            yalign 0.5
            action [SetScreenVariable("display_alt", False), Function(gallery_db.next_image)]

        if img_data.has_alt_images():
            hbox:
                xalign 0.02
                yalign 0.0
                spacing 5

                textbutton "<": 
                    text_style "navigation_button_text"
                    action Function(gallery_db.prev_alt_image)
                textbutton "Alt":
                    text_style "navigation_button_text"
                    action SetScreenVariable("display_alt", not display_alt)
                textbutton ">": 
                    text_style "navigation_button_text"
                    action Function(gallery_db.next_alt_image)
    else:
        viewport:
            id "gallery_viewport"
            draggable True
            xmaximum config.screen_width
            ymaximum config.screen_height
            child_size (int(config.screen_width * gallery_zoom), int(config.screen_height * gallery_zoom))

            python:
                bg_displayable = Transform(
                    img_data.get_image_background(),
                    zoom=gallery_zoom,
                    xoffset=gallery_offsx,
                    yoffset=gallery_offsy
                ) if img_data.get_image_background() else Null()

                main_image_displayable = Transform(
                    img_data.get_image(),
                    zoom=gallery_zoom,
                    xoffset=gallery_offsx,
                    yoffset=gallery_offsy
                )
            
            add "black"
            add bg_displayable
            add main_image_displayable
        
        frame:
            background "#0008"
            padding (10, 10)
            xalign 0.01
            yalign 0.5

            vbox:
                spacing 10
                textbutton "Z+" action SetScreenVariable("gallery_zoom", gallery_zoom + 0.1)
                key "mousedown_4" action SetScreenVariable("gallery_zoom", gallery_zoom + 0.1)

                textbutton "Z-" action SetScreenVariable("gallery_zoom", max(1.0, gallery_zoom - 0.1))
                key "mousedown_5" action SetScreenVariable("gallery_zoom", max(1.0, gallery_zoom - 0.1))

                textbutton "Reset" action [SetScreenVariable("gallery_zoom", 1.0), SetScreenVariable("gallery_offsx", 0), SetScreenVariable("gallery_offsy", 0)]
                key "mousedown_2" action [SetScreenVariable("gallery_zoom", 1.0), SetScreenVariable("gallery_offsx", 0), SetScreenVariable("gallery_offsy", 0)]
    
    textbutton ("View Full Image" if not persistent.full_image_view else "Back") action [
        ToggleVariable("persistent.full_image_view"),
        SetScreenVariable("gallery_zoom", 1.0),
        SetScreenVariable("gallery_offsx", 0),
        SetScreenVariable("gallery_offsy", 0),
    ]:
        xalign 1.0
        yalign 1.0
        padding (10, 5)
        text_style "navigation_button_text"

    on "replaced" action With(Dissolve(0.5))
    