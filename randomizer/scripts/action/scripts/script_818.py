"""A0818_LANDS_END_CHOW_JUMP_OUT_OF_PIT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOn(),
        SetAllSpeeds(FAST),
        PlaySound(sound=SO030_SURPRISED_MONSTER, channel=4),
        JumpToHeight(128),
        Walk1StepFDirection(),
        SetSolidityBits(cant_pass_walls=True),
        Pause(1, identifier="ACTION_818_pause_6"),
        JmpIfObjectInAir(DUMMY_0X07, ["ACTION_818_pause_6"]),
        Set700CToPressedButton(),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_700C, 22, ["ACTION_818_set_solidity_bits_11"]
        ),
        SetBit(TEMP_7044_7),
        SetSolidityBits(
            cant_walk_under=True, identifier="ACTION_818_set_solidity_bits_11"
        ),
        SetSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        SetPriority(3),
        JmpIfRandom1of2(
            ["ACTION_818_set_animation_speed_19"],
            identifier="ACTION_818_jmp_if_random_above_128_14"),
        SetWalkingSpeed(NORMAL, identifier="ACTION_818_set_animation_speed_15"),
        FaceMario(),
        Walk1StepFDirection(),
        Jmp(["ACTION_818_jmp_if_random_above_128_14"]),
        SetWalkingSpeed(SLOW, identifier="ACTION_818_set_animation_speed_19"),
        TurnRandomDirection(),
        Walk1StepFDirection(),
        Jmp(["ACTION_818_set_animation_speed_15"]),
    ]
)
