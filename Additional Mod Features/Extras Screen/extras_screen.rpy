## Copyright 2019-2023 Azariel Del Carmen (GanstaKingofSA). All rights reserved.

# extras_screen.rpy
# This file contains the screen code for the extras menu for more screen options
# (Achievements/Gallery)

default enable_gallery = True
default enable_achievements = True

screen extras():
    tag menu
    style_prefix "extras"

    use game_menu(_("Extras")):

        fixed:
                
            vpgrid id "ext":

                rows 1
                cols 3
                        
                xalign 0.5
                yalign 0.4

                spacing 18

                if enable_gallery:
                    frame:
                        xsize 160
                        ysize 140

                        vbox:
                            xalign 0.5
                            yalign 0.5

                            imagebutton:
                                idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/gallery.png", (40, 75), Text("Gallery", style="extras_text"))
                                hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/gallery.png", (38, 73), Text("Gallery", style="extras_hover_text"))
                                action ShowMenu("gallery")

                if enable_achievements: 
                    frame:
                        xsize 160
                        ysize 140

                        vbox:
                            xalign 0.5
                            yalign 0.5
            
                            imagebutton:
                                idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/achievements.png", (40, 75), Text("Awards", style="extras_text"))
                                hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/achievements.png", (38, 73), Text("Awards", style="extras_hover_text"))
                                action ShowMenu("achievements")

                frame:
                    xsize 160
                    ysize 140

                    vbox:
                        xalign 0.5
                        yalign 0.5
            
                        imagebutton:
                            idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/about.png", (40, 75), Text("Credits", style="extras_text"))
                            hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/about.png", (38, 73), Text("Credits", style="extras_hover_text"))
                            action ShowMenu("about")

                ## Increase rows or cols count before commenting this out
                # frame:
                #     xsize 160
                #     ysize 140

                #     vbox:
                #         xalign 0.5
                #         yalign 0.5
        
                #         imagebutton:
                #             idle Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/ost_player.png", (40, 75), Text("DDLC OST-Player", style="extras_text"))
                #             hover Composite((150, 130), (50, 20), "mod_assets/mod_extra_images/ost_player.png", (38, 73), Text("DDLC OST-Player", style="extras_hover_text"))
                #             action [ShowMenu("new_music_room"), Function(ost_start)]

            vbar value YScrollValue("ext") xalign 0.99 ysize 560

style extras_text:
    color "#000"
    outlines []
    size 20

style extras_hover_text is extras_text:
    outlines [(2, "#cacaca", 0, 0), (2, "#cacaca", 2, 2)]

style extras_image_button:
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
