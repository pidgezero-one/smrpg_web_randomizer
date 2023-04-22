"""A0500_MUSHROOM_DERBY_UNKNOWN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Db(bytearray(b" \x03"), identifier="ACTION_500_db_0"),
        Db(bytearray(b"$ \x00\xf0\xff")),
        Pause(1, identifier="ACTION_500_pause_2"),
        Jmp(["ACTION_500_pause_2"]),
    ]
)
