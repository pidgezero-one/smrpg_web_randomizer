"""A0696_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_1"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        Db(bytearray(b"\xfd\x12")),
        FloatingOff(),
        ClearSolidityBits(cant_pass_walls=True),
        TransferToXYZF(x=16, y=77, z=0, direction=EAST),
        WalkEastPixels(16),
        FaceNortheast(),
        VisibilityOn(),
        SetWalkingSpeed(SLOW),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        WalkNortheastSteps(4),
        FloatingOn(),
        SetSolidityBits(cant_pass_walls=True),
        JumpToHeight(108),
        Walk1StepNortheast(),
        FloatingOff(),
        ClearSolidityBits(cant_pass_walls=True),
        WalkNortheastPixels(4),
        StartLoopNTimes(2),
        FloatingOff(),
        ClearSolidityBits(cant_pass_walls=True),
        Walk1StepNorthwest(),
        FloatingOn(),
        SetSolidityBits(cant_pass_walls=True),
        JumpToHeight(108),
        Walk1StepNorthwest(),
        EndLoop(),
        FloatingOff(),
        ClearSolidityBits(cant_pass_walls=True),
        WalkNorthwestPixels(4),
        WalkSouthwestSteps(5),
        VisibilityOff(),
        Db(bytearray(b"\xfd\xf2")),
        Return(),
    ]
)
