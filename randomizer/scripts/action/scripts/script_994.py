"""A0994_KEEP_BRIDGE_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(VERY_FAST, identifier="ACTION_994_set_animation_speed_0"),
        SetWalkingSpeed(NORMAL),
        WalkNortheastSteps(3),
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(SLOW),
        WalkNortheastSteps(2),
        WalkSoutheastSteps(1),
        WalkSouthwestSteps(3),
        FaceSoutheast(),
        FixedFCoordOn(),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(VERY_SLOW),
        WalkSouthwestSteps(2),
        FixedFCoordOff(),
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(SLOW),
        WalkSouthwestSteps(6),
        WalkNorthwestSteps(1),
        WalkNortheastSteps(6),
        Jmp(["ACTION_994_set_animation_speed_0"]),
    ]
)
