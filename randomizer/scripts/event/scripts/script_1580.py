# pylint: disable=C0301

"""E1580_MIDAS_RIVER_BARREL_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_6, ["EVENT_1580_ret_9"]),
        ClearBit(TEMP_7044_3),
        ClearBit(TEMP_7043_3),
        SetBit(TEMP_7043_6),
        JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 4, ["EVENT_1580_ret_9"]),
        RunBackgroundEvent(
            event_id=E1569_MIDAS_RIVER_BARREL_SUBROUTINE,
            return_on_level_exit=True,
            bit_6=True),
        SetVarToConst(X_COORD_2, 28),
        SetVarToConst(Y_COORD_2, 113),
        JmpToEvent(E1573_MIDAS_RIVER_BARREL_SUBROUTINE),
        Return(identifier="EVENT_1580_ret_9"),
    ]
)
