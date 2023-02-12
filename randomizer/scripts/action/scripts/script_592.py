#A0592_MIDAS_BARREL_CAMERA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetAllSpeeds(FAST),
	Walk1StepSouthwest(identifier="ACTION_592_walk_1_step_southwest_1"),
	Jmp(["ACTION_592_walk_1_step_southwest_1"]),
	Return()
])
