#A0650_BLUE_CLOUD_MOVEMENT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	StartLoopNTimes(2),
	ShiftZUpPixels(4),
	ShiftZDownPixels(4),
	ShiftZUpPixels(4),
	ShiftZDownPixels(4),
	EndLoop(),
	Return()
])
