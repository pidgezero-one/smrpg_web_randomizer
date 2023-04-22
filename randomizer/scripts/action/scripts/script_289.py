"""A0289_MARIO_DISMOUNT_YOSHI"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(SLOW),
        SetObjectMemoryBits(arg_1=0x0E, bits=[]),
        SetSolidityBits(cant_pass_walls=True),
        ClearBit(TEMP_7044_0),
        ClearBit(TEMP_7044_1),
        ClearBit(TEMP_7044_2),
        ClearBit(TEMP_7044_3),
        ClearBit(TEMP_7044_5),
        Pause(12),
        SetSequenceSpeed(SLOW),
        SetWalkingSpeed(NORMAL),
        SequenceLoopingOn(),
        SetSolidityBits(cant_walk_through=True),
        ClearSolidityBits(cant_pass_npcs=True),
        CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_700C),
        FaceEast7C(),
        Return(),
    ]
)
