"""A0327_MARRYMORE_ELDERLY_GUEST_LEAVES"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSolidityBits(cant_pass_walls=True),
        FloatingOn(),
        FaceSouthwest(),
        TransferToXYZF(x=7, y=59, z=3, direction=EAST),
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(NORMAL),
        WalkSouthwestSteps(3),
        SetSequenceSpeed(SLOW),
        FaceNorthwest(),
        Pause(60),
        SetSequenceSpeed(NORMAL),
        Walk1StepSouthwest(),
        FaceSoutheast(),
        SetBit(TEMP_7044_3),
        Pause(1),
        ClearBit(TEMP_7044_3),
        Pause(29),
        Walk1StepSoutheast(),
        TransferToXYZF(x=6, y=88, z=0, direction=EAST),
        ClearSolidityBits(cant_pass_walls=True),
        FloatingOff(),
        SetBit(EMPLOYMENT_704C_2),
        Return(),
    ]
)
