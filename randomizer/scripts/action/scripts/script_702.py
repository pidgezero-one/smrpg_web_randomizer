#A0702_TOWER_FIRST_STAIRCASE_BOSS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShiftSouthwestSteps(2),
	ShiftSouthwestPixels(8),
	ShiftSoutheastSteps(3),
	VisibilityOff(),
	Return()
])
