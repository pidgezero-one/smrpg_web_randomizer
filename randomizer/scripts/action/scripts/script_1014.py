"""A1014_KEEP_DARK_ROOM_TROOPA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(VERY_FAST, identifier="ACTION_1014_set_animation_speed_0"),
        SetWalkingSpeed(FAST),
        WalkSoutheastSteps(5),
        WalkNortheastSteps(6),
        WalkSoutheastSteps(4),
        WalkSouthwestSteps(3),
        WalkNorthwestSteps(9),
        WalkNortheastSteps(3),
        WalkSoutheastSteps(10),
        WalkSouthwestSteps(6),
        WalkNorthwestSteps(10),
        BounceToXYWithHeight(x=17, y=27, height=2),
        Jmp(["ACTION_1014_set_animation_speed_0"]),
    ]
)
