#A0584_SEASIDE_OCCUPIED_INNKEEPER_AFTER_SLEEP

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceNortheast(),
	SequenceLoopingOn(),
	SetSequenceSpeed(FAST),
	Pause(120),
	Pause(120),
	SetWalkingSpeed(FAST),
	SetWalkingSpeed(VERY_FAST),
	JumpToHeight(height=32, silent=True),
	ShiftNorthwestSteps(4),
	ShiftSouthwestSteps(2),
	VisibilityOff(),
	Return()
])
