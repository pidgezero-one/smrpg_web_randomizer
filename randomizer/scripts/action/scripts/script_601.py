#A0601_MIDAS_RIVER_BOTTOM_LEFT_TUNNEL_PLAYER_OUTER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ClearSolidityBits(cant_pass_walls=True),
	ClearBit(TEMP_7043_0),
	SetVarToConst(X_COORD_2, 14080),
	SetVarToConst(Y_COORD_2, 4480),
	SetVarToConst(Z_COORD_2, 0),
	TransferTo70167018701A(),
	SetAllSpeeds(NORMAL),
	VisibilityOn(),
	ShiftNortheastSteps(4),
	ShiftNorthSteps(2),
	ShiftNorthwestSteps(4),
	ShiftWestSteps(3),
	Walk1StepNorthwest(),
	ShiftNorthSteps(3),
	ShiftNorthwestSteps(6),
	ShiftSouthwestSteps(3),
	ShiftSouthSteps(2),
	ShiftSoutheastSteps(4),
	ShiftSouthSteps(2),
	Walk1StepSouthwest(),
	SetBit(TEMP_7043_0),
	Walk1StepSouthwest(),
	Return()
])
