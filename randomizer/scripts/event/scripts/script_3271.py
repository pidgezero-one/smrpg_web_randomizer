# pylint: disable=C0301

"""E3271_SHIP_FINAL_SAVE_ROOM_OPEN_EXIT_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3271_ret_4"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT,
            mod_id=0,
        ),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_0),
        Return(identifier="EVENT_3271_ret_4"),
    ]
)
