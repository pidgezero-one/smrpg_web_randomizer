# pylint: disable=C0301

"""E1955_KEEP_COIN_GAME_ROOM_EXIT_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([JmpToEvent(E1956_KEEP_ENTER_BUTTON_GAME_ROOM)])
