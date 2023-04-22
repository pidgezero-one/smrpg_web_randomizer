"""A0602_MIDAS_RIVER_BOTTOM_RIGHT_TUNNEL_PLAYER_OUTER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ClearSolidityBits(cant_pass_walls=True),
        ClearBit(TEMP_7043_0),
        SetVarToConst(X_COORD_2, 4608),
        SetVarToConst(Y_COORD_2, 13568),
        SetVarToConst(Z_COORD_2, 0),
        TransferTo70167018701A(),
        SetAllSpeeds(NORMAL),
        VisibilityOn(),
        WalkNortheastSteps(6),
        Walk1StepNorth(),
        WalkNorthwestSteps(4),
        WalkNorthSteps(2),
        WalkNorthwestSteps(4),
        WalkSouthwestSteps(3),
        WalkSouthSteps(2),
        WalkSoutheastSteps(3),
        Walk1StepSouth(),
        WalkSouthwestSteps(3),
        Walk1StepWest(),
        WalkNorthwestSteps(2),
        Walk1StepNorth(),
        WalkNorthwestSteps(3),
        WalkSouthwestSteps(2),
        SetBit(TEMP_7043_0),
        Walk1StepSouthwest(),
        Return(),
    ]
)
