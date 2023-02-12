#A0743_TOWER_MID_CIRCLING_BOMB

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequenceLoopingOn(identifier="ACTION_743_sequence_looping_on_0"),
	SetWalkingSpeed(SLOW),
	Walk1StepNorthwest(),
	ShiftSouthwestSteps(3),
	Walk1StepSoutheast(),
	ShiftNortheastSteps(3),
	Jmp(["ACTION_743_sequence_looping_on_0"])
])
