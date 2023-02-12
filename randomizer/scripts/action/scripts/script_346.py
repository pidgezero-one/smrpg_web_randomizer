#A0346_SHIP_PUZZLE_AREA_DRY_BONES

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(VERY_SLOW, identifier="ACTION_346_set_animation_speed_0"),
	Walk1StepSoutheast(),
	ShiftNorthwestSteps(3),
	ShiftSoutheastSteps(2),
	Jmp(["ACTION_346_set_animation_speed_0"])
])
