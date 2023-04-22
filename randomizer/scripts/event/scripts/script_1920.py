# pylint: disable=C0301

"""E1920_ABYSS_BIG_CONVEYOR_CHECKPOINT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_4, ["EVENT_1920_ret_7"]),
        SetBit(TEMP_7043_4),
        SetVarToConst(TEMP_7026, 5),
        ClearBit(TEMP_7043_0),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        ClearBit(TEMP_7043_3),
        Return(identifier="EVENT_1920_ret_7"),
    ]
)
