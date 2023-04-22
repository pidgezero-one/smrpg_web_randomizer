"""A0538_RIGHT_GOOMBA_IN_MUSHROOM_WAY_2"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetBit(TEMP_7044_5),
        ClearSolidityBits(cant_pass_walls=True),
        SetWalkingSpeed(FAST),
        SetSequenceSpeed(VERY_FAST),
        WalkSoutheastSteps(7),
        SetWalkingSpeed(NORMAL),
        SetSequenceSpeed(FAST),
        WalkSoutheastSteps(1),
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(NORMAL),
        WalkSoutheastSteps(1),
        Pause(60),
        SetWalkingSpeed(NORMAL),
        SetSequenceSpeed(VERY_FAST),
        WalkNorthwestSteps(9),
        Pause(5),
        ClearBit(TEMP_7044_5),
        Return(),
    ]
)
