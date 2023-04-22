# pylint: disable=C0301

"""E3501_BOOSTER_HILL_BARREL_INTERACTION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopBackgroundEvent(TIMER_701C),
        ClearBit(TEMP_7043_5),
        EnableControlsUntilReturn([]),
        JmpIfMarioOnAnObjectOrNot(
            ["EVENT_3501_set_short_18", "EVENT_3501_action_queue_sync_7"]
        ),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
        CompareVarToConst(PRIMARY_TEMP_7000, 256),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3501_set_short_18"]),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
            identifier="EVENT_3501_action_queue_sync_7",
        ),
        ResumeActionScript(MEM_70A8),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFloatingOff(),
                ASPlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASJumpToHeight(height=112, silent=True),
                ASSetSpriteSequence(
                    index=7, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASSetWalkingSpeed(NORMAL),
                ASFloatingOn(),
                ASStartLoopNTimes(15),
                ASVisibilityOff(),
                ASPause(1),
                ASVisibilityOn(),
                ASCompareVarToConst(SECONDARY_TEMP_7024, 65488),
                ASJmpIfLoadedMemoryIsAboveOrEqual0(
                    ["EVENT_3501_action_queue_async_9_SUBSCRIPT_pause_17"]
                ),
                ASWalkSoutheastPixels(1),
                ASDec(SECONDARY_TEMP_7024),
                ASJmp(["EVENT_3501_action_queue_async_9_SUBSCRIPT_end_loop_18"]),
                ASPause(
                    1, identifier="EVENT_3501_action_queue_async_9_SUBSCRIPT_pause_17"
                ),
                ASEndLoop(
                    identifier="EVENT_3501_action_queue_async_9_SUBSCRIPT_end_loop_18"
                ),
                ASResetProperties(),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
        ),
        EnableControlsUntilReturn([B]),
        CompareVarToConst(SECONDARY_TEMP_7024, 0),
        JmpIfLoadedMemoryIsBelow0(["EVENT_3501_resume_background_event_16"]),
        SetVarToConst(TIMER_701C, 2),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E3505_BOOSTER_HILL_UNKNOWN, timer_var=TIMER_701C
        ),
        Return(),
        ResumeBackgroundEvent(
            TIMER_701C, identifier="EVENT_3501_resume_background_event_16"
        ),
        Return(),
        SetVarToConst(TEMP_7028, 36, identifier="EVENT_3501_set_short_18"),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
            identifier="EVENT_3501_action_queue_sync_19",
        ),
        ResumeActionScript(MEM_70A8),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASCopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_700C),
                ASAddVarTo700C(TEMP_7028),
                ASCompareVarToConst(PRIMARY_TEMP_700C, 64),
                ASJmpIfLoadedMemoryIsAboveOrEqual0(
                    [
                        "EVENT_3501_action_queue_async_21_SUBSCRIPT_set_700C_to_7000_short_mem_6"
                    ]
                ),
                ASJmp(["EVENT_3501_action_queue_async_21_SUBSCRIPT_set_8"]),
                ASCopyVarToVar(
                    from_var=TEMP_7028,
                    to_var=PRIMARY_TEMP_700C,
                    identifier="EVENT_3501_action_queue_async_21_SUBSCRIPT_set_700C_to_7000_short_mem_6",
                ),
                ASJmp(
                    [
                        "EVENT_3501_action_queue_async_21_SUBSCRIPT_set_animation_speed_16"
                    ]
                ),
                ASSetVarToConst(
                    PRIMARY_TEMP_700C,
                    64,
                    identifier="EVENT_3501_action_queue_async_21_SUBSCRIPT_set_8",
                ),
                ASDecVarFrom700C(SECONDARY_TEMP_7024),
                ASJmpIfVarNotEqualsConst(
                    PRIMARY_TEMP_700C,
                    0,
                    [
                        "EVENT_3501_action_queue_async_21_SUBSCRIPT_set_animation_speed_16"
                    ],
                ),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=4),
                ASFloatingOff(),
                ASJumpToHeight(height=108, silent=True),
                ASFloatingOn(),
                ASJmp(
                    ["EVENT_3501_action_queue_async_21_SUBSCRIPT_set_solidity_bits_25"]
                ),
                ASSetWalkingSpeed(
                    NORMAL,
                    identifier="EVENT_3501_action_queue_async_21_SUBSCRIPT_set_animation_speed_16",
                ),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=4),
                ASFloatingOff(),
                ASJumpToHeight(height=108, silent=True),
                ASFloatingOn(),
                ASLoadMemory(PRIMARY_TEMP_700C),
                ASWalkNorthwestPixels(1),
                ASInc(SECONDARY_TEMP_7024),
                ASEndLoop(),
                ASSetSolidityBits(
                    bit_4=True,
                    cant_pass_npcs=True,
                    cant_walk_through=True,
                    bit_7=True,
                    identifier="EVENT_3501_action_queue_async_21_SUBSCRIPT_set_solidity_bits_25",
                ),
            ],
        ),
        EnableControlsUntilReturn([B]),
        CompareVarToConst(SECONDARY_TEMP_7024, 0),
        JmpIfLoadedMemoryIsAboveOrEqual0(["EVENT_3501_resume_background_event_16"]),
        SetVarToConst(TIMER_701C, 120),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E3505_BOOSTER_HILL_UNKNOWN, timer_var=TIMER_701C
        ),
        Return(),
    ]
)
