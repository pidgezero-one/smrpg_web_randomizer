"""A0521_TOWER_BEETLE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(VERY_SLOW, identifier="ACTION_521_set_animation_speed_0"),
        WalkNorthwestPixels(6),
        Pause(30),
        WalkSouthwestPixels(6),
        Pause(20),
        WalkSoutheastPixels(6),
        Pause(40),
        WalkNortheastPixels(6),
        Pause(15),
        Jmp(["ACTION_521_set_animation_speed_0"]),
    ]
)
