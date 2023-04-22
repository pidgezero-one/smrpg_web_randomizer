# pylint: disable=C0301

"""E1918_ABYSS_BIG_CONVEYOR_CHECKPOINT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_3, ["EVENT_1918_ret_7"]),
        SetBit(TEMP_7043_3),
        SetVarToConst(TEMP_7026, 4),
        ClearBit(TEMP_7043_0),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        ClearBit(TEMP_7043_4),
        Return(identifier="EVENT_1918_ret_7"),
    ]
)
