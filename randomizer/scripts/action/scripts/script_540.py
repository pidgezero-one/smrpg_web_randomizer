"""A0540_JUMPING_GOOMBA_MUSHROOM_WAY_2"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetBit(TEMP_7044_4),
        ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
        SetSolidityBits(cant_pass_walls=True),
        SetAllSpeeds(NORMAL),
        SequenceLoopingOn(),
        JumpToHeight(144),
        WalkSouthwestSteps(3),
        Pause(60),
        FixedFCoordOn(),
        SetAllSpeeds(NORMAL),
        WalkNortheastSteps(3),
        ClearBit(TEMP_7044_4),
        Return(),
    ]
)
