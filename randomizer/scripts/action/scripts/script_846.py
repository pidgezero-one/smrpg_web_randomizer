"""A0846_VALLEY_TOP_PIPE_RIGHT_GECKO"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        WalkSouthwestSteps(4, identifier="ACTION_846_shift_southwest_steps_0"),
        Walk1StepNorthwest(),
        WalkNortheastSteps(4),
        Walk1StepSoutheast(),
        Jmp(["ACTION_846_shift_southwest_steps_0"]),
    ]
)
