"""A0477_BANDITS_WAY_1ST_PLATFORMS_STATIC"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Db(bytearray(b" \x00")),
        Pause(1, identifier="ACTION_477_pause_1"),
        Jmp(["ACTION_477_pause_1"]),
    ]
)
