## script.rpy

# Este es el script principal que Ren'Py llama al iniciar
# la historia de tu mod! 

label start:

    # Esta rama configura el número anti-trampa para el juego despues del Acto 1.
    # Es recomendable dejar esto como está y utilizar lo siguiente para tu script:
    #   $ persistent.anticheat = renpy.random.randint(X, Y) 
    #   X - El número mínimo | Y - El número máximo
    $ anticheat = persistent.anticheat

    # Esta variable cambia el número de capítulo a 0 para usarlo en el mod.
    $ chapter = 0

    # Esta variable controla cuando el jugador puede pausar mientras juega.
    $ _dismiss_pause = config.developer

    ## Nombres de los personajes
    # Estas variables establecen los nombres de los personajes en el juego.
    # Para añadir un personaje, utiliza el siguiente ejempo a continuación: 
    #   $ mi_name = "Mike". 
    # No se te olvide añadir el personaje a 'definitions.rpy'!
    $ s_name = "???"
    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"

    # Esta variable controla cuando el menú rapido en la caja de texto esta activado.
    $ quick_menu = True

    # Esta variable controla cuando queramos dialogo normal o dialogo con glitches.
    # For glitched dialogue, use 'style.edited'.
    $ style.say_dialogue = style.normal

    # Esta variable controla cuando Sayori está muerta. Es recomendable dejarlo
    # como está.
    $ in_sayori_kill = None
    
    # Esta variable controla cuando el jugador puede saltarse dialogo o transiciones.
    $ allow_skipping = True
    $ config.allow_skipping = True

    ## La parte principal del código
    # Aqui es donde el código de tu script es llamado!
    # 'persistent.playthrough' controla el número de acto en el que el jugador está, ejemplo:(Acto 1, 2, 3, 4)
    if persistent.playthrough == 0:

        # Esta variable establece el numero de capitulo a X dependiendo del capitulo
        # que tu jugador está viviendo al momento.
        $ chapter = 0

        # Esta sentencia llama a la rama de tu script para ser reproducida.
        call ch0_main
        
        # Esta sentencia llama al minijuego del poema para ser reproducido.
        call poem

        ## Día 1
        $ chapter = 1
        call ch1_main

        # This call statement calls the poem sharing minigame to be played.
        call poemresponse_start
        call ch1_end

        call poem

        ## Day 2
        $ chapter = 2
        call ch2_main
        call poemresponse_start
        call ch2_end

        call poem

        ## Day 3
        $ chapter = 3
        call ch3_main
        call poemresponse_start
        call ch3_end

        ## Day 4
        $ chapter = 4
        call ch4_main

        # This python statement writes a file from within the game to the game folder
        # or to the Android/data/[modname]/files/game folder.
        python:
            if renpy.android and renpy.version_tuple == (6, 99, 12, 4, 2187):
                try: file(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png")
                except: open(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
            elif renpy.android:
                try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png")
                except: open(os.environ['ANDROID_PUBLIC'] + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())
            else:
                try: renpy.file(config.basedir + "/hxppy thxughts.png")
                except: open(config.basedir + "/hxppy thxughts.png", "wb").write(renpy.file("hxppy thxughts.png").read())

        ## Day 5
        $ chapter = 5
        call ch5_main

        # This call statement ends the game but doesn't play the credits.
        call endgame
        return

    elif persistent.playthrough == 1:
        $ chapter = 0
        call ch10_main
        
        # This jump statement jumps over to Act 2 from Act 1.
        jump playthrough2


    elif persistent.playthrough == 2:
        ## Day 1 - Act 2
        $ chapter = 0
        call ch20_main
        label playthrough2:
            call poem

            python:
                if renpy.android and renpy.version_tuple == (6, 99, 12, 4, 2187):
                    try: file(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt")
                    except: open(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())
                elif renpy.android:
                    try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt")
                    except: open(os.environ['ANDROID_PUBLIC'] + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())
                else:
                    try: renpy.file(config.basedir + "/CAN YOU HEAR ME.txt")
                    except: open(config.basedir + "/CAN YOU HEAR ME.txt", "wb").write(renpy.file("CAN YOU HEAR ME.txt").read())

            ## Day 2 - Act 2
            $ chapter = 1
            call ch21_main
            call poemresponse_start
            call ch21_end

            # This call statement calls the poem mini-game with no transition.
            call poem(False)

            python:
                if renpy.android and renpy.version_tuple == (6, 99, 12, 4, 2187):
                    try: file(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
                    except: open(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())
                elif renpy.android:
                    try: renpy.file(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
                    except: open(os.environ['ANDROID_PUBLIC'] + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())
                else:
                    try: renpy.file(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt")
                    except: open(config.basedir + "/iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt", "wb").write(renpy.file("iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii.txt").read())

            ## Day 3 - Act 2
            $ chapter = 2
            call ch22_main
            call poemresponse_start
            call ch22_end

            call poem(False)

            ## Day 4 - Act 2
            $ chapter = 3
            call ch23_main

            # This if statement calls either a special poem response game or play
            # as normal.
            if y_appeal >= 3:
                call poemresponse_start2
            else:
                call poemresponse_start

            # This if statement is leftover code from DDLC where if your game is
            # a demo that it ends the game fully.
            if persistent.demo:
                stop music fadeout 2.0
                scene black with dissolve_cg
                "End of demo"
                return

            call ch23_end
            return

    elif persistent.playthrough == 3:
        jump ch30_main

    elif persistent.playthrough == 4:
        ## Day 1 - Act 4
        $ chapter = 0
        call ch40_main
        jump credits

# This label is where the game 'ends' during Act 1.
label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return
