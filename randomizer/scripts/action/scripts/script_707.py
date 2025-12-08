"""A0707_BOOSTER_HILL_HENCHMAN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(2, identifier="ACTION_707_set_priority_0"),
        SetWalkingSpeed(FAST),
        SetSequenceSpeed(FASTER),
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        SetSolidityBits(bit_4=True, cant_walk_through=True),
        WalkNorthwestSteps(6),
        SequenceLoopingOn(),
        FixedFCoordOn(),
        JmpIfBitSet(TEMP_7043_6, ["ACTION_707_set_animation_speed_43"]),
        SetVarToRandom(
            PRIMARY_TEMP_700C, 60, identifier="ACTION_707_set_var_to_random_10"
        ),
        CompareVarToConst(PRIMARY_TEMP_700C, 30),
        JmpIfComparisonResultIsLesser(["ACTION_707_jmp_if_bit_set_24"]),
        LoadMemory(PRIMARY_TEMP_700C, identifier="ACTION_707_load_mem_13"),
        Pause(1),
        EndLoop(),
        JmpIfBitSet(TEMP_7043_3, ["ACTION_707_jmp_if_bit_set_24"]),
        SetWalkingSpeed(VERY_SLOW),
        SetSequenceSpeed(FAST),
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        WalkNorthwestPixels(8),
        WalkSoutheastPixels(8),
        JmpIfBitSet(TEMP_7043_6, ["ACTION_707_set_animation_speed_43"]),
        Jmp(["ACTION_707_set_var_to_random_10"]),
        JmpIfBitSet(
            TEMP_7043_6,
            ["ACTION_707_set_animation_speed_43"],
            identifier="ACTION_707_jmp_if_bit_set_24"),
        JmpIfVarEqualsConst(TEMP_70AE, 3, ["ACTION_707_load_mem_13"]),
        Inc(TEMP_70AE),
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(NORMAL),
        PlaySound(sound=SO030_SURPRISED_MONSTER, channel=4),
        JumpToHeight(56),
        SetSpriteSequence(index=2, is_sequence=True, looping=False),
        Pause(32),
        SetSpriteSequence(index=1, is_sequence=True, looping=True),
        SetSequenceSpeed(FAST),
        WalkNorthwestSteps(6),
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        WalkSoutheastSteps(3),
        JmpIfBitSet(TEMP_7043_6, ["ACTION_707_shift_southeast_steps_42"]),
        Dec(TEMP_70AE),
        WalkSoutheastSteps(3),
        Jmp(["ACTION_707_set_var_to_random_10"]),
        WalkSoutheastSteps(3, identifier="ACTION_707_shift_southeast_steps_42"),
        SetSequenceSpeed(NORMAL, identifier="ACTION_707_set_animation_speed_43"),
        SetWalkingSpeed(SLOW),
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        Walk1StepSoutheast(identifier="ACTION_707_walk_1_step_southeast_46"),
        Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_X, pixel=True),
        CompareVarToConst(PRIMARY_TEMP_700C, 5888),
        JmpIfComparisonResultIsLesser(["ACTION_707_walk_1_step_southeast_46"]),
        Return(),
    ]
)
