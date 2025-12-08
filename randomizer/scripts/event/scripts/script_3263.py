# pylint: disable=C0301

"""E3263_SHIP_LOWER_FIRST_TRAMPOLINE_ROOM_OPEN_EXIT_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3263_ret_4"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE,
            mod_id=0),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_0),
        Return(identifier="EVENT_3263_ret_4"),
    ]
)
