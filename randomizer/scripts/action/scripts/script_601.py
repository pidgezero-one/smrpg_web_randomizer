"""A0601_MIDAS_RIVER_BOTTOM_LEFT_TUNNEL_PLAYER_OUTER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ClearSolidityBits(cant_pass_walls=True),
        ClearBit(TEMP_7043_0),
        SetVarToConst(X_COORD_2, 14080),
        SetVarToConst(Y_COORD_2, 4480),
        SetVarToConst(Z_COORD_2, 0),
        TransferTo70167018701A(),
        SetAllSpeeds(NORMAL),
        VisibilityOn(),
        WalkNortheastSteps(4),
        WalkNorthSteps(2),
        WalkNorthwestSteps(4),
        WalkWestSteps(3),
        Walk1StepNorthwest(),
        WalkNorthSteps(3),
        WalkNorthwestSteps(6),
        WalkSouthwestSteps(3),
        WalkSouthSteps(2),
        WalkSoutheastSteps(4),
        WalkSouthSteps(2),
        Walk1StepSouthwest(),
        SetBit(TEMP_7043_0),
        Walk1StepSouthwest(),
        Return(),
    ]
)
