
init python:
    import math
    import renpy.display.image as imgcore

    galleryList = []
    current_img = None

    class GalleryImage:

        def __init__(self, image, small_size=None, name=None, sprite=False):
            self.file = image
            
            if name:
                self.name = name
            else:
                self.name = image

            self.sprite = sprite

            if sprite:

                self.image = LiveComposite(
                    (1280, 720), (0, 0), 
                    "black", (0.2, 0), 
                    Transform(image, zoom=0.75*0.95)
                )

                if small_size:
                    self.small_size = small_size 
                else:               
                    self.small_size = LiveComposite(
                        (234, 132), (0, 0), 
                        "black", (0.2, 0), 
                        Transform(image, zoom=0.137)
                    )
            else:
                self.image = Transform(image, size=(1280, 680))

                if small_size:
                    self.small_size = small_size 
                else:     
                    self.small_size = Transform(image, size=(234, 132))

        def export(self):
            if renpy.android:
                try: os.mkdir(os.environ['ANDROID_PUBLIC'] + "/gallery")
                except: pass
            else:
                try: os.mkdir(config.basedir + "/gallery")
                except: pass

            if self.sprite:
                renpy.show_screen("dialog", message="Sprites cannot be exported to the gallery folder. Please try another image.", ok_action=Hide("dialog"))
            else:
                export = imgcore.get_registered_image(self.file).filename
                
                if renpy.android:
                    with open(os.path.join(os.environ['ANDROID_PUBLIC'], "gallery", self.file + os.path.splitext(export)[-1]).replace("\\", "/"), "wb") as p:
                        p.write(renpy.file(export).read())
                else:
                    with open(os.path.join(config.basedir, "gallery", self.file + os.path.splitext(export)[-1]).replace("\\", "/"), "wb") as p:
                        p.write(renpy.file(export).read())

                renpy.show_screen("dialog", message="Exported \"" + self.name + "\" to the gallery folder.", ok_action=Hide("dialog"))

    def next_image(back=False):
        global current_img

        index = 0
        while current_img != galleryList[index]:
            index = index + 1

        if back:
            current_img = galleryList[index-1]
        else:
            try: current_img = galleryList[index+1]
            except: current_img = galleryList[0]

    residential = GalleryImage("bg residential_day")
    galleryList.append(residential)

    s1a = GalleryImage("sayori 1", sprite=True)
    galleryList.append(s1a)

    m1a = GalleryImage("monika 1", sprite=True)
    galleryList.append(m1a)

    y1a = GalleryImage("yuri 1", sprite=True)
    galleryList.append(y1a)

    n1a = GalleryImage("natsuki 1", sprite=True)
    galleryList.append(n1a)

    m5a = GalleryImage("monika 5", name="Happy Monika", sprite=True)
    galleryList.append(m5a)

    cday = GalleryImage("bg class_day")
    galleryList.append(cday)

    clday = GalleryImage("bg club_day", name="Literature Club")
    galleryList.append(clday)

    co = GalleryImage("bg corridor")
    galleryList.append(co)

    h = GalleryImage("bg house")
    galleryList.append(h)
