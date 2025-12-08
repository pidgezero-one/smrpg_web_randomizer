# pylint: disable=C0301

"""E3261_SHIP_BARREL_PUZZLE_ROOM_OPEN_EXIT_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3261_ret_8"]),
        Set0158Bit7Offset(True),
        Set0158Bit7Offset(True),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R176_SUNKEN_SHIP_AREA_08_WSAVE_POINT_AND_GREEN_SWITCH_FOR_BARREL,
            mod_id=32),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_0),
        Clear0158Bit7Offset(True),
        Clear0158Bit7Offset(True),
        Return(identifier="EVENT_3261_ret_8"),
    ]
)
