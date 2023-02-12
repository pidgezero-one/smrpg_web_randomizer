#A0852_VALLEY_RIGHT_PIPE_2ND_GECKO_RUNNING

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOn(),
	SetWalkingSpeed(FAST),
	SetSequenceSpeed(FASTER),
	SequenceLoopingOn(),
	ResetProperties(),
	ShiftNortheastSteps(5),
	Pause(16),
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(NORMAL),
	ShiftNorthwestPixels(8),
	ShiftSouthwestSteps(3, identifier="ACTION_852_shift_southwest_steps_10"),
	Walk1StepSoutheast(),
	ShiftNortheastSteps(3),
	Walk1StepNorthwest(),
	Jmp(["ACTION_852_shift_southwest_steps_10"])
])
