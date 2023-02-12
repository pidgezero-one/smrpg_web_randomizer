#A0847_VALLEY_TOP_PIPE_MID_GECKO

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(SLOW, identifier="ACTION_847_set_animation_speed_0"),
	ShiftNorthwestSteps(3),
	Walk1StepSouthwest(),
	Walk1StepSoutheast(),
	Walk1StepNortheast(),
	ShiftSoutheastSteps(2),
	Jmp(["ACTION_847_set_animation_speed_0"])
])
