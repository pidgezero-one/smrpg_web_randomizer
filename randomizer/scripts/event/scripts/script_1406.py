# pylint: disable=C0301

"""E1406_MARIOS_PAD_OPEN_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7042_0, ["EVENT_1406_ret_4"]),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(use_alternate=True, room_id=R016_MARIOS_PAD, mod_id=33),
        SetBit(TEMP_7042_0),
        Return(identifier="EVENT_1406_ret_4"),
    ]
)
