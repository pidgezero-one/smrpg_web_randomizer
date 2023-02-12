# E3486_MIDAS_RIVER_BASE_AREA_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 15),
        ActionQueueAsync(
            target=MARIO, subscript=[ASObjectMemorySetBit(arg_1=0x0B, bits=[3])]
        ),
        EnableControlsUntilReturn([]),
        SlowDownMusicTempoBy(duration=0, change=0),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASJmpIfBitSet(BUCKET_WARP_BIT, ["EVENT_3486_action_queue_sync_5"]),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftWestPixels(4),
                ASSetWalkingSpeed(NORMAL),
            ],
            identifier="EVENT_3486_action_queue_sync_5",
        ),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASSetVRAMPriority(PRIORITY_3),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(VERY_FAST),
                ASAddZCoord1Step(),
                ASShiftEastPixels(4),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[0, 1]),
            ],
        ),
        JmpIfBitClear(BUCKET_WARP_BIT, ["EVENT_3486_jmp_if_bit_set_9"]),
        RemoveObjectFromCurrentLevel(NPC_3),
        JmpIfBitSet(
            TEMP_7044_7,
            ["EVENT_3486_remove_from_current_level_11"],
            identifier="EVENT_3486_jmp_if_bit_set_9",
        ),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_3486_action_queue_async_15"]),
        RemoveObjectFromCurrentLevel(
            NPC_1, identifier="EVENT_3486_remove_from_current_level_11"
        ),
        RemoveObjectFromCurrentLevel(NPC_4),
        SetVarToConst(TEMP_702A, 0),
        JmpIfBitClear(TEMP_7044_7, ["EVENT_3486_jmp_to_event_14"]),
        SetBit(SIGNAL_RING_DIRECTIONAL_BIT),
        RunEventAsSubroutine(
            E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3486_jmp_to_event_14"
        ),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3486_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3486_ret_26"]),
        RunEventAsSubroutine(E3892_MIDAS_RIVER_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_3486_ret_26"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=17, y=15, z=10, direction=EAST),
                ASJumpToHeight(height=0, silent=True),
                ASPause(5),
            ],
            identifier="EVENT_3486_action_queue_async_15",
        ),
        FadeInFromBlack(sync=True),
        PlaySoundBalance(sound=SO048_MINECART_START, balance=30),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASFixedFCoordOn(),
                ASSetAllSpeeds(FAST),
                ASShiftSoutheastSteps(7),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASShadowOff(),
                ASSetAllSpeeds(FAST),
                ASShiftSoutheastSteps(7),
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=4),
            ],
        ),
        JmpIfBitSet(BUCKET_WARP_BIT, ["EVENT_3486_action_queue_sync_22"]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetAllSpeeds(FASTER),
                ASWalk1StepNorthwest(),
                ASJmpIfBitSet(
                    UNKNOWN_MIDAS_RIVER_704E_5,
                    [
                        "EVENT_3486_action_queue_sync_21_SUBSCRIPT_shift_northeast_steps_5"
                    ],
                ),
                ASShiftNortheastSteps(5),
                ASJmp(["EVENT_3486_action_queue_sync_22"]),
                ASShiftNortheastSteps(
                    4,
                    identifier="EVENT_3486_action_queue_sync_21_SUBSCRIPT_shift_northeast_steps_5",
                ),
            ],
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftSouthPixels(4),
                ASShiftNorthPixels(8),
                ASShiftSouthPixels(8),
                ASSetWalkingSpeed(SLOW),
            ],
            identifier="EVENT_3486_action_queue_sync_22",
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASStartLoopNTimes(1),
                ASShiftZUpPixels(4),
                ASShiftZDownPixels(4),
                ASEndLoop(),
                ASShiftNorthwestSteps(8),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASShadowOn(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetSpriteSequence(
                    index=0,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASJumpToHeight(height=112, silent=True),
                ASShiftSoutheastSteps(3),
                ASSetSolidityBits(cant_pass_walls=True),
                ASPause(
                    1, identifier="EVENT_3486_action_queue_async_24_SUBSCRIPT_pause_6"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3486_action_queue_async_24_SUBSCRIPT_pause_6"]
                ),
                ASResetProperties(),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=4),
                ASJumpToHeight(height=112, silent=True),
                ASShiftSouthwestSteps(2),
                ASPause(
                    1, identifier="EVENT_3486_action_queue_async_24_SUBSCRIPT_pause_12"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3486_action_queue_async_24_SUBSCRIPT_pause_12"]
                ),
                ASSetAllSpeeds(NORMAL),
            ],
        ),
        RemoveObjectFromCurrentLevel(NPC_4),
        JmpIfBitSet(BUCKET_WARP_BIT, ["EVENT_3486_ret_44"]),
        JmpIfBitSet(UNKNOWN_MIDAS_RIVER_7079_0, ["EVENT_3486_jmp_if_bit_set_39"]),
        SetBit(UNKNOWN_7065_6),
        SetBit(UNKNOWN_7065_7),
        SetBit(MAP_DIRECTIONAL_KERO_SEWERS_MIDAS_RIVER),
        SetBit(MAP_DIRECTIONAL_MIDAS_RIVER_TADPOLE_POND),
        SetBit(UNKNOWN_MIDAS_RIVER_7079_0),
        CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 32768),
        JmpIfComparisonResultIsLesser(["EVENT_3486_set_70A0_short_mem_to_7000_37"]),
        SetVarToConst(PRIMARY_TEMP_7000, 0),
        CopyVarToVar(
            from_var=PRIMARY_TEMP_7000,
            to_var=MIDAS_RIVER_70B3,
            identifier="EVENT_3486_set_70A0_short_mem_to_7000_37",
        ),
        SetBit(TEMP_7043_2),
        JmpIfBitSet(
            UNKNOWN_MIDAS_RIVER_704E_5,
            ["EVENT_3486_jmp_to_event_43"],
            identifier="EVENT_3486_jmp_if_bit_set_39",
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASPlaySound(sound=SO034_SQUIRM_WRITHE, channel=4),
                ASPause(20),
                ASPlaySound(sound=SO056_SHAKE_HEAD, channel=4),
                ASSetAllSpeeds(FAST),
                ASFixedFCoordOn(),
                ASShiftEastPixels(2),
                ASStartLoopNTimes(3),
                ASShiftWestPixels(4),
                ASShiftEastPixels(4),
                ASEndLoop(),
                ASShiftWestPixels(2),
                ASWalk1StepSouthwest(),
                ASFixedFCoordOff(),
                ASFaceNortheast(),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(height=1, silent=True),
                ASPause(
                    1, identifier="EVENT_3486_action_queue_async_41_SUBSCRIPT_pause_1"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3486_action_queue_async_41_SUBSCRIPT_pause_1"]
                ),
                ASPlaySound(sound=SO058_INSERT, channel=4),
            ],
        ),
        SetBit(UNKNOWN_MIDAS_RIVER_704E_5),
        JmpToEvent(
            E3479_MIDAS_RIVER_SCORE_SUBMISSION, identifier="EVENT_3486_jmp_to_event_43"
        ),
        Return(identifier="EVENT_3486_ret_44"),
    ]
)
