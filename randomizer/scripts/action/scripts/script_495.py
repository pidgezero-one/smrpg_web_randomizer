#A0495_FAST_SPINY

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetBit(TEMP_7043_1),
	ClearSolidityBits(cant_pass_walls=True),
	VisibilityOn(),
	SetSequenceSpeed(VERY_FAST),
	SetWalkingSpeed(FAST),
	ShiftSouthwestSteps(3),
	VisibilityOff(),
	ShiftToXYCoords(x=19, y=85),
	Pause(96),
	ClearBit(TEMP_7043_1),
	Return()
])
