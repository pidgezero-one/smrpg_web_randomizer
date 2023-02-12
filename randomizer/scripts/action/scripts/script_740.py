#A0740_TOWER_MID_CIRCLING_BOMB

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequenceLoopingOn(identifier="ACTION_740_sequence_looping_on_0"),
	SetWalkingSpeed(SLOW),
	Walk1StepSoutheast(),
	Walk1StepNortheast(),
	Walk1StepNorthwest(),
	Walk1StepSouthwest(),
	Jmp(["ACTION_740_sequence_looping_on_0"])
])
