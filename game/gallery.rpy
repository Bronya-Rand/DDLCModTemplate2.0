
init python:
    import math
    import renpy.display.image as imgcore

    galleryList = []
    current_img = None

    class GalleryImage:

        def __init__(self, image, small_size=None, name=None, sprite=False, watermark=False):
            #The image variable name in the game
            self.file = image
            #The human readable name of the image
            if name:
                self.name = name
            else:
                self.name = image
            #A condition to see if the image given is a sprite
            self.sprite = sprite

            if sprite:

                self.image = LiveComposite(
                    (1280, 720), (0, 0), 
                    "black", (0.2, 0), 
                    Transform(image, zoom=0.75*0.95)
                )

                if small_size:
                    #A descaled version of the main image
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
                    
            #A condition to see if we export a watermark version of the image
            self.watermark = watermark

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
                try: 
                    renpy.file(self.file)
                    export = self.file
                except:
                    export = imgcore.get_registered_image(self.file).filename
                
                if renpy.android:
                    with open(os.path.join(os.environ['ANDROID_PUBLIC'], "gallery", os.path.splitext(export)[0].split("/")[-1] + os.path.splitext(export)[-1]), "wb") as p:
                        p.write(renpy.file(export).read())
                else:
                    with open(os.path.join(config.basedir, "gallery", os.path.splitext(export)[0].split("/")[-1] + os.path.splitext(export)[-1]).replace("\\", "/"), "wb") as p:
                        if self.watermark:
                            p.write(renpy.file(os.path.splitext(export)[0] + "_watermark" + os.path.splitext(export)[-1]).read())
                        else:
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

    m1a = GalleryImage("monika 1", name="Monika", sprite=True)
    galleryList.append(m1a)

