"""A0608_ROSE_WAY_5_CHEST_SHY_GUY"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShadowOff(),
        SetVRAMPriority(PRIORITY_3),
        SetPriority(3),
        SetObjectMemoryBits(arg_1=0x0E, bits=[0, 2]),
        FaceMario(identifier="ACTION_608_face_mario_4"),
        Pause(1),
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 65535),
        JmpIfMem704XAt700CBitClear(["ACTION_608_face_mario_4"]),
        ShadowOn(),
        SetObjectMemoryBits(arg_1=0x0E, bits=[]),
        JumpToHeight(108),
        Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F, pixel=True),
        CompareVarToConst(PRIMARY_TEMP_700C, 3),
        JmpIfComparisonResultIsGreaterOrEqual(["ACTION_608_set_sprite_sequence_19"]),
        CompareVarToConst(PRIMARY_TEMP_700C, 7),
        JmpIfComparisonResultIsLesser(["ACTION_608_set_sprite_sequence_19"]),
        SetSpriteSequence(index=4, looping=False, mirror_sprite=True),
        Jmp(["ACTION_608_shift_f_direction_steps_20"]),
        SetSpriteSequence(
            index=4, looping=False, identifier="ACTION_608_set_sprite_sequence_19"
        ),
        WalkFDirectionSteps(2, identifier="ACTION_608_shift_f_direction_steps_20"),
        SetVRAMPriority(NORMAL_PRIORITY),
        ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
        PlaySound(sound=SO079_YELP_IN_DISTANCE, channel=4),
        Pause(30),
        ResetProperties(),
        Set700CToPressedButton(identifier="ACTION_608_set_700C_to_pressed_button_26"),
        SetVarToConst(SECONDARY_TEMP_7024, 5),
        DecVarFrom700C(SECONDARY_TEMP_7024),
        CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70A9),
        FaceSouthwest7D(),
        Walk1StepFDirection(),
        JumpToHeight(56),
        Pause(25),
        JmpIfRandom2of3(
            [
                "ACTION_608_set_700C_to_pressed_button_26",
                "ACTION_608_set_700C_to_pressed_button_26",
            ]
        ),
        TurnRandomDirection(),
        Walk1StepFDirection(),
        Jmp(["ACTION_608_set_700C_to_pressed_button_26"]),
    ]
)
