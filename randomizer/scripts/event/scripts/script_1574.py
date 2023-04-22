# pylint: disable=C0301

"""E1574_MIDAS_RIVER_BARREL_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_1574_ret_11"]),
        ClearBit(TEMP_7044_3),
        SetBit(TEMP_7043_0),
        Inc(SECONDARY_TEMP_7024),
        JmpIfVarEqualsConst(
            SECONDARY_TEMP_7024, 1, ["EVENT_1574_jmp_if_var_not_equals_const_6"]
        ),
        RunBackgroundEvent(
            event_id=E1586_MIDAS_RIVER_BARREL_FISH_MOVEMENT,
            return_on_level_exit=True,
            bit_6=True,
        ),
        JmpIfVarNotEqualsConst(
            SECONDARY_TEMP_7024,
            2,
            ["EVENT_1574_set_short_8"],
            identifier="EVENT_1574_jmp_if_var_not_equals_const_6",
        ),
        SpeedUpMusicTempoBy(duration=255, change=24),
        SetVarToConst(X_COORD_2, 6, identifier="EVENT_1574_set_short_8"),
        SetVarToConst(Y_COORD_2, 29),
        JmpToEvent(E1573_MIDAS_RIVER_BARREL_SUBROUTINE),
        Return(identifier="EVENT_1574_ret_11"),
    ]
)
