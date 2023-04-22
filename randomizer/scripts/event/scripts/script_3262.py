# pylint: disable=C0301

"""E3262_SHIP_PASSWORD_ROOM_OPEN_DOOR_TO_BOSS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3262_ret_6"]),
        Store02To0248(),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM,
            mod_id=32,
        ),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        SetBit(TEMP_7043_0),
        Store00To0248(),
        Return(identifier="EVENT_3262_ret_6"),
    ]
)
