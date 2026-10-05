## Copyright 2019-2026 Azariel Del Carmen (bronya_rand). All rights reserved.
# gallery.rpy
# This file contains the screen and backend code for the Gallery Menu.

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
                rows int(math.ceil(gallery_img_count / 3.0))
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
        add img_data.get_image() yoffset yoffs xsize config.screen_width ysize config.screen_height
    else:
        add alt_img_data.get_image() yoffset yoffs xsize config.screen_width ysize config.screen_height
    
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
                    action Show("dialog", message="Artist: " + (img_data.get_image_artist() if not display_alt or not img_data.has_alt_images() else alt_img_data.get_image_artist()), ok_action=Hide("dialog"))

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

init -1 python:
    import os
    import math

    if not hasattr(renpy.store, "Composite"):
        Composite = getattr(renpy.store, "LiveComposite", renpy.display.layout.LiveComposite)

    class GalleryBase(object):
        def __init__(
            self,
            img,
            small_img=None,
            export_img_name=None,
            name=None,
            artist=None,
            description=None,
            bg=None,
            sprite=False,
            exportable=True,
            unlock_by_default=False,
        ):
            self.name = name if name else img
            self.artist = artist
            self.description = description

            if img in persistent.unlocked_gallery_images or unlock_by_default:
                if unlock_by_default and img not in persistent.unlocked_gallery_images:
                    persistent.unlocked_gallery_images.append(img)
                self.unlocked = True
            else:
                self.unlocked = False

            self.sprite = sprite
            self.exportable = exportable

            self.img_file = img
            self.img, self.small_img = self._setup_images(img, small_img, sprite, bg)
            self.bg = (
                renpy.store.Transform(
                    bg, size=(renpy.config.screen_width, renpy.config.screen_height)
                )
                if bg
                else None
            )
            self.export_name = export_img_name

        def _setup_images(self, img, small_img, sprite, bg):
            bg = bg if bg else "black"
            if sprite:
                full_img = renpy.store.Composite(
                    (renpy.config.screen_width, renpy.config.screen_height),
                    (0, 0),
                    bg,
                    (int(0.2 * renpy.config.screen_width / 1280.0), 0),
                    renpy.store.Transform(img, zoom=0.75 * 0.95),
                )
                display_img = small_img or renpy.store.Composite(
                    (234, 132),
                    (0, 0),
                    renpy.store.Transform(bg, size=(233, 131)),
                    (0, 0),
                    renpy.store.Transform(img, zoom=0.137),
                )
            else:
                full_img = renpy.store.Transform(
                    img,
                    size=(renpy.config.screen_width, renpy.config.screen_height),
                )
                display_img = small_img or renpy.store.Composite(
                    (234, 132),
                    (0, 0),
                    renpy.store.Transform(bg, size=(233, 131)),
                    (0, 0),
                    renpy.store.Transform(img, size=(234, 132)),
                )

            return full_img, display_img

        def unlock(self):
            self.unlocked = True
            if self.img not in persistent.unlocked_gallery_images:
                persistent.unlocked_gallery_images.append(self.img)

        def lock(self):
            self.unlocked = False
            if self.img in persistent.unlocked_gallery_images:
                persistent.unlocked_gallery_images.remove(self.img)

        def get_image(self):
            return self.img

        def get_image_name(self):
            return self.name

        def get_small_image(self):
            return self.small_img or "mod_assets/mod_extra_images/galleryLock.png"

        def get_image_artist(self):
            return self.artist

        def get_image_description(self):
            return self.description or ""

        def get_image_background(self):
            return self.bg

        def is_exportable(self):
            return self.exportable

        def is_unlocked(self):
            return self.unlocked

        def export_image(self):
            if not self.exportable:
                renpy.show_screen(
                    "dialog",
                    message="This image is not exportable.",
                    ok_action=renpy.store.Hide("dialog"),
                )
                return

            if self.sprite:
                renpy.show_screen(
                    "dialog",
                    message="Sprite images are not exportable.",
                    ok_action=renpy.store.Hide("dialog"),
                )
                return

            export_dir = None
            if renpy.android:
                android_public_dir = os.environ.get("ANDROID_PUBLIC_DIRECTORY")
                if not android_public_dir:
                    renpy.show_screen(
                        "dialog",
                        message="Unable to access Android public directory for exporting images.",
                        ok_action=renpy.store.Hide("dialog"),
                    )
                    return
                export_dir = os.path.join(android_public_dir, "gallery")
            else:
                export_dir = os.path.join(renpy.config.basedir, "gallery")

            if export_dir is None:
                renpy.show_screen(
                    "dialog",
                    message="Unable to determine export directory.",
                    ok_action=renpy.store.Hide("dialog"),
                )
                return

            if not os.path.exists(export_dir):
                try:
                    os.makedirs(export_dir)
                except (IOError, OSError):
                    pass

            try:
                renpy.open_file(self.img_file)
                renpy_img = self.img_file
            except (IOError, OSError):
                img_filename = self.img_file
                if not isinstance(img_filename, tuple):
                    img_filename = tuple(img_filename.split())
                img_obj = renpy.display.image.images.get(img_filename)
                renpy_img = img_obj.filename if img_obj else None

            if not renpy_img:
                renpy.show_screen(
                    "dialog",
                    message="Unable to locate image file for export.",
                    ok_action=renpy.store.Hide("dialog"),
                )
                return

            original_ext = os.path.splitext(renpy_img)[1]

            export_filename = None
            if self.export_name:
                if not os.path.splitext(self.export_name)[1]:
                    export_filename = "%s%s" % (self.export_name, original_ext)
                else:
                    export_filename = self.export_name
            else:
                export_filename = os.path.basename(renpy_img)

            if not export_filename:
                renpy.show_screen(
                    "dialog",
                    message="Unable to determine export filename.",
                    ok_action=renpy.store.Hide("dialog"),
                )
                return

            img_export_file = os.path.join(export_dir, export_filename)
            if os.path.exists(img_export_file):
                renpy.show_screen(
                    "dialog",
                    message="This image has already been exported.",
                    ok_action=renpy.store.Hide("dialog"),
                )
                return

            with open(img_export_file, "wb") as outfile:
                try:
                    outfile.write(renpy.open_file(renpy_img).read())
                except (IOError, OSError):
                    try:
                        outfile.write(
                            renpy.loader.load(renpy_img, directory="images").read()
                        )
                    except Exception as e:
                        renpy.show_screen(
                            "dialog",
                            message="Failed to export image: %s" % str(e),
                            ok_action=renpy.store.Hide("dialog"),
                        )
                        return

            renpy.show_screen(
                "dialog",
                message="Image exported to the 'gallery' folder in the base directory.",
                ok_action=renpy.store.Hide("dialog"),
            )


    class GalleryAltImage(GalleryBase):
        def __init__(
            self,
            img,
            small_img=None,
            export_img_name=None,
            name="",
            artist="",
            description="",
            bg=None,
            sprite=False,
            exportable=True,
            unlock_by_default=False,
        ):
            super(GalleryAltImage, self).__init__(
                img,
                small_img=small_img,
                export_img_name=export_img_name,
                name=name,
                artist=artist,
                description=description,
                bg=bg,
                sprite=sprite,
                exportable=exportable,
                unlock_by_default=unlock_by_default,
            )


    class GalleryImage(GalleryBase):
        def __init__(
            self,
            img,
            small_img=None,
            export_img_name=None,
            name="",
            artist="",
            description="",
            alts=None,
            bg=None,
            sprite=False,
            exportable=True,
            unlock_by_default=False,
        ):
            super(GalleryImage, self).__init__(
                img,
                small_img=small_img,
                export_img_name=export_img_name,
                name=name,
                artist=artist,
                description=description,
                bg=bg,
                sprite=sprite,
                exportable=exportable,
                unlock_by_default=unlock_by_default,
            )

            if type(alts) is list and all(isinstance(alt, GalleryAltImage) for alt in alts):
                self.alts = list(alts)
            else:
                self.alts = []

        def has_alt_images(self):
            return len(self.alts) > 0

        def unlock_alt_image(self, img_index):
            if 0 <= img_index < len(self.alts):
                self.alts[img_index].unlock()

        def unlock_all_alt_images(self):
            for alt in self.alts:
                alt.unlock()

        def lock_alt_image(self, img_index):
            if 0 <= img_index < len(self.alts):
                self.alts[img_index].lock()

        def lock_all_alt_images(self):
            for alt in self.alts:
                alt.lock()


    class GalleryDB(object):
        def __init__(self):
            self.images = []
            self.image_index = 0
            self.alt_index = 0

        def add_image(self, image):
            self.images.append(image)

        def set_image_index(self, index):
            if 0 <= index < len(self.images):
                self.image_index = index
                self.alt_index = 0

        def get_alt_image_index(self):
            return self.alt_index

        def set_alt_image_index(self, index):
            image = self.get_image()
            if 0 <= index < len(image.alts):
                self.alt_index = index

        def get_image(self):
            if len(self.images) == 0:
                raise IndexError("No gallery images available.")
            return self.images[self.image_index]

        def get_alt_image(self):
            image = self.get_image()
            if len(image.alts) == 0:
                raise IndexError("No alternative images available for this gallery image.")
            return image.alts[self.alt_index]

        def has_next_image(self):
            return len(self.images) > 0 and self.image_index < len(self.images) - 1

        def has_prev_image(self):
            return len(self.images) > 0 and self.image_index > 0

        def has_next_alt_image(self):
            try:
                image = self.get_image()
                return len(image.alts) > 0 and self.alt_index < len(image.alts) - 1
            except IndexError:
                return False

        def has_prev_alt_image(self):
            try:
                image = self.get_image()
                return len(image.alts) > 0 and self.alt_index > 0
            except IndexError:
                return False

        def _find_next_unlocked(self):
            if len(self.images) == 0:
                return None
            for i in range(self.image_index + 1, len(self.images)):
                if self.images[i].is_unlocked():
                    return i
            for i in range(0, self.image_index + 1):
                if self.images[i].is_unlocked():
                    return i
            return None

        def _find_prev_unlocked(self):
            if len(self.images) == 0:
                return None
            for i in range(self.image_index - 1, -1, -1):
                if self.images[i].is_unlocked():
                    return i
            for i in range(len(self.images) - 1, self.image_index - 1, -1):
                if self.images[i].is_unlocked():
                    return i
            return None

        def _find_next_alt_unlocked(self):
            try:
                image = self.get_image()
            except IndexError:
                return None
            if len(image.alts) == 0:
                return None
            for i in range(self.alt_index + 1, len(image.alts)):
                if image.alts[i].is_unlocked():
                    return i
            for i in range(0, self.alt_index + 1):
                if image.alts[i].is_unlocked():
                    return i
            return None

        def _find_prev_alt_unlocked(self):
            try:
                image = self.get_image()
            except IndexError:
                return None
            if len(image.alts) == 0:
                return None
            for i in range(self.alt_index - 1, -1, -1):
                if image.alts[i].is_unlocked():
                    return i
            for i in range(len(image.alts) - 1, self.alt_index - 1, -1):
                if image.alts[i].is_unlocked():
                    return i
            return None

        def next_image(self):
            next_index = self._find_next_unlocked()
            if next_index is not None:
                self.image_index = next_index
                self.alt_index = 0

        def prev_image(self):
            prev_index = self._find_prev_unlocked()
            if prev_index is not None:
                self.image_index = prev_index
                self.alt_index = 0

        def next_alt_image(self):
            next_index = self._find_next_alt_unlocked()
            if next_index is not None:
                self.alt_index = next_index

        def prev_alt_image(self):
            prev_index = self._find_prev_alt_unlocked()
            if prev_index is not None:
                self.alt_index = prev_index

        def reset_navigation(self):
            self.image_index = 0
            self.alt_index = 0

        def get_images(self):
            return self.images

        def get_image_count(self):
            return len(self.images)

    gallery_db = GalleryDB()

    residential = GalleryImage("bg residential_day", unlock_by_default=True)
    s1a = GalleryImage("sayori 1", sprite=True, unlock_by_default=True)
    m1a = GalleryImage("monika 1", name="Monika", artist="Satchely", sprite=True)

    n2a = GalleryAltImage("natsuki 2", sprite=True, unlock_by_default=True)
    n3a = GalleryAltImage("natsuki 3", sprite=True)
    n1a = GalleryImage("natsuki 1", sprite=True, unlock_by_default=True, alts=[n2a, n3a])

    gallery_db.add_image(residential)
    gallery_db.add_image(s1a)
    gallery_db.add_image(m1a)
    gallery_db.add_image(n1a)
