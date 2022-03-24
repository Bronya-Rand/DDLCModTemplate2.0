## Copyright 2019-2022 Azariel Del Carmen (GanstaKingofSA). All rights reserved.

# extras_screen.rpy
# This file contains the screen code for the extras menu for more screen options
# (Achievements/Gallery)

screen extras():

    tag menu

    use game_menu(_("Extras")):

        fixed:
            
            vpgrid id "ext":

                rows 1
                cols 2
                    
                xalign 0.5
                yalign 0.4

                spacing 18

                frame:
                    xsize 180
                    ysize 160
                    vbox:
                        xalign 0.5
                        yalign 0.5
                        imagebutton:
                            idle Transform("mod_assets/mod_extra_images/gallery.png")
                            hover Text('Gallery', style="extras_text")
                            action ShowMenu("gallery")

                frame:
                    xsize 180
                    ysize 160

                    vbox:
                        xalign 0.5
                        yalign 0.5
                        imagebutton:
                            idle Transform("mod_assets/mod_extra_images/achievements.png")
                            hover Text('Awards', style="extras_text")
                            action ShowMenu("achievements")

                # frame:
                #     xsize 180
                #     ysize 160

                #     vbox:
                #         xalign 0.5
                #         yalign 0.5
                #         imagebutton:
                #             idle Transform("mod_assets/mod_extra_images/ost_player.png")
                #             hover Text('DDLC OST-Player', style="extras_text")
                #             action [ShowMenu("new_music_room"), Function(ost_start)]

            vbar value YScrollValue("ext") xalign 0.99 ysize 560

style extras_text:
    color "#000"
    outlines []
    size 20