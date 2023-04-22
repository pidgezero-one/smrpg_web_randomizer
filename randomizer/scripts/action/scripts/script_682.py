"""A0682_MUSHROOM_DERBY_UNKNOWN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
        SetSolidityBits(cant_walk_through=True),
        SetSolidityBits(bit_4=True),
        Pause(30),
        SetSequenceSpeed(NORMAL),
        FaceSouthwest(),
        SetWalkingSpeed(SLOW),
        WalkSouthwestSteps(20),
        FaceNortheast(),
        Pause(60),
        Jmp(["ACTION_656_set_object_memory_bits_0"]),
    ]
)
