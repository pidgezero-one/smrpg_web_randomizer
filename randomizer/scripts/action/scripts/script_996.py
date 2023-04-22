"""A0996_KEEP_BRIDGE_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST, identifier="ACTION_996_set_animation_speed_0"),
        SetWalkingSpeed(SLOW),
        WalkSouthwestSteps(5),
        WalkNorthwestSteps(1),
        WalkNortheastSteps(11),
        WalkSoutheastSteps(1),
        WalkSouthwestSteps(1),
        FaceNortheast(),
        FixedFCoordOn(),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(VERY_SLOW),
        WalkSouthwestSteps(2),
        FixedFCoordOff(),
        SetSequenceSpeed(VERY_FAST),
        SetWalkingSpeed(NORMAL),
        WalkSouthwestSteps(3),
        Jmp(["ACTION_996_set_animation_speed_0"]),
    ]
)
