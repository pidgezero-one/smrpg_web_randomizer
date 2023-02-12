#A0975_ENDING_CREDITS_CASTLE_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(SLOW),
	SequenceLoopingOn(),
	ShiftSoutheastSteps(9),
	ShiftSouthwestSteps(2),
	ShiftNorthwestSteps(4),
	SetWalkingSpeed(VERY_FAST),
	ShiftNortheastSteps(2),
	FaceNorthwest(),
	JumpToHeight(64),
	Pause(32),
	SequenceLoopingOff(),
	Return()
])
