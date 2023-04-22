"""A0930_DONUT_LIFT_FALL"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FixedFCoordOn(),
        Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F, pixel=True),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_930_set_sprite_sequence_5"]),
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        Jmp(["ACTION_930_start_loop_n_times_6"]),
        SetSpriteSequence(
            index=0,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_930_set_sprite_sequence_5",
        ),
        StartLoopNTimes(47, identifier="ACTION_930_start_loop_n_times_6"),
        Pause(1),
        JmpIfMarioInAir(["ACTION_930_ret_23"]),
        EndLoop(),
        StartLoopNTimes(11),
        SetWalkingSpeed(FAST),
        ShiftZDownPixels(2),
        ShiftZUpPixels(2),
        JmpIfMarioInAir(["ACTION_930_ret_23"]),
        EndLoop(),
        JumpToHeight(height=0, silent=True),
        FloatingOn(),
        Pause(1, identifier="ACTION_930_pause_18"),
        JmpIfObjectInAir(DUMMY_0X07, ["ACTION_930_pause_18"]),
        ClearSolidityBits(
            cant_pass_walls=True,
            bit_4=True,
            cant_pass_npcs=True,
            cant_walk_through=True,
            bit_7=True,
        ),
        VisibilityOff(),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        Return(identifier="ACTION_930_ret_23"),
    ]
)
