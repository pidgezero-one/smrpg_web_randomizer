#A0598_MIDAS_RIVER_TOP_TUNNEL_PLAYER_OUTER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ClearSolidityBits(cant_pass_walls=True),
	ClearBit(TEMP_7043_0),
	SetVarToConst(X_COORD_2, 768),
	SetVarToConst(Y_COORD_2, 2560),
	SetVarToConst(Z_COORD_2, 0),
	TransferTo70167018701A(),
	SetAllSpeeds(NORMAL),
	VisibilityOn(),
	ShiftNortheastSteps(3),
	Walk1StepEast(),
	ShiftSoutheastSteps(4),
	ShiftSouthSteps(2),
	Walk1StepSoutheast(),
	Walk1StepEast(),
	ShiftNortheastSteps(5),
	Walk1StepEast(),
	ShiftSoutheastSteps(3),
	SetBit(TEMP_7043_1),
	Walk1StepSoutheast(),
	ShiftSouthSteps(2),
	ShiftSouthwestSteps(3),
	ShiftSouthwestSteps(2),
	SetBit(TEMP_7043_0),
	Walk1StepSouthwest(),
	Return()
])
