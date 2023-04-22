"""A0270_SHIP_BLOOBER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetMovementsBits(bit_0=True, cant_walk_under=True),
        SetPriority(3),
        SetWalkingSpeed(SLOW, identifier="ACTION_270_set_animation_speed_2"),
        SequencePlaybackOff(),
        ShiftZDownSteps(5),
        FaceMario(),
        Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F, pixel=True),
        CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7032),
        SequencePlaybackOn(),
        ClearSolidityBits(cant_pass_walls=True),
        SetWalkingSpeed(FAST),
        SetSolidityBits(cant_pass_walls=True),
        StartLoopNTimes(39),
        ShiftZUpPixels(2),
        WalkFDirectionPixels(1),
        EndLoop(),
        Jmp(["ACTION_270_set_animation_speed_2"]),
    ]
)
