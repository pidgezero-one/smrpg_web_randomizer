"""A0449_FACTORY_FOUR_SCREW_ROOM_GLUM_REAPER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShadowOff(),
        SequenceLoopingOn(),
        SetSequenceSpeed(NORMAL),
        WalkSoutheastSteps(8, identifier="ACTION_449_shift_southeast_steps_3"),
        Pause(24),
        WalkNorthwestSteps(8),
        Pause(24),
        Jmp(["ACTION_449_shift_southeast_steps_3"]),
    ]
)
