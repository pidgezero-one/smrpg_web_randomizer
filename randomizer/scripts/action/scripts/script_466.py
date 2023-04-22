"""A0466_MIDAS_RIVER_TUNNEL_LEAVE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOff(),
        SetWalkingSpeed(SLOW),
        Walk1StepSouth(identifier="ACTION_466_walk_1_step_south_2"),
        Jmp(["ACTION_466_walk_1_step_south_2"]),
    ]
)
