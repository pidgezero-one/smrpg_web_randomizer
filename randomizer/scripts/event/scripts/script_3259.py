# pylint: disable=C0301

"""E3259_SHIP_SHOP_ROOM_OPEN_UPPER_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3259_ret_4"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R169_SUNKEN_SHIP_AREA_07_PUZZLE_ROOM_PASSAGEWAY_BRANCH_ROOM_WSHAMAN,
            mod_id=0),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_0),
        Return(identifier="EVENT_3259_ret_4"),
    ]
)
