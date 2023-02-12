#A0684_MUSHROOM_DERBY_UNKNOWN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
	SetSolidityBits(cant_walk_through=True),
	SetSolidityBits(bit_4=True),
	SetSequenceSpeed(NORMAL),
	SetWalkingSpeed(SLOW),
	ShiftNorthwestSteps(2),
	ShiftSouthwestSteps(2),
	ShiftSouthwestPixels(8),
	FaceSoutheast(),
	SetSequenceSpeed(SLOW),
	Return()
])
