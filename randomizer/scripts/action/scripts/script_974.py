#A0974_ENDING_CREDITS_CASTLE_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(SLOW),
	ShiftSoutheastSteps(2),
	ShiftNortheastSteps(2),
	Walk1StepSoutheast(),
	SetWalkingSpeed(FAST),
	ShiftSoutheastSteps(2),
	ShiftSouthwestSteps(3),
	SetWalkingSpeed(SLOW),
	ShiftNorthwestSteps(5),
	ShiftNorthwestPixels(8),
	Walk1StepSouthwest(),
	ShiftSoutheastPixels(8),
	Pause(24),
	SequenceLoopingOn(),
	JumpToHeight(64),
	Pause(32),
	FaceNorthwest(),
	Pause(32),
	SequenceLoopingOff(),
	Return()
])
