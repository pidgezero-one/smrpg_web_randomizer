"""A0305_OUTER_SEA_BUBBLE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOff(),
        WalkSoutheastPixels(8),
        SetSequenceSpeed(VERY_SLOW),
        Set700CToPressedButton(),
        Mem700CAndConst(0x0006),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_305_pause_9"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_305_pause_10"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_305_pause_11"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_305_jmp_to_subroutine_12"]),
        Pause(80, identifier="ACTION_305_pause_9"),
        Pause(80, identifier="ACTION_305_pause_10"),
        Pause(80, identifier="ACTION_305_pause_11"),
        JmpToSubroutine(
            ["ACTION_304_visibility_on_21"],
            identifier="ACTION_305_jmp_to_subroutine_12"),
        TransferXYZFSteps(x=2, y=4, z=20, direction=NORTHEAST),
        Pause(40),
        JmpToSubroutine(["ACTION_304_visibility_on_21"]),
        TransferXYZFSteps(x=253, y=254, z=20, direction=NORTHEAST),
        Pause(40),
        JmpToSubroutine(["ACTION_304_visibility_on_21"]),
        TransferXYZFSteps(x=1, y=254, z=20, direction=NORTHEAST),
        Pause(40),
        Jmp(["ACTION_305_jmp_to_subroutine_12"]),
    ]
)
