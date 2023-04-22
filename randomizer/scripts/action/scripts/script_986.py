"""A0986_DREAM_CUSHION_CHEF"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST, identifier="ACTION_986_set_animation_speed_0"),
        WalkNorthwestSteps(3),
        Pause(10),
        WalkSoutheastSteps(3),
        Pause(30),
        Jmp(["ACTION_986_set_animation_speed_0"]),
    ]
)
