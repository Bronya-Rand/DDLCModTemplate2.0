from pypresence import Presence
import time
import threading
import renpy


class DiscordRPC:
    def __init__(self, client_id):
        ## DO NOT TOUCH THIS
        self.client_id = str(client_id)

        ## You may touch this. All values MUST be strings.

        # Details indicates what the player is doing ATM
        # Example: In Main Menu
        self.details = renpy.version

        # State indicates additional information to details
        # Example: Browsing Settings
        self.state = "Monika Is Watching You Code"

        # The previous state the RPC was in
        self.prev_state = None

        # Defines the largest image to use in rich presence as the
        # main icon.
        self.large_img = "ddlcmodtemplatelogo"

        # Defines the text when a user hovers on the large icon in
        # a players' status.
        # Example: DDLC Mod Template
        self.large_txt = renpy.config.name  # Uses the name of the mod defined in-game.

        # Defines the smallest image to use in rich presence as the
        # secondary icon.
        self.small_img = "test"
        # Defines the text when a user hovers on the small icon in
        # a players' status.
        self.small_txt = renpy.config.version  # Uses the version name of the mod

        ## DO NOT TOUCH THIS EITHER
        self.start_time = time.time()
        self.rpc = Presence(self.client_id)
        self.rpc.connect()
        self.rpc_thread = threading.Thread(target=self.rpc_thread_main, daemon=True)
        self.rpc_thread.start()

    def rpc_thread_main(self):
        self.update_info()
        while True:  # The presence will stay on as long as the program is running
            # We save the previous status if the player returns back to what we are doing
            if self.prev_state is None:
                self.prev_state = self.state

            # These default checks sets up different statuses per menu accessed.
            if renpy.display.screen.get_screen("main_menu"):
                self.update_state("In the Main Menu")
            elif renpy.display.screen.get_screen("navigation"):
                self.update_state("In the Start Menu")
            elif renpy.display.screen.get_screen("preferences"):
                self.update_state("In the Settings Menu")
            elif renpy.display.screen.get_screen("load"):
                self.update_state("In the Load Menu")
            elif renpy.display.screen.get_screen("save"):
                self.update_state("In the Save Menu")
            elif renpy.display.screen.get_screen("history"):
                self.update_state("In the History Menu")
            elif renpy.display.screen.get_screen("extras"):
                self.update_state("In the Extras Menu")
            elif renpy.display.screen.get_screen("gallery"):
                self.update_state("In the Gallery Menu")
            elif renpy.display.screen.get_screen("preview"):
                self.update_state("Previewing a Gallery Image")
            elif renpy.display.screen.get_screen("achievements"):
                self.update_state("In the Awards Menu")
            else:
                self.update_state(self.prev_state)
                self.prev_state = None

                time.sleep(1)

        self.prev_state = None
        self.rpc.close()
        self.rpc_thread.stop()

    ## DO NOT TOUCH THESE FUNCTIONS
    def update_state(self, state):
        self.state = str(state)
        self.update_info()

    def update_details(self, details):
        self.details = str(details)
        self.update_info()

    def update_large_img_info(self, large_img=None, large_txt=None):
        if large_img is not None:
            self.large_img = str(large_img)
        if large_txt is not None:
            self.large_txt = str(large_txt)
        self.update_info()

    def update_small_img_info(self, small_img=None, small_txt=None):
        if small_img is not None:
            self.small_img = str(small_img)
        if small_txt is not None:
            self.small_txt = str(small_txt)
        self.update_info()

    def update_info(self):
        self.rpc.update(
            state=self.state,
            details=self.details,
            start=self.start_time,
            large_image=self.large_img,
            large_text=self.large_txt,
            small_image=self.small_img,
            small_text=self.small_txt,
        )
