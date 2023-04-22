# pylint: disable=C0301

"""E0297_MUSHROOM_KINGDOM_RUNNING_KID"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfMarioOnAnObjectOrNot(
            [
                "EVENT_297_set_7000_to_current_level_9",
                "EVENT_297_set_7000_to_current_level_9",
            ]
        ),
        RunDialog(
            dialog_id=DI0534_MUSHROOM_KINGDOM_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        Set7000ToCurrentLevel(identifier="EVENT_297_set_7000_to_current_level_9"),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 495, ["EVENT_256_ret_0"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 51, ["EVENT_256_ret_0"]),
        ResumeActionScript(MEM_70A8),
        Pause(1, identifier="EVENT_297_pause_13"),
        JmpIfMarioInAir(["EVENT_297_pause_13"]),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
        StartLoopNTimes(239),
        Pause(1),
        JmpIfMarioInAir(["EVENT_256_ret_0"]),
        EndLoop(),
        EnableControlsUntilReturn([]),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 191, ["EVENT_297_set_7000_to_object_coord_25"]
        ),
        Set7000ToObjectCoord(target_npc=NPC_6, coord=COORD_F, pixel=True),
        Jmp(["EVENT_297_set_7000_short_mem_to_7000_26"]),
        Set7000ToObjectCoord(
            target_npc=NPC_7,
            coord=COORD_F,
            pixel=True,
            identifier="EVENT_297_set_7000_to_object_coord_25",
        ),
        CopyVarToVar(
            from_var=PRIMARY_TEMP_7000,
            to_var=PRIMARY_TEMP_700C,
            identifier="EVENT_297_set_7000_short_mem_to_7000_26",
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSequencePlaybackOff(),
                ASJumpToHeight(64),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    1,
                    [
                        "EVENT_297_action_queue_async_27_SUBSCRIPT_walk_1_step_southwest_7"
                    ],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    5,
                    [
                        "EVENT_297_action_queue_async_27_SUBSCRIPT_walk_1_step_northeast_9"
                    ],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    3,
                    [
                        "EVENT_297_action_queue_async_27_SUBSCRIPT_walk_1_step_northwest_11"
                    ],
                ),
                ASWalk1StepSoutheast(),
                ASJmp(["EVENT_297_action_queue_async_27_SUBSCRIPT_pause_12"]),
                ASWalk1StepSouthwest(
                    identifier="EVENT_297_action_queue_async_27_SUBSCRIPT_walk_1_step_southwest_7"
                ),
                ASJmp(["EVENT_297_action_queue_async_27_SUBSCRIPT_pause_12"]),
                ASWalk1StepNortheast(
                    identifier="EVENT_297_action_queue_async_27_SUBSCRIPT_walk_1_step_northeast_9"
                ),
                ASJmp(["EVENT_297_action_queue_async_27_SUBSCRIPT_pause_12"]),
                ASWalk1StepNorthwest(
                    identifier="EVENT_297_action_queue_async_27_SUBSCRIPT_walk_1_step_northwest_11"
                ),
                ASPause(
                    1, identifier="EVENT_297_action_queue_async_27_SUBSCRIPT_pause_12"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_297_action_queue_async_27_SUBSCRIPT_pause_12"]
                ),
                ASSequencePlaybackOn(),
                ASStartLoopNTimes(7),
                ASTurnClockwise45DegreesNTimes(1),
                ASPause(2),
                ASEndLoop(),
                ASTurnClockwise45DegreesNTimes(
                    1,
                    identifier="EVENT_297_action_queue_async_27_SUBSCRIPT_turn_clockwise_45_degrees_n_times_19",
                ),
                ASPause(2),
                ASSet700CToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    7,
                    ["EVENT_297_action_queue_async_27_SUBSCRIPT_start_loop_n_times_24"],
                ),
                ASJmp(
                    [
                        "EVENT_297_action_queue_async_27_SUBSCRIPT_turn_clockwise_45_degrees_n_times_19"
                    ]
                ),
                ASStartLoopNTimes(
                    2,
                    identifier="EVENT_297_action_queue_async_27_SUBSCRIPT_start_loop_n_times_24",
                ),
                ASSetSpriteSequence(
                    index=19,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(4),
                ASSetSpriteSequence(
                    index=3,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(4),
                ASSetSpriteSequence(
                    index=23,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(6),
                ASSetSpriteSequence(
                    index=3,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(2),
                ASEndLoop(),
                ASSetSpriteSequence(
                    index=19,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASPause(2),
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=4),
                ASSetSpriteSequence(
                    index=8, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(30),
                ASResetProperties(),
            ],
        ),
        Pause(10),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
    ]
)
