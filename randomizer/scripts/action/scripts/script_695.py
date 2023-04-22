"""A0695_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_2"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        Db(bytearray(b"\xfd\x12")),
        FloatingOff(),
        ClearSolidityBits(cant_pass_walls=True),
        TransferToXYZF(x=13, y=71, z=16, direction=EAST),
        WalkEastPixels(16),
        FaceNortheast(),
        VisibilityOn(),
        SetWalkingSpeed(SLOW),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        WalkNortheastSteps(5),
        FloatingOn(),
        SetSolidityBits(cant_pass_walls=True),
        StartLoopNTimes(2),
        Walk1StepSoutheast(),
        FloatingOff(),
        ClearSolidityBits(cant_pass_walls=True),
        WalkSoutheastPixels(6),
        FloatingOn(),
        SetSolidityBits(cant_pass_walls=True),
        JumpToHeight(0),
        WalkSoutheastPixels(10),
        EndLoop(),
        Pause(16),
        Walk1StepSouthwest(),
        WalkSouthwestPixels(8),
        JumpToHeight(0),
        Walk1StepSouthwest(),
        FloatingOff(),
        ClearSolidityBits(cant_pass_walls=True),
        WalkSouthwestSteps(2),
        WalkSouthwestPixels(8),
        Db(bytearray(b"\xfd\xf2")),
        VisibilityOff(),
        Return(),
    ]
)
