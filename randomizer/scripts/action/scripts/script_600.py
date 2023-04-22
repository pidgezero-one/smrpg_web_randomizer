"""A0600_MIDAS_RIVER_MID_RIGHT_TUNNEL_PLAYER_OUTER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ClearSolidityBits(cant_pass_walls=True),
        ClearBit(TEMP_7043_0),
        SetVarToConst(X_COORD_2, 8448),
        SetVarToConst(Y_COORD_2, 8832),
        SetVarToConst(Z_COORD_2, 0),
        TransferTo70167018701A(),
        SetAllSpeeds(NORMAL),
        VisibilityOn(),
        WalkNorthwestSteps(4),
        WalkNorthSteps(2),
        WalkNortheastSteps(3),
        WalkSoutheastSteps(8),
        ClearBit(TEMP_7043_5),
        WalkSouthSteps(2),
        WalkSoutheastSteps(2),
        Walk1StepEast(),
        WalkNortheastSteps(2),
        WalkSoutheastSteps(4),
        WalkNortheastSteps(4),
        Walk1StepEast(),
        Walk1StepSoutheast(),
        WalkSouthSteps(2),
        Walk1StepSouthwest(),
        SetBit(TEMP_7043_0),
        Walk1StepSouthwest(),
        Return(),
    ]
)
