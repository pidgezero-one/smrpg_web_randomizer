# pylint: disable=C0301

"""E1407_MARIOS_PAD_CLOSE_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7042_0, ["EVENT_1407_ret_4"]),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(use_alternate=True, room_id=R016_MARIOS_PAD, mod_id=32),
        ClearBit(TEMP_7042_0),
        Return(identifier="EVENT_1407_ret_4"),
    ]
)
