# pylint: disable=C0301

"""E2634_CASINO_SLOT_MACHINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7043_0, ["EVENT_2634_ret_112"]),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_2634_jmp_if_bit_set_38"]),
        SetBit(TEMP_7043_1, identifier="EVENT_2634_set_bit_2"),
        ClearBit(DIRECTIONAL_7045_0),
        ClearBit(DIRECTIONAL_7045_1),
        ClearBit(DIRECTIONAL_7045_2),
        ClearBit(DIRECTIONAL_7045_3),
        ClearBit(DIRECTIONAL_7045_4),
        ClearBit(DIRECTIONAL_7045_5),
        JmpIfRandom2of3(["EVENT_2634_set_bit_11", "EVENT_2634_set_bit_13"]),
        Jmp(["EVENT_2634_jmp_if_random_above_66_14"]),
        SetBit(DIRECTIONAL_7045_0, identifier="EVENT_2634_set_bit_11"),
        Jmp(["EVENT_2634_jmp_if_random_above_66_14"]),
        SetBit(DIRECTIONAL_7045_1, identifier="EVENT_2634_set_bit_13"),
        JmpIfRandom2of3(
            ["EVENT_2634_set_bit_16", "EVENT_2634_set_bit_18"],
            identifier="EVENT_2634_jmp_if_random_above_66_14"),
        Jmp(["EVENT_2634_jmp_if_random_above_66_19"]),
        SetBit(DIRECTIONAL_7045_2, identifier="EVENT_2634_set_bit_16"),
        Jmp(["EVENT_2634_jmp_if_random_above_66_19"]),
        SetBit(DIRECTIONAL_7045_3, identifier="EVENT_2634_set_bit_18"),
        JmpIfRandom2of3(
            ["EVENT_2634_set_bit_21", "EVENT_2634_set_bit_23"],
            identifier="EVENT_2634_jmp_if_random_above_66_19"),
        Jmp(["EVENT_2634_pause_action_script_24"]),
        SetBit(DIRECTIONAL_7045_4, identifier="EVENT_2634_set_bit_21"),
        Jmp(["EVENT_2634_pause_action_script_24"]),
        SetBit(DIRECTIONAL_7045_5, identifier="EVENT_2634_set_bit_23"),
        PauseActionScript(NPC_4, identifier="EVENT_2634_pause_action_script_24"),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASSequenceLoopingOn(),
                ASSetSpriteSequence(index=1, looping=False),
                ASPause(6),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
            ]),
        Pause(6),
        SummonObjectToCurrentLevel(NPC_5),
        SummonObjectToCurrentLevel(NPC_6),
        SummonObjectToCurrentLevel(NPC_7),
        Pause(1),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASShadowOff(),
                ASSetWalkingSpeed(FASTEST),
                ASWalkWestPixels(17),
            ]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASShadowOff(),
                ASSetWalkingSpeed(FASTEST),
                ASWalkEastPixels(17),
            ]),
        PlaySound(sound=SO153_SLOT_MACHINES, channel=6),
        SetSyncActionScript(NPC_5, A0205_CASINO_SLOT_MACHINE_ROLLER),
        SetSyncActionScript(NPC_6, A0206_CASINO_SLOT_MACHINE_ROLLER),
        SetSyncActionScript(NPC_7, A0207_CASINO_SLOT_MACHINE_ROLLER),
        Return(),
        JmpIfBitSet(
            TEMP_7043_2,
            ["EVENT_2634_jmp_if_bit_set_44"],
            identifier="EVENT_2634_jmp_if_bit_set_38"),
        SetBit(TEMP_7043_2),
        PauseActionScript(NPC_5),
        Pause(12),
        PlaySound(sound=SO153_SLOT_MACHINES, channel=6),
        Return(),
        JmpIfBitSet(
            TEMP_7043_3,
            ["EVENT_2634_pause_action_script_50"],
            identifier="EVENT_2634_jmp_if_bit_set_44"),
        SetBit(TEMP_7043_3),
        PauseActionScript(NPC_6),
        Pause(12),
        PlaySound(sound=SO153_SLOT_MACHINES, channel=6),
        Return(),
        PauseActionScript(NPC_7, identifier="EVENT_2634_pause_action_script_50"),
        Pause(16),
        ActionQueueSync(
            target=NPC_5,
            subscript=[ASSetWalkingSpeed(VERY_FAST), ASWalkEastPixels(17)]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[ASSetWalkingSpeed(VERY_FAST), ASWalkWestPixels(17)]),
        RemoveObjectFromCurrentLevel(NPC_5),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromCurrentLevel(NPC_7),
        Set70107015ToObjectXYZ(NPC_4),
        CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 256),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
        CreatePacketAt7010(
            packet=P052_BOMB_EXPLOSION_FASTER, destinations=["EVENT_2634_pause_62"]
        ),
        Pause(16, identifier="EVENT_2634_pause_62"),
        JmpIfVarEqualsConst(
            FACTORY_FALL_1, 0, ["EVENT_2634_jmp_if_var_equals_const_66"]
        ),
        JmpIfVarEqualsConst(
            FACTORY_FALL_1, 1, ["EVENT_2634_jmp_if_var_equals_const_68"]
        ),
        JmpIfVarEqualsConst(
            FACTORY_FALL_1, 2, ["EVENT_2634_jmp_if_var_equals_const_70"]
        ),
        JmpIfVarEqualsConst(
            FACTORY_FALL_2,
            0,
            ["EVENT_2634_jmp_if_var_equals_const_72"],
            identifier="EVENT_2634_jmp_if_var_equals_const_66"),
        Jmp(["EVENT_2634_play_sound_86"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_2,
            1,
            ["EVENT_2634_jmp_if_var_equals_const_74"],
            identifier="EVENT_2634_jmp_if_var_equals_const_68"),
        Jmp(["EVENT_2634_play_sound_86"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_2,
            2,
            ["EVENT_2634_jmp_if_var_equals_const_76"],
            identifier="EVENT_2634_jmp_if_var_equals_const_70"),
        Jmp(["EVENT_2634_play_sound_86"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_3,
            0,
            ["EVENT_2634_set_7010_to_object_xyz_78"],
            identifier="EVENT_2634_jmp_if_var_equals_const_72"),
        Jmp(["EVENT_2634_play_sound_86"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_3,
            1,
            ["EVENT_2634_set_7010_to_object_xyz_78"],
            identifier="EVENT_2634_jmp_if_var_equals_const_74"),
        Jmp(["EVENT_2634_play_sound_86"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_3,
            2,
            ["EVENT_2634_set_7010_to_object_xyz_78"],
            identifier="EVENT_2634_jmp_if_var_equals_const_76"),
        Jmp(["EVENT_2634_play_sound_86"]),
        Set70107015ToObjectXYZ(
            NPC_4, identifier="EVENT_2634_set_7010_to_object_xyz_78"
        ),
        CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 256),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
        PlaySound(sound=SO094_FROG_COIN, channel=6),
        CreatePacketAt7010(
            packet=P019_FROG_COIN_BEING_COLLECTED, destinations=["EVENT_2634_jmp_85"]
        ),
        AddFrogCoins(1),
        Jmp(["EVENT_2634_action_queue_async_88"], identifier="EVENT_2634_jmp_85"),
        PlaySound(
            sound=SO105_SURPRISE, channel=6, identifier="EVENT_2634_play_sound_86"
        ),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASVisibilityOn(),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
                ASPause(24),
                ASVisibilityOff(),
            ]),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASPause(16),
                ASSetSequenceSpeed(VERY_FAST),
                ASSetSpriteSequence(index=3, looping=False),
            ],
            identifier="EVENT_2634_action_queue_async_88"),
        ClearBit(TEMP_7043_0),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        ClearBit(TEMP_7043_3),
        SetVarToConst(FACTORY_FALL_1, 0),
        SetVarToConst(FACTORY_FALL_2, 0),
        SetVarToConst(FACTORY_FALL_3, 0),
        Pause(32),
        RunDialog(
            dialog_id=DI3294_BLACKJACK,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        JmpIfDialogOptionBSelected(["EVENT_2634_pause_113"]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        StoreCoinCountTo7000(),
        CompareVarToConst(PRIMARY_TEMP_7000, 10),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2634_set_bit_108"]),
        RunDialog(
            dialog_id=DI3316_CASINO_SLOTS,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetSpriteSequence(
                    index=10,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True)
            ]),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        Return(),
        SetBit(TEMP_7043_0, identifier="EVENT_2634_set_bit_108"),
        SetVarToConst(PRIMARY_TEMP_7000, 10),
        Dec7000FromCoins(),
        Jmp(["EVENT_2634_set_bit_2"]),
        Return(identifier="EVENT_2634_ret_112"),
        Pause(10, identifier="EVENT_2634_pause_113"),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetSpriteSequence(
                    index=10,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True)
            ]),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        Return(),
    ]
)
