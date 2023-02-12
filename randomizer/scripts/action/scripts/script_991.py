#A0991_SMITHY_COMPONENT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(FAST),
	ShiftNortheastPixels(2),
	SetWalkingSpeed(SLOW),
	ShiftSouthPixels(4),
	ShiftSouthwestPixels(6),
	Pause(12),
	SetWalkingSpeed(FAST),
	ShiftNortheastPixels(8),
	SetWalkingSpeed(SLOW),
	ShiftSouthwestPixels(4),
	SetWalkingSpeed(VERY_SLOW),
	ShiftNorthPixels(4),
	Return()
])
