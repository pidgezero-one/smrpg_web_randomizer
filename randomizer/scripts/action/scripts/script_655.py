#A0655_BOOSTER_HILL_LAYER_2

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(NORMAL),
	StartLoopNTimes(199),
	ShiftWestPixels(1),
	Pause(20),
	EndLoop(),
	StartLoopNTimes(99),
	ShiftWestPixels(1),
	Pause(20),
	EndLoop(),
	SetBit(TEMP_7043_6),
	StartLoopNTimes(25),
	ShiftWestPixels(1),
	Pause(20),
	EndLoop(),
	SetBit(TEMP_7043_4),
	Return()
])
