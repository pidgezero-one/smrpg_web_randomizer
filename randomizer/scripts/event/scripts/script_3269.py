# pylint: disable=C0301

"""E3269_SHIP_OUTER_CLONE_ROOM_OPEN_RIGHT_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_3269_ret_6"]),
        Store02To0248(),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM,
            mod_id=33,
        ),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_1),
        Store00To0248(),
        Return(identifier="EVENT_3269_ret_6"),
    ]
)
