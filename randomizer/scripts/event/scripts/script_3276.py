# pylint: disable=C0301

"""E3276_SHIP_BIG_WATER_ROOM_OPEN_UPPER_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3276_ret_4"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R027_SUNKEN_SHIP_POSTKC_AREA_13_LARGE_UNDERWATER_ROOM_WITH_A_BLOOBER,
            mod_id=0),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_0),
        Return(identifier="EVENT_3276_ret_4"),
    ]
)
