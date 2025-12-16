# This file contains the Python code for the Discord Rich Presence integration.
# This requires the pypresence library to be included in your mod's `python-packages` folder.

# Before starting, make a new application on Discord's Developer Portal:    
# https://discord.com/developers/applications
# Follow the comments inside of `set_defaults` in order to set up RPC to your liking.

## This import is not used when the game is running, but exists so IDEs reports
## one warning than multiple.
import renpy # type: ignore
from renpy import NoRollback # type: ignore
from game.definitions.py.core_ren import persistent

last_reported_status_data = {
    "state": "",
    "details": "",
    "large_image": "",
    "large_text": "",
    "small_image": "",
    "small_text": "",
}

"""renpy
init -950 python:
"""

from pypresence import Presence, DiscordError, DiscordNotFound, InvalidPipe
from copy import deepcopy
import time

class DiscordRPC(NoRollback):
    def __init__(self, client_id: str) -> None:
        """
        Initializes the DiscordRPC with the given client ID.

        :param client_id: The Discord application client ID.
        :type client_id: str
        """

        self.client_id = client_id
        self.rpc_connected = False
        self.rpc: Presence | None = None

        # Discord Status Data
        self.start: float = 0.0
        self.details: str = ""
        self.state: str = ""
        self.large_image: str = ""
        self.large_text: str = ""
        self.small_image: str = ""
        self.small_text: str = ""

        self.original_state: dict = {}

    def set_defaults(self) -> None:
        """
        Sets the default values for the Discord Rich Presence status.
        Modify these values to customize the default status.
        """

        # Details indicates what the player is doing in the mod.
        # Example: In Main Menu
        self.details = renpy.version()

        # State indicates additional information to details.
        # Example: Browsing Settings
        self.state = "Bronya... :o"

        # Sets the largest image to use in rich presence
        self.large_image = "ddlcmodtemplatelogo"

        # Sets the text when a user hovers on the large image
        self.large_text = renpy.config.name # Uses the name of the mod defined in-game.

        # Sets the smallest image to use in rich presence
        self.small_image = "test"
        
        # Sets the text when a user hovers on the small image
        self.small_text = renpy.config.version # Uses the version name of the mod

        self.original_state = self.__dict__()

    def initialize_rpc(self) -> None:
        """
        Initializes the Discord RPC connection.
        """
        if not persistent.enable_discord:
            return
        
        try:
            self.rpc = Presence(self.client_id)
        except (DiscordError, DiscordNotFound):
            renpy.exports.write_log("Discord client not found.")
            return
    
    def connect(self, reset: bool = False) -> None:
        """
        Connects to the Discord Rich Presence service.
        :param reset: Whether to reset the status data upon connection.
        :type reset: bool
        """

        if not persistent.enable_discord:
            return
        if self.rpc_connected:
            return # Already connected
        if self.rpc is None:
            self.initialize_rpc()
            if self.rpc is None:
                return
        
        if reset:
            self.reset()
            self.start = time.time()
        else:
            self.set(**self.__dict__())
        
        try:
            self.rpc.connect()
            self.rpc_connected = True
        except InvalidPipe:
            self.rpc = None
    
    def disconnect(self) -> None:
        """
        Disconnects from the Discord Rich Presence service.
        """

        if self.rpc is None:
            return
        self.rpc.close()
        self.rpc_connected = False

    def set(self, **kwargs) -> None:
        """
        Sets the Discord Rich Presence status.

        :param kwargs: Key-value pairs for the status data. 
        """
        if not persistent.enable_discord:
            return
        if self.rpc is None or not self.rpc_connected:
            return

        # Update the status data with provided keyword arguments.
        valid_keys = {
            "state", "details", "large_image", "large_text",
            "small_image", "small_text"
        }
        for key, value in kwargs.items():
            if key in valid_keys:
                setattr(self, key, value)

        updated_data = self.__dict__()
        self.rpc.update(**updated_data)
        self.record_to_rollback()

    def reset(self) -> None:
        """
        Resets the Discord Rich Presence status to the original state.
        """
        self.set(**self.original_state)

    def record_to_rollback(self) -> None:
        """
        Records the current status data for rollback purposes.
        """
        global last_reported_status_data
        last_reported_status_data = deepcopy(self.__dict__())

    def rollback_check(self) -> None:
        """
        Checks if the status data has changed and updates it if necessary.
        """

        global last_reported_status_data
        if not persistent.enable_discord:
            return
        if self.rpc is None or not self.rpc_connected:
            return
        
        current_data = self.__dict__()
        if current_data != last_reported_status_data:
            self.set(**last_reported_status_data)

    def on_load(self) -> None:
        """
        Updates the Discord Rich Presence status after loading a saved game.
        """

        global last_reported_status_data
        if not persistent.enable_discord:
            return
        if self.rpc is None or not self.rpc_connected:
            return
        
        self.set(**last_reported_status_data)

    def __dict__(self) -> dict:
        return {
            "state": self.state,
            "details": self.details,
            "large_image": self.large_image,
            "large_text": self.large_text,
            "small_image": self.small_image,
            "small_text": self.small_text,
            "start": self.start,
        }

# Place your Discord RPC token inside the ""'s
RPC = DiscordRPC("979471077187125248")
RPC.initialize_rpc()
RPC.connect(True)

renpy.config.quit_callbacks.append(RPC.disconnect)
renpy.config.after_load_callbacks.append(RPC.on_load)
renpy.config.interact_callbacks.append(RPC.rollback_check)
renpy.config.start_callbacks.append(RPC.reset)