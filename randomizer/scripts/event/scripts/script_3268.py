# pylint: disable=C0301

"""E3268_SHIP_OUTER_CLONE_ROOM_OPEN_LEFT_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3268_ret_6"]),
        Store02To0248(),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM,
            mod_id=32,
        ),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_0),
        Store00To0248(),
        Return(identifier="EVENT_3268_ret_6"),
    ]
)
