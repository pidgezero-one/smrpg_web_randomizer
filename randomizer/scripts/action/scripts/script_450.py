"""A0450_FACTORY_FOUR_SCREW_ROOM_GLUM_REAPER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShadowOff(),
        SequenceLoopingOn(),
        SetSequenceSpeed(NORMAL),
        WalkSoutheastSteps(5, identifier="ACTION_450_shift_southeast_steps_3"),
        Pause(16),
        WalkNorthwestSteps(5),
        Pause(16),
        Jmp(["ACTION_450_shift_southeast_steps_3"]),
    ]
)
