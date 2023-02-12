#A0391_CAMERA_SHAKE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	StartLoopNTimes(7),
	SetWalkingSpeed(FASTEST),
	ShiftNorthPixels(4),
	ShiftSouthPixels(8),
	ShiftNorthPixels(4),
	EndLoop(),
	Return()
])
