# pylint: disable=C0301

"""E2491_BEAN_VALLEY_BOTTOM_LEFT_PIPE_BASEMENT_ORIGINAL_SLOT_MACHINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7044_2, ["EVENT_2491_jmp_if_bit_set_15"]),
        SetBit(TEMP_7044_2),
        PauseActionScript(MEM_70A8),
        Set7016701BToObjectXYZ(MEM_70A8),
        AddConstToVar(Z_COORD_2, 304),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASSequenceLoopingOn(),
                ASSetSpriteSequence(index=1, looping=False),
                ASPause(6),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
            ]),
        ActionQueueSync(target=NPC_2, subscript=[ASTransferTo70167018701A()]),
        ActionQueueSync(target=NPC_3, subscript=[ASTransferTo70167018701A()]),
        ActionQueueSync(target=NPC_4, subscript=[ASTransferTo70167018701A()]),
        ActionQueueSync(target=NPC_5, subscript=[ASTransferTo70167018701A()]),
        ActionQueueAsync(target=NPC_6, subscript=[ASTransferTo70167018701A()]),
        Pause(6),
        SummonObjectToCurrentLevel(NPC_2),
        SummonObjectToCurrentLevel(NPC_3),
        SummonObjectToCurrentLevel(NPC_4),
        Pause(1),
        ActionQueueSync(
            target=NPC_3, subscript=[ASSetWalkingSpeed(FASTEST), ASWalkEastPixels(17)]
        ),
        ActionQueueAsync(
            target=NPC_4, subscript=[ASSetWalkingSpeed(FASTEST), ASWalkWestPixels(17)]
        ),
        SetSyncActionScript(NPC_2, A0185_CHEST_SLOT_MACHINE_ROLLER),
        SetSyncActionScript(NPC_3, A0186_CHEST_SLOT_MACHINE_ROLLER),
        SetSyncActionScript(NPC_4, A0184_CHEST_SLOT_MACHINE_ROLLER),
        Return(),
        JmpIfBitSet(
            TEMP_7044_3,
            ["EVENT_2491_jmp_if_bit_set_19"],
            identifier="EVENT_2491_jmp_if_bit_set_15"),
        SetBit(TEMP_7044_3),
        PauseActionScript(NPC_4),
        Return(),
        JmpIfBitSet(
            TEMP_7044_4,
            ["EVENT_2491_disable_trigger_23"],
            identifier="EVENT_2491_jmp_if_bit_set_19"),
        SetBit(TEMP_7044_4),
        PauseActionScript(NPC_2),
        Return(),
        DisableObjectTrigger(MEM_70A8, identifier="EVENT_2491_disable_trigger_23"),
        PauseActionScript(NPC_3),
        Pause(16),
        ActionQueueSync(
            target=NPC_4, subscript=[ASSetWalkingSpeed(VERY_FAST), ASWalkEastPixels(8)]
        ),
        ActionQueueSync(
            target=NPC_3, subscript=[ASSetWalkingSpeed(VERY_FAST), ASWalkWestPixels(8)]
        ),
        StopEmbeddedActionScript(NPC_3),
        StopEmbeddedActionScript(NPC_4),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_3),
        RemoveObjectFromCurrentLevel(NPC_4),
        SummonObjectToCurrentLevel(NPC_6),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetSpriteSequence(index=1, looping=False),
                ASPause(16),
                ASVisibilityOff(),
            ]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_1, 0, ["EVENT_2491_jmp_if_var_equals_const_38"]
        ),
        JmpIfVarEqualsConst(
            FACTORY_FALL_1, 1, ["EVENT_2491_jmp_if_var_equals_const_41"]
        ),
        JmpIfVarEqualsConst(
            FACTORY_FALL_1, 2, ["EVENT_2491_jmp_if_var_equals_const_44"]
        ),
        JmpIfVarEqualsConst(
            FACTORY_FALL_2,
            0,
            ["EVENT_2491_jmp_if_var_equals_const_47"],
            identifier="EVENT_2491_jmp_if_var_equals_const_38"),
        JmpIfVarEqualsConst(
            FACTORY_FALL_2, 1, ["EVENT_2491_jmp_if_var_equals_const_49"]
        ),
        Jmp(["EVENT_2491_jmp_if_var_equals_const_52"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_2,
            0,
            ["EVENT_2491_jmp_if_var_equals_const_55"],
            identifier="EVENT_2491_jmp_if_var_equals_const_41"),
        JmpIfVarEqualsConst(
            FACTORY_FALL_2, 1, ["EVENT_2491_jmp_if_var_equals_const_58"]
        ),
        Jmp(["EVENT_2491_jmp_if_var_equals_const_60"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_2,
            0,
            ["EVENT_2491_jmp_if_var_equals_const_63"],
            identifier="EVENT_2491_jmp_if_var_equals_const_44"),
        JmpIfVarEqualsConst(
            FACTORY_FALL_2, 1, ["EVENT_2491_jmp_if_var_equals_const_66"]
        ),
        Jmp(["EVENT_2491_jmp_if_var_equals_const_69"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_3,
            0,
            ["EVENT_2491_summon_to_current_level_71"],
            identifier="EVENT_2491_jmp_if_var_equals_const_47"),
        Jmp(["EVENT_2491_play_sound_76"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_3,
            0,
            ["EVENT_2491_play_sound_76"],
            identifier="EVENT_2491_jmp_if_var_equals_const_49"),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2491_play_sound_81"]),
        Jmp(["EVENT_2491_action_queue_async_92"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_3,
            0,
            ["EVENT_2491_play_sound_76"],
            identifier="EVENT_2491_jmp_if_var_equals_const_52"),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2491_action_queue_async_92"]),
        Jmp(["EVENT_2491_play_sound_88"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_3,
            0,
            ["EVENT_2491_play_sound_76"],
            identifier="EVENT_2491_jmp_if_var_equals_const_55"),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2491_play_sound_81"]),
        Jmp(["EVENT_2491_action_queue_async_92"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_3,
            1,
            ["EVENT_2491_summon_to_current_level_71"],
            identifier="EVENT_2491_jmp_if_var_equals_const_58"),
        Jmp(["EVENT_2491_play_sound_81"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_3,
            0,
            ["EVENT_2491_action_queue_async_92"],
            identifier="EVENT_2491_jmp_if_var_equals_const_60"),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2491_play_sound_81"]),
        Jmp(["EVENT_2491_play_sound_88"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_3,
            0,
            ["EVENT_2491_play_sound_76"],
            identifier="EVENT_2491_jmp_if_var_equals_const_63"),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2491_action_queue_async_92"]),
        Jmp(["EVENT_2491_play_sound_88"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_3,
            0,
            ["EVENT_2491_action_queue_async_92"],
            identifier="EVENT_2491_jmp_if_var_equals_const_66"),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 1, ["EVENT_2491_play_sound_81"]),
        Jmp(["EVENT_2491_play_sound_88"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_3,
            2,
            ["EVENT_2491_summon_to_current_level_71"],
            identifier="EVENT_2491_jmp_if_var_equals_const_69"),
        Jmp(["EVENT_2491_play_sound_88"]),
        SummonObjectToCurrentLevel(
            NPC_5, identifier="EVENT_2491_summon_to_current_level_71"
        ),
        PlaySound(sound=SO094_FROG_COIN, channel=6),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetPriority(3),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASPause(32),
                ASVisibilityOff(),
            ]),
        AddFrogCoins(1),
        Jmp(["EVENT_2491_action_queue_sync_99"]),
        PlaySound(sound=SO014_FLOWER, channel=6, identifier="EVENT_2491_play_sound_76"),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASVisibilityOn(),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
                ASPause(32),
                ASVisibilityOff(),
            ]),
        SetVarToConst(PRIMARY_TEMP_7000, 1),
        Add7000ToMaxFP(),
        Jmp(["EVENT_2491_action_queue_sync_99"]),
        PlaySound(
            sound=SO071_MUSHROOM_CURE, channel=6, identifier="EVENT_2491_play_sound_81"
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASVisibilityOn(),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASPause(32),
                ASVisibilityOff(),
            ]),
        RestoreAllHP(),
        RestoreAllFP(),
        TintLayers(
            layers=[LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND],
            red=64,
            green=160,
            blue=64,
            speed=3,
            bit_15=True),
        TintLayers(
            layers=[LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND],
            red=0,
            green=0,
            blue=0,
            speed=3,
            bit_15=True),
        Jmp(["EVENT_2491_action_queue_sync_99"]),
        PlaySound(
            sound=SO027_FOUND_AN_ITEM, channel=6, identifier="EVENT_2491_play_sound_88"
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASVisibilityOn(),
                ASSetSpriteSequence(index=3, is_sequence=True, looping=True),
                ASPause(32),
                ASVisibilityOff(),
            ]),
        AddToInventory(RockCandy),
        Jmp(["EVENT_2491_action_queue_sync_99"]),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASVisibilityOn(),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
            ],
            identifier="EVENT_2491_action_queue_async_92"),
        Pause(32),
        JmpIfBitSet(
            ALTERNATE_STAR_PIECE_WIN_CONDITION, ["EVENT_2491_start_battle_94_"]
        ),
        RunEventAsSubroutine(E1931_TREASURE_CHEST_FAILURE_MIMIC_FIGHT),
        Jmp(["EVENT_2491_remove_from_current_level_97"]),
        SetVarToConst(PRIMARY_TEMP_7000, 514, identifier="EVENT_2491_start_battle_94_"),
        RunEventAsSubroutine(E0353_BOSS_BATTLE),
        RunEventAsSubroutine(E0171_MIMIC_3_GRANT_STAR_PIECE_CONTAINER),
        RemoveObjectFromCurrentLevel(
            NPC_2, identifier="EVENT_2491_remove_from_current_level_97"
        ),
        FadeInFromBlack(sync=False),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASPause(32),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=3, looping=False),
                ASPause(10),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
            ],
            identifier="EVENT_2491_action_queue_sync_99"),
        DisableObjectTrigger(MEM_70A8),
        ClearBit(TEMP_7044_2),
        ClearBit(TEMP_7044_3),
        ClearBit(TEMP_7044_4),
        Return(),
    ]
)
