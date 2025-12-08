# pylint: disable=C0301

"""E3264_SHIP_LOWER_FIRST_DRYBONES_ROOM_OPEN_UPPER_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3264_ret_4"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R180_SUNKEN_SHIP_POSTKC_AREA_02_SMALL_2LEVEL_ROOM,
            mod_id=0),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_0),
        Return(identifier="EVENT_3264_ret_4"),
    ]
)
