#A0596_MIDAS_BARREL_LEFT_LANE_TO_RIGHT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetAllSpeeds(FAST),
	ShiftSouthwestSteps(11),
	SetBit(TEMP_7044_5),
	ShiftSouthwestSteps(2),
	ClearBit(TEMP_7044_5),
	SetBit(TEMP_7044_7),
	Pause(2),
	Walk1StepSoutheast(),
	Walk1StepSoutheast(),
	Walk1StepSouthwest(identifier="ACTION_596_walk_1_step_southwest_9"),
	Jmp(["ACTION_596_walk_1_step_southwest_9"])
])
