#A0600_MIDAS_RIVER_MID_RIGHT_TUNNEL_PLAYER_OUTER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ClearSolidityBits(cant_pass_walls=True),
	ClearBit(TEMP_7043_0),
	SetVarToConst(X_COORD_2, 8448),
	SetVarToConst(Y_COORD_2, 8832),
	SetVarToConst(Z_COORD_2, 0),
	TransferTo70167018701A(),
	SetAllSpeeds(NORMAL),
	VisibilityOn(),
	ShiftNorthwestSteps(4),
	ShiftNorthSteps(2),
	ShiftNortheastSteps(3),
	ShiftSoutheastSteps(8),
	ClearBit(TEMP_7043_5),
	ShiftSouthSteps(2),
	ShiftSoutheastSteps(2),
	Walk1StepEast(),
	ShiftNortheastSteps(2),
	ShiftSoutheastSteps(4),
	ShiftNortheastSteps(4),
	Walk1StepEast(),
	Walk1StepSoutheast(),
	ShiftSouthSteps(2),
	Walk1StepSouthwest(),
	SetBit(TEMP_7043_0),
	Walk1StepSouthwest(),
	Return()
])
