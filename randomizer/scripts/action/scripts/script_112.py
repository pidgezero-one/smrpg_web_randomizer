"""A0112_MK_HALL_TOAD"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST),
        VisibilityOff(),
        Pause(30, identifier="ACTION_112_pause_2"),
        ClearBit(TEMP_7043_1),
        VisibilityOn(),
        WalkSoutheastSteps(9),
        VisibilityOff(),
        Pause(150),
        SetBit(TEMP_7043_2),
        Pause(100),
        VisibilityOn(),
        WalkNorthwestSteps(9),
        VisibilityOff(),
        ClearBit(TEMP_7043_2),
        Pause(1, identifier="ACTION_112_pause_14"),
        JmpIfBitSet(TEMP_7043_1, ["ACTION_112_pause_2"]),
        Jmp(["ACTION_112_pause_14"]),
    ]
)
