# pylint: disable=C0301

"""E1363_CURTAIN_4"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        MoveScriptToBackgroundThread2(),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_1363_ret_6"]),
        SetBit(TEMP_7043_3),
        ClearBit(TEMP_7043_0),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        Return(identifier="EVENT_1363_ret_6"),
    ]
)
