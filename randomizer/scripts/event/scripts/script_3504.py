# pylint: disable=C0301

"""E3504_BOOSTER_HILL_HENCHMAN_INTERACTION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopBackgroundEvent(TIMER_701C),
        ClearBit(TEMP_7043_5),
        EnableControlsUntilReturn([]),
        JmpIfMarioOnAnObjectOrNot(
            ["EVENT_3504_reset_coords_15", "EVENT_3504_set_7000_to_object_coord_4"]
        ),
        Set7000ToObjectCoord(
            target_npc=MARIO,
            coord=COORD_Z,
            pixel=True,
            identifier="EVENT_3504_set_7000_to_object_coord_4",
        ),
        CompareVarToConst(PRIMARY_TEMP_7000, 288),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3504_reset_coords_15"]),
        DisableObjectTrigger(MEM_70A8),
        ResumeActionScript(MEM_70A8),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFloatingOff(),
                ASPlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
                ASJumpToHeight(height=112, silent=True),
                ASSetSpriteSequence(
                    index=7, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASFloatingOn(),
                ASSetWalkingSpeed(FAST),
                ASVisibilityOff(
                    identifier="EVENT_3504_action_queue_async_9_SUBSCRIPT_visibility_off_7"
                ),
                ASPause(1),
                ASVisibilityOn(),
                ASCompareVarToConst(SECONDARY_TEMP_7024, 65475),
                ASJmpIfLoadedMemoryIsAboveOrEqual0(
                    ["EVENT_3504_action_queue_async_9_SUBSCRIPT_pause_15"]
                ),
                ASWalkSoutheastPixels(2),
                ASAddConstToVar(SECONDARY_TEMP_7024, 65534),
                ASJmp(["EVENT_3504_action_queue_async_9_SUBSCRIPT_visibility_off_7"]),
                ASPause(
                    1, identifier="EVENT_3504_action_queue_async_9_SUBSCRIPT_pause_15"
                ),
                ASResetProperties(),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
        ),
        EnableControlsUntilReturn([B]),
        EnableObjectTrigger(MEM_70A8),
        SetVarToConst(TIMER_701C, 2),
        RunBackgroundEventWithPauseReturnOnExit(
            event_id=E3505_BOOSTER_HILL_UNKNOWN, timer_var=TIMER_701C
        ),
        Return(),
        ResetCoords(MEM_70A8, identifier="EVENT_3504_reset_coords_15"),
        SetSyncActionScript(MEM_70A8, A0711_BOOSTER_HILL_HENCHMAN_BOUNCE),
        SetVarToConst(TEMP_7028, 48),
        Jmp(["EVENT_3501_action_queue_sync_19"]),
    ]
)
