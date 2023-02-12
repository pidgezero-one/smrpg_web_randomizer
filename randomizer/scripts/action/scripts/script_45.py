#A0045_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_ITEM_PATH

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOn(),
	Pause(117),
	JmpIfBitSet(MIDAS_RIVER_TUNNEL_4_PRIZE, ["ACTION_45_reset_properties_13"]),
	JumpToHeight(108),
	ShiftSouthwestSteps(2),
	SetBit(MIDAS_RIVER_TUNNEL_4_PRIZE),
	StartLoopNTimes(4),
	VisibilityOn(),
	Pause(2),
	VisibilityOff(),
	Pause(2),
	EndLoop(),
	Return(),
	ResetProperties(identifier="ACTION_45_reset_properties_13"),
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(FASTER),
	Walk1StepEast(),
	Walk1StepWest(),
	Jmp(["ACTION_45_reset_properties_13"])
])
