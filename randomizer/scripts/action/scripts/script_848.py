#A0848_VALLEY_RIGHT_PIPE_1ST_GECKO

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(SLOW, identifier="ACTION_848_set_animation_speed_0"),
	Walk1StepSoutheast(),
	ShiftNortheastSteps(4),
	Walk1StepNorthwest(),
	ShiftSouthwestSteps(4),
	Jmp(["ACTION_848_set_animation_speed_0"])
])
