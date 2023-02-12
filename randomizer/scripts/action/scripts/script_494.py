#A0494_FAST_SPINY

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetBit(TEMP_7043_2),
	ClearSolidityBits(cant_pass_walls=True),
	VisibilityOn(),
	SequenceLoopingOn(),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(FASTER),
	ShiftNorthwestSteps(5),
	ShiftNorthwestPixels(5),
	Pause(24),
	FaceNortheast(),
	Pause(8),
	ShiftSoutheastSteps(5),
	ShiftSoutheastPixels(5),
	VisibilityOff(),
	Pause(48),
	ClearBit(TEMP_7043_2),
	Return()
])
