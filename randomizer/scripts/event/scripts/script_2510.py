# pylint: disable=C0301

"""E2510_STAR_HILL_1ST_ROOM_TOP_LEFT_FLOWER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_2510_ret_12"]),
        SetBit(TEMP_7043_1),
        PlaySound(sound=SO081_STAR, channel=6),
        Store01To0248(),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R158_STAR_HILL_AREA_02, mod_id=1
        ),
        Pause(1),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R158_STAR_HILL_AREA_02, mod_id=2
        ),
        Inc(TEMP_70AE),
        JmpIfVarEqualsConst(TEMP_70AE, 5, ["EVENT_2515_pause_0"]),
        Store00To0248(),
        Return(identifier="EVENT_2510_ret_12"),
    ]
)
