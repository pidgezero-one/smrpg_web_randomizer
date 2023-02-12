#A0602_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_PLAYER_OUTER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ClearSolidityBits(cant_pass_walls=True),
	ClearBit(TEMP_7043_0),
	SetVarToConst(X_COORD_2, 4608),
	SetVarToConst(Y_COORD_2, 13568),
	SetVarToConst(Z_COORD_2, 0),
	TransferTo70167018701A(),
	SetAllSpeeds(NORMAL),
	VisibilityOn(),
	ShiftNortheastSteps(6),
	Walk1StepNorth(),
	ShiftNorthwestSteps(4),
	ShiftNorthSteps(2),
	ShiftNorthwestSteps(4),
	ShiftSouthwestSteps(3),
	ShiftSouthSteps(2),
	ShiftSoutheastSteps(3),
	Walk1StepSouth(),
	ShiftSouthwestSteps(3),
	Walk1StepWest(),
	ShiftNorthwestSteps(2),
	Walk1StepNorth(),
	ShiftNorthwestSteps(3),
	ShiftSouthwestSteps(2),
	SetBit(TEMP_7043_0),
	Walk1StepSouthwest(),
	Return()
])
