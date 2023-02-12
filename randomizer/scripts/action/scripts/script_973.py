#A0973_ENDING_CREDITS_CASTLE_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(SLOW),
	SequenceLoopingOn(),
	Walk1StepNortheast(),
	ShiftNorthwestSteps(2),
	ShiftSouthwestSteps(2),
	ShiftSoutheastSteps(3),
	ShiftSoutheastPixels(8),
	ShiftNortheastSteps(5),
	Walk1StepNorthwest(),
	SetWalkingSpeed(VERY_FAST),
	ShiftSouthwestSteps(3),
	FaceNorthwest(),
	JumpToHeight(64),
	Pause(32),
	SequenceLoopingOff(),
	Return()
])
