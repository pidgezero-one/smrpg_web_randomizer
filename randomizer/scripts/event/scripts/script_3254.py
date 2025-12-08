# pylint: disable=C0301

"""E3254_SHIP_PUZZLE_HUB_ROOM_OPEN_TRAMPOLINE_PUZZLE_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_2, ["EVENT_3254_ret_4"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY,
            mod_id=2),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_2),
        Return(identifier="EVENT_3254_ret_4"),
    ]
)
