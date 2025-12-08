# pylint: disable=C0301

"""E3273_SHIP_1ST_WATER_ROOM_OPEN_UNDERWATER_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_3273_ret_4"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R187_SUNKEN_SHIP_POSTKC_AREA_10_WATER_ROOM_WITH_FROG_COINS,
            mod_id=1),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_1),
        Return(identifier="EVENT_3273_ret_4"),
    ]
)
