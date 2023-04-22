"""A0266_SEA_SHORE_BLOOBER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetMovementsBits(bit_0=True, cant_walk_under=True),
        Set700CToPressedButton(),
        Mem700CAndConst(0x0003),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_266_set_animation_speed_9"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_266_pause_8"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_266_pause_7"]),
        Pause(3),
        Pause(3, identifier="ACTION_266_pause_7"),
        Pause(3, identifier="ACTION_266_pause_8"),
        SetWalkingSpeed(SLOW, identifier="ACTION_266_set_animation_speed_9"),
        SequencePlaybackOff(),
        ShiftZDownSteps(4),
        FaceMario(),
        SequencePlaybackOn(),
        ClearSolidityBits(cant_pass_walls=True),
        SetWalkingSpeed(FAST),
        SetSolidityBits(cant_pass_walls=True),
        StartLoopNTimes(31),
        ShiftZUpPixels(2),
        WalkFDirectionPixels(1),
        EndLoop(),
        Jmp(["ACTION_266_set_animation_speed_9"]),
    ]
)
