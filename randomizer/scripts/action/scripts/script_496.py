#A0496_MUSHROOM_DERBY_REFEREE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(NORMAL),
	SetWalkingSpeed(SLOW),
	ShiftNorthwestSteps(1),
	ShiftSouthwestSteps(2),
	ShiftSouthwestPixels(8),
	FaceSoutheast(),
	SetSequenceSpeed(SLOW),
	Return()
])
