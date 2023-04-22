"""A0852_VALLEY_RIGHT_PIPE_2ND_GECKO_RUNNING"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOn(),
        SetWalkingSpeed(FAST),
        SetSequenceSpeed(FASTER),
        SequenceLoopingOn(),
        ResetProperties(),
        WalkNortheastSteps(5),
        Pause(16),
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(NORMAL),
        WalkNorthwestPixels(8),
        WalkSouthwestSteps(3, identifier="ACTION_852_shift_southwest_steps_10"),
        Walk1StepSoutheast(),
        WalkNortheastSteps(3),
        Walk1StepNorthwest(),
        Jmp(["ACTION_852_shift_southwest_steps_10"]),
    ]
)
