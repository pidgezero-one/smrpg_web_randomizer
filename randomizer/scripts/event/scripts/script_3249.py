# pylint: disable=C0301

"""E3249_SHIP_ENTRANCE_OPEN_LEFT_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_3249_ret_4"]),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R160_SUNKEN_SHIP_AREA_01, mod_id=1
        ),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_1),
        Return(identifier="EVENT_3249_ret_4"),
    ]
)
