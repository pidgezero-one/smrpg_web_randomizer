#A0990_SMITHY_COMPONENT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(FAST),
	ShiftNortheastPixels(2),
	ShiftSouthwestPixels(2),
	SetWalkingSpeed(SLOW),
	ShiftZDownPixels(2),
	SetWalkingSpeed(VERY_SLOW),
	ShiftZDownPixels(2),
	Pause(17),
	SetWalkingSpeed(FAST),
	ShiftZUpPixels(4),
	ShiftNortheastPixels(2),
	SetWalkingSpeed(NORMAL),
	ShiftSouthwestPixels(4),
	SetWalkingSpeed(SLOW),
	ShiftNortheastPixels(2),
	Return()
])
