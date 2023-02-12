#A0685_MUSHROOM_DERBY_UNKNOWN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
	SetSolidityBits(cant_walk_through=True),
	SetSolidityBits(bit_4=True),
	SetSequenceSpeed(NORMAL),
	FaceSouthwest(),
	SetWalkingSpeed(SLOW),
	ShiftSouthwestSteps(20),
	ShiftSouthwestPixels(12),
	Walk1StepNorthwest(),
	FaceSoutheast(),
	SetSequenceSpeed(SLOW),
	ClearBit(TEMP_7043_3),
	Return()
])
