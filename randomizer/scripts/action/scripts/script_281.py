"""A0281_KEEP_TOPPER_GAME_SET_BUTTON_OR_BALL_STATE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 65515),
        SetVarToConst(TEMP_7026, 1),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 0, ["ACTION_281_set_700C_to_7000_short_mem_7"]
        ),
        LoadMemory(PRIMARY_TEMP_700C),
        VarShiftLeft(TEMP_7026, 255),
        EndLoop(),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_700C,
            identifier="ACTION_281_set_700C_to_7000_short_mem_7"),
        Mem700CAndVar(TEMP_7026),
        CompareVarToConst(PRIMARY_TEMP_700C, 0),
        JmpIfLoadedMemoryIsNot0(["ACTION_281_jmp_to_subroutine_18"]),
        JmpToSubroutine(["ACTION_281_set_700C_to_7000_short_mem_25"]),
        SetVRAMPriority(NORMAL_PRIORITY),
        SetSolidityBits(bit_4=True, cant_walk_through=True),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        Pause(1),
        Return(),
        JmpToSubroutine(
            ["ACTION_281_set_700C_to_7000_short_mem_25"],
            identifier="ACTION_281_jmp_to_subroutine_18"),
        SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
        ClearSolidityBits(bit_4=True, cant_walk_through=True),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        SetSpriteSequence(index=1, is_sequence=True, looping=True),
        Pause(1),
        Return(),
        CopyVarToVar(
            from_var=ROSE_WAY_703C,
            to_var=PRIMARY_TEMP_700C,
            identifier="ACTION_281_set_700C_to_7000_short_mem_25"),
        Mem700CAndVar(TEMP_7026),
        CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
        CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_700C),
        Mem700CAndVar(TEMP_7026),
        Compare700CToVar(TEMP_7028),
        JmpIfLoadedMemoryIs0(["ACTION_281_ret_33"]),
        PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
        Return(identifier="ACTION_281_ret_33"),
    ]
)
