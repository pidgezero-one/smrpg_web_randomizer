#A0040_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT_WATER_DROPLETS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	StartLoopNTimes(2),
	Pause(1, identifier="ACTION_40_pause_1"),
	JmpIfBitClear(TEMP_7043_1, ["ACTION_40_pause_1"]),
	SetVarToConst(X_COORD_2, 15104),
	SetVarToConst(Y_COORD_2, 3712),
	SetVarToConst(Z_COORD_2, 0),
	TransferTo70167018701A(),
	VisibilityOn(),
	SequenceLoopingOn(),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	Pause(15),
	VisibilityOff(),
	EndLoop(),
	Return()
])
