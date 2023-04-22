# pylint: disable=C0301

"""E3699_NIMBUS_CASTLE_WEST_LOWER_HALL_MARIO_BLOWN_BY_FAN_BIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7043_0, ["EVENT_3584_ret_0"]),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_3584_ret_0"]),
        SetBit(TEMP_7043_1),
        SetSyncActionScript(MARIO, A0814_MARIO_BLOWN_BY_FAN),
        Return(),
    ]
)
