#A1010_KEEP_DARK_ROOM_INIT_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(FAST),
	ShiftNortheastPixels(8),
	ShiftNorthwestSteps(5),
	ShiftNorthwestPixels(8),
	ShiftSouthwestSteps(5),
	VisibilityOff(),
	Return()
])
