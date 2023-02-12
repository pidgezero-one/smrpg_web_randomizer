#A0173_MIDAS_RIVER_WATERFALL_INTERACTION

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	TransferTo70167018701A(),
	ShadowOff(),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	StartLoopNTimes(3),
	VisibilityOff(),
	Pause(1),
	VisibilityOn(),
	Pause(1),
	EndLoop(),
	Jmp(["ACTION_163_set_700C_to_current_level_0"])
])
