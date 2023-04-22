"""A0170_MIDAS_BARRELS_WATER_SPLASH"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceSouthwest(),
        FixedFCoordOn(),
        SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
        SetPriority(3),
        SequenceLoopingOn(),
        AddConstToVar(Z_COORD_2, 2),
        Db(bytearray(b"\x9a")),
        SetWalkingSpeed(VERY_FAST),
        WalkEastPixels(4),
        SetObjectMemoryBits(arg_1=0x0E, bits=[3]),
        VisibilityOn(),
        Return(),
    ]
)
