#A0138_CHANCELLOR

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
	SetSolidityBits(bit_4=True),
	SetWalkingSpeed(VERY_SLOW),
	SetSequenceSpeed(FAST),
	ShiftNorthwestPixels(8),
	FaceSouthwest(),
	Pause(20, identifier="ACTION_138_pause_6"),
	Walk1StepSoutheast(),
	FaceSouthwest(),
	Pause(20),
	Walk1StepNorthwest(),
	FaceSouthwest(),
	Jmp(["ACTION_138_pause_6"])
])
