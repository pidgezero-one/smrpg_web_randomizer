#A0062_SEWER_RAT_NEAR_PROGRESSION_PIPE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ObjectMemorySetBit(arg_1=0x0B, bits=[3], identifier="ACTION_62_object_memory_set_bit_0"),
	SetSequenceSpeed(FAST),
	ShiftSoutheastSteps(2),
	ShiftSouthwestSteps(2),
	ShiftNorthwestSteps(2),
	ShiftNortheastSteps(2),
	Jmp(["ACTION_62_object_memory_set_bit_0"])
])
