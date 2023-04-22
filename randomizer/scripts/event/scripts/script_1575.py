# pylint: disable=C0301

"""E1575_MIDAS_RIVER_BARREL_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_1575_ret_4"]),
        ClearBit(TEMP_7043_7),
        SetBit(TEMP_7043_1),
        JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 4, ["EVENT_1575_db_5"]),
        Return(identifier="EVENT_1575_ret_4"),
        Db(bytearray(b"\xfd\x8d"), identifier="EVENT_1575_db_5"),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R068_MIDAS_RIVER_BARREL_JUMPING_RIVER, mod_id=2
        ),
        Return(),
    ]
)
