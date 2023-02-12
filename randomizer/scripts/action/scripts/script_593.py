#A0593_MIDAS_BARREL_AREA_MOVE_SOUTHWEST_REPEATEDLY

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FixedFCoordOn(),
	SetAllSpeeds(FAST),
	Walk1StepSouthwest(identifier="ACTION_593_walk_1_step_southwest_2"),
	Jmp(["ACTION_593_walk_1_step_southwest_2"])
])
