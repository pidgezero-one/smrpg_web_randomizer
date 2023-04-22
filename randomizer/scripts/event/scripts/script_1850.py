# pylint: disable=C0301

"""E1850_CANNONBALL_ROOM_BOMB_2_CONTD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        MoveScriptToMainThread(),
        Db(bytearray(b"\xfdG")),
        RunEventAtReturn(E1848_CANNONBALL_ROOM_BOMB_2),
        Return(),
    ]
)
