# pylint: disable=C0301

"""E1915_ABYSS_BIG_CONVEYOR_CHECKPOINT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_1915_ret_7"]),
        SetBit(TEMP_7043_0),
        SetVarToConst(TEMP_7026, 1),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        ClearBit(TEMP_7043_3),
        ClearBit(TEMP_7043_4),
        Return(identifier="EVENT_1915_ret_7"),
    ]
)
