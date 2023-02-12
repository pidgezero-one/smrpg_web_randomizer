#A0737_TOWER_EARLY_CIRCLING_BOMB

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequenceLoopingOn(identifier="ACTION_737_sequence_looping_on_0"),
	SetWalkingSpeed(SLOW),
	ShiftSoutheastSteps(2),
	Walk1StepNortheast(),
	ShiftNorthwestSteps(2),
	Walk1StepSouthwest(),
	Jmp(["ACTION_737_sequence_looping_on_0"])
])
