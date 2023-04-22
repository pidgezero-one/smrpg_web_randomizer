"""A0537_LEFT_GOOMBA_IN_MUSHROOM_WAY_2"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetBit(TEMP_7044_6),
        FaceSoutheast(),
        FixedFCoordOn(),
        SetWalkingSpeed(FAST),
        SetSequenceSpeed(VERY_FAST),
        WalkSouthwestSteps(1),
        Pause(25),
        FixedFCoordOff(),
        WalkSoutheastSteps(9),
        SetWalkingSpeed(NORMAL),
        SetSequenceSpeed(FAST),
        WalkSoutheastSteps(1),
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(NORMAL),
        WalkSoutheastSteps(1),
        Pause(60),
        SetWalkingSpeed(NORMAL),
        SetSequenceSpeed(VERY_FAST),
        WalkNorthwestSteps(11),
        WalkNortheastSteps(1),
        ClearBit(TEMP_7044_6),
        Return(),
    ]
)
