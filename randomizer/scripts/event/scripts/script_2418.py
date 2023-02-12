# E2418_FOREST_UNDERGROUND_1_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 242, ["EVENT_2418_jmp_if_bit_set_8"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 236, ["EVENT_2418_action_queue_async_4"]
        ),
        Jmp(["EVENT_2418_jmp_if_bit_clear_62"]),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASShadowOff(),
                ASSetAllSpeeds(FASTEST),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASShiftSouthPixels(12),
                ASShiftSouthwestPixels(5),
            ],
            identifier="EVENT_2418_action_queue_async_4",
        ),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASSetSpriteSequence(
                    index=5, is_sequence=True, looping=True, mirror_sprite=True
                )
            ],
        ),
        SetSyncActionScript(NPC_8, A0947_FOREST_1ST_UNDERGROUND_RAT),
        Jmp(["EVENT_2418_jmp_if_bit_clear_62"]),
        JmpIfBitSet(
            DIRECTIONAL_7046_7,
            ["EVENT_2418_remove_from_current_level_31"],
            identifier="EVENT_2418_jmp_if_bit_set_8",
        ),
        JmpIfBitSet(DIRECTIONAL_7046_5, ["EVENT_2418_remove_from_current_level_44"]),
        JmpIfBitSet(DIRECTIONAL_7046_6, ["EVENT_2418_remove_from_current_level_51"]),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS,
            mod_id=1,
        ),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_3),
        RemoveObjectFromCurrentLevel(NPC_4),
        RemoveObjectFromCurrentLevel(NPC_10),
        JmpIfRandom1of2(["EVENT_2418_jmp_if_random_above_128_22"]),
        RemoveObjectFromCurrentLevel(NPC_5),
        JmpIfRandom1of2(
            ["EVENT_2418_jmp_if_random_above_128_24"],
            identifier="EVENT_2418_jmp_if_random_above_128_22",
        ),
        RemoveObjectFromCurrentLevel(NPC_6),
        JmpIfRandom1of2(
            ["EVENT_2418_jmp_if_random_above_128_26"],
            identifier="EVENT_2418_jmp_if_random_above_128_24",
        ),
        RemoveObjectFromCurrentLevel(NPC_7),
        JmpIfRandom1of2(
            ["EVENT_2418_jmp_if_random_above_128_28"],
            identifier="EVENT_2418_jmp_if_random_above_128_26",
        ),
        RemoveObjectFromCurrentLevel(NPC_8),
        JmpIfRandom1of2(
            ["EVENT_2418_jmp_30"], identifier="EVENT_2418_jmp_if_random_above_128_28"
        ),
        RemoveObjectFromCurrentLevel(NPC_9),
        Jmp(["EVENT_2418_jmp_if_bit_clear_62"], identifier="EVENT_2418_jmp_30"),
        SummonObjectToCurrentLevel(
            NPC_2, identifier="EVENT_2418_remove_from_current_level_31"
        ),
        RemoveObjectFromCurrentLevel(NPC_3),
        RemoveObjectFromCurrentLevel(NPC_4),
        RemoveObjectFromCurrentLevel(NPC_5),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromCurrentLevel(NPC_8),
        RemoveObjectFromCurrentLevel(NPC_9),
        JmpIfObjectNotInSpecificLevel(
            NPC_10,
            R242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS,
            ["EVENT_2418_jmp_if_bit_clear_62"],
        ),
        ActionQueueAsync(
            target=NPC_10,
            subscript=[
                ASShadowOff(),
                ASSetAllSpeeds(FASTEST),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASShiftSouthPixels(12),
                ASShiftSouthwestPixels(5),
            ],
        ),
        SetSyncActionScript(NPC_10, A0947_FOREST_1ST_UNDERGROUND_RAT),
        Jmp(["EVENT_2418_jmp_if_bit_clear_62"]),
        RemoveObjectFromCurrentLevel(
            NPC_1, identifier="EVENT_2418_remove_from_current_level_44"
        ),
        RemoveObjectFromCurrentLevel(NPC_2),
        SummonObjectToCurrentLevel(NPC_3),
        RemoveObjectFromCurrentLevel(NPC_4),
        RemoveObjectFromCurrentLevel(NPC_10),
        Jmp(["EVENT_2418_jmp_if_bit_clear_62"]),
        RemoveObjectFromCurrentLevel(
            NPC_1, identifier="EVENT_2418_remove_from_current_level_51"
        ),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_3),
        SummonObjectToCurrentLevel(NPC_4),
        RemoveObjectFromCurrentLevel(NPC_5),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromCurrentLevel(NPC_8),
        RemoveObjectFromCurrentLevel(NPC_9),
        RemoveObjectFromCurrentLevel(NPC_10),
        JmpIfBitClear(
            DIRECTIONAL_7047_1,
            ["EVENT_2418_fade_in_from_black_async_24"],
            identifier="EVENT_2418_jmp_if_bit_clear_62",
        ),
        PlaySound(
            sound=SO019_LONG_FALL, channel=6, identifier="EVENT_2418_play_sound_63"
        ),
        ClearBit(DIRECTIONAL_7047_1),
        FreezeCamera(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASFloatingOff(),
                ASShiftZUpSteps(16),
                ASShadowOff(),
            ],
        ),
        FadeInFromBlack(sync=False),
        Pause(16),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOn(),
                ASJumpToHeight(height=0, silent=True),
                ASPause(
                    1, identifier="EVENT_2418_action_queue_async_69_SUBSCRIPT_pause_2"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2418_action_queue_async_69_SUBSCRIPT_pause_2"]
                ),
            ],
        ),
        PlaySound(sound=SO000_SILENCE, channel=6),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 233, ["EVENT_2418_set_7000_to_object_coord_84"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 235, ["EVENT_2418_action_queue_sync_78"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 236, ["EVENT_2418_action_queue_sync_80"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 242, ["EVENT_2418_action_queue_sync_82"]
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASSetSpriteSequence(index=0, looping=False),
            ],
        ),
        Jmp(["EVENT_2418_action_queue_async_89"]),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASSetSpriteSequence(index=0, looping=False),
            ],
            identifier="EVENT_2418_action_queue_sync_78",
        ),
        Jmp(["EVENT_2418_action_queue_async_89"]),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASSetSpriteSequence(index=0, looping=False),
            ],
            identifier="EVENT_2418_action_queue_sync_80",
        ),
        Jmp(["EVENT_2418_action_queue_async_89"]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASSetSpriteSequence(index=0, looping=False),
            ],
            identifier="EVENT_2418_action_queue_sync_82",
        ),
        Jmp(["EVENT_2418_action_queue_async_89"]),
        Set7000ToObjectCoord(
            object=MARIO,
            coord=COORD_X,
            pixel=True,
            bit_7=True,
            identifier="EVENT_2418_set_7000_to_object_coord_84",
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_2418_action_queue_sync_88"]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASSetSpriteSequence(index=0, looping=False),
            ],
        ),
        Jmp(["EVENT_2418_action_queue_async_89"]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASSetSpriteSequence(index=0, looping=False),
            ],
            identifier="EVENT_2418_action_queue_sync_88",
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFixedFCoordOn(),
                ASFloatingOff(),
                ASSequencePlaybackOff(),
                ASSetWalkingSpeed(NORMAL),
                ASShiftSouthPixels(8),
            ],
            identifier="EVENT_2418_action_queue_async_89",
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(8),
                ASJumpToHeight(height=128, silent=True),
                ASDb(bytearray(b"\xfd\x9c\n")),
                ASWalk1StepSouth(),
            ],
        ),
        Pause(48),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        Return(),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2418_fade_in_from_black_async_24"
        ),
        Return(),
    ]
)
