# pylint: disable=C0301

"""E3270_SHIP_ROOM_WITH_BOX_WALL_OPEN_RIGHT_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3270_ret_4"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R182_SUNKEN_SHIP_POSTKC_AREA_07_THREE_DRY_BONES,
            mod_id=0),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_0),
        Return(identifier="EVENT_3270_ret_4"),
    ]
)
