"""A0124_MK_BRANCH_HALLWAY_HENCHMAN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetBit(TEMP_7043_5, identifier="ACTION_124_set_bit_0"),
        SetVarToRandom(PRIMARY_TEMP_700C, 2),
        Inc(PRIMARY_TEMP_700C),
        LoadMemory(PRIMARY_TEMP_700C),
        JmpToSubroutine(["ACTION_103_clear_solidity_bits_0"]),
        EndLoop(),
        JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
        JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
        FaceSoutheast(),
        Jmp(["ACTION_124_set_bit_0"]),
    ]
)
