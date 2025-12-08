# pylint: disable=C0301

"""E3279_SHIP_OPEN_DOOR_IN_FINAL_BOSS_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3279_ret_4"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
            mod_id=0),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_0),
        Return(identifier="EVENT_3279_ret_4"),
    ]
)
