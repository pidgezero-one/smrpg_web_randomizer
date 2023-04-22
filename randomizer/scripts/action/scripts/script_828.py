"""A0828_BIG_CONVEYOR_ROOM_BOO"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(SLOW),
        SetPriority(3),
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 65517),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(1),
        EndLoop(),
        Set700CToPressedButton(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 27, ["ACTION_828_shift_northeast_steps_37"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 26, ["ACTION_828_shift_southwest_steps_33"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 25, ["ACTION_828_shift_northwest_steps_29"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 24, ["ACTION_828_shift_southwest_steps_26"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 23, ["ACTION_828_shift_southeast_steps_19"]
        ),
        WalkNortheastSteps(6, identifier="ACTION_828_shift_northeast_steps_13"),
        WalkNorthwestSteps(2),
        WalkNortheastSteps(2),
        WalkNorthwestSteps(4),
        WalkNortheastSteps(2),
        WalkNorthwestSteps(5),
        WalkSoutheastSteps(5, identifier="ACTION_828_shift_southeast_steps_19"),
        WalkSouthwestSteps(2),
        WalkSoutheastSteps(4),
        WalkSouthwestSteps(2),
        WalkSoutheastSteps(2),
        WalkSouthwestSteps(6),
        Jmp(["ACTION_828_shift_northeast_steps_13"]),
        WalkSouthwestSteps(2, identifier="ACTION_828_shift_southwest_steps_26"),
        WalkSoutheastSteps(5),
        Walk1StepSouthwest(),
        WalkNorthwestSteps(3, identifier="ACTION_828_shift_northwest_steps_29"),
        WalkNortheastSteps(3),
        WalkNorthwestSteps(2),
        Jmp(["ACTION_828_shift_southwest_steps_26"]),
        WalkSouthwestSteps(2, identifier="ACTION_828_shift_southwest_steps_33"),
        WalkNorthwestSteps(2),
        WalkSouthwestSteps(2),
        Walk1StepNorthwest(),
        WalkNortheastSteps(3, identifier="ACTION_828_shift_northeast_steps_37"),
        WalkSoutheastSteps(3),
        Walk1StepNortheast(),
        Jmp(["ACTION_828_shift_southwest_steps_33"]),
    ]
)
