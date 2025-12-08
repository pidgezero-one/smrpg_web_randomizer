# pylint: disable=C0301

"""E3274_SHIP_UPPER_WHIRLPOOL_ROOM_OPEN_UNDERWATER_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3274_ret_4"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R188_SUNKEN_SHIP_POSTKC_AREA_11_WATER_ROOM_WITH_WHIRLPOOL,
            mod_id=0),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_0),
        Return(identifier="EVENT_3274_ret_4"),
    ]
)
