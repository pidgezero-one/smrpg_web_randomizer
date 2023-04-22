"""A0272_VOLCANO_DRY_BONES"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(NORMAL, identifier="ACTION_272_set_animation_speed_0"),
        SetSequenceSpeed(FAST),
        Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F, pixel=True),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 7, ["ACTION_272_set_sprite_sequence_30"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 1, ["ACTION_272_set_sprite_sequence_30"]
        ),
        SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        ClearSolidityBits(bit_4=True, cant_walk_through=True),
        Set700CToPressedButton(),
        Mem700CAndConst(0x0003),
        VarShiftLeft(PRIMARY_TEMP_700C, 255),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(1),
        EndLoop(),
        Pause(4, identifier="ACTION_272_pause_14"),
        JmpIfObjectWithinRangeSameZ(
            comparing_npc=MARIO,
            usually=128,
            tiles=1,
            destinations=["ACTION_272_play_sound_17"],
        ),
        Jmp(["ACTION_272_pause_14"]),
        PlaySound(
            sound=SO117_SPINNING_MONSTER,
            channel=4,
            identifier="ACTION_272_play_sound_17",
        ),
        SetSpriteSequence(index=8, looping=False),
        Pause(18),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        SetSolidityBits(bit_4=True, cant_walk_through=True),
        StartLoopNTimes(1, identifier="ACTION_272_start_loop_n_times_22"),
        FaceMario(),
        WalkFDirectionSteps(2),
        EndLoop(),
        JmpIfObjectWithinRangeSameZ(
            comparing_npc=MARIO,
            usually=0,
            tiles=3,
            destinations=["ACTION_272_start_loop_n_times_22"],
        ),
        Pause(8),
        JmpIfRandom1of2(["ACTION_272_start_loop_n_times_22"]),
        Jmp(["ACTION_272_set_animation_speed_0"]),
        SetSpriteSequence(
            index=6,
            is_mold=True,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_272_set_sprite_sequence_30",
        ),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        ClearSolidityBits(bit_4=True, cant_walk_through=True),
        Set700CToPressedButton(),
        Mem700CAndConst(0x0003),
        VarShiftLeft(PRIMARY_TEMP_700C, 255),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(1),
        EndLoop(),
        Pause(4, identifier="ACTION_272_pause_39"),
        JmpIfObjectWithinRangeSameZ(
            comparing_npc=MARIO,
            usually=0,
            tiles=3,
            destinations=["ACTION_272_play_sound_42"],
        ),
        Jmp(["ACTION_272_pause_39"]),
        PlaySound(
            sound=SO117_SPINNING_MONSTER,
            channel=4,
            identifier="ACTION_272_play_sound_42",
        ),
        SetSpriteSequence(index=8, looping=False),
        Pause(18),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        SetSolidityBits(bit_4=True, cant_walk_through=True),
        Jmp(["ACTION_272_start_loop_n_times_22"]),
    ]
)
