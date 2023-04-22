# pylint: disable=C0301

"""E3248_SHIP_ENTRANCE_OPEN_RIGHT_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3248_ret_4"]),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R160_SUNKEN_SHIP_AREA_01, mod_id=0
        ),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_0),
        Return(identifier="EVENT_3248_ret_4"),
    ]
)
