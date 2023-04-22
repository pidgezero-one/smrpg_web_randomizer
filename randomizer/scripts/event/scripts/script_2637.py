# pylint: disable=C0301

"""E2637_CASINO_GRATE_GUY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASSequenceLoopingOff()],
            identifier="EVENT_2637_action_queue_sync_9",
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASOverwriteSolidity(),
                ASWalkToXYCoords(x=4, y=16),
                ASFaceNortheast(),
            ],
        ),
        RunDialog(
            dialog_id=DI3304_AWAIT_LEFT_OR_RIGHT,
            above_object=Bowser,
            closable=False,
            sync=True,
            multiline=True,
            use_background=False,
        ),
        Set7000ToPressedButton(identifier="EVENT_2637_set_7000_to_pressed_button_13"),
        Pause(1),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2637_close_dialog_18"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_2637_close_dialog_18_"]),
        Jmp(["EVENT_2637_set_7000_to_pressed_button_13"]),
        CloseDialog(identifier="EVENT_2637_close_dialog_18"),
        Pause(16),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=11,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                )
            ],
        ),
        JmpIfRandom1of2(["EVENT_2637_action_queue_sync_26"]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASSetSpriteSequence(index=3, is_sequence=True, looping=True)],
        ),
        Pause(30),
        RunEventAsSubroutine(E2646_CASINO_GRATE_GUY_AWAIT_BUTTON),
        Jmp(["EVENT_2637_play_sound_40"]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASSetSpriteSequence(index=2, is_sequence=True, looping=True)],
            identifier="EVENT_2637_action_queue_sync_26",
        ),
        Pause(30),
        RunEventAsSubroutine(E2646_CASINO_GRATE_GUY_AWAIT_BUTTON),
        Jmp(["EVENT_2637_play_sound_49"]),
        CloseDialog(identifier="EVENT_2637_close_dialog_18_"),
        Pause(16),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=10,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                )
            ],
        ),
        JmpIfRandom1of2(["EVENT_2637_action_queue_sync_37"]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASSetSpriteSequence(index=3, is_sequence=True, looping=True)],
        ),
        Pause(30),
        RunEventAsSubroutine(E2646_CASINO_GRATE_GUY_AWAIT_BUTTON),
        Jmp(["EVENT_2637_play_sound_49"]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASSetSpriteSequence(index=2, is_sequence=True, looping=True)],
            identifier="EVENT_2637_action_queue_sync_37",
        ),
        Pause(30),
        RunEventAsSubroutine(E2646_CASINO_GRATE_GUY_AWAIT_BUTTON),
        Jmp(["EVENT_2637_play_sound_40"]),
        PlaySound(
            sound=SO088_WRONG_SIGNAL, channel=6, identifier="EVENT_2637_play_sound_40"
        ),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        ActionQueueSync(
            target=NPC_1, subscript=[ASResetProperties(), ASSequenceLoopingOn()]
        ),
        Jmp(["EVENT_2637_run_dialog_79"]),
        PlaySound(
            sound=SO087_CORRECT_SIGNAL, channel=6, identifier="EVENT_2637_play_sound_49"
        ),
        Pause(25),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        ActionQueueSync(
            target=NPC_1, subscript=[ASResetProperties(), ASSequenceLoopingOn()]
        ),
        JmpIfBitSet(CASINO_PRIZE_WON, ["EVENT_2637_set_var_to_random_grant"]),
        Inc(UNKNOWN_70EF),
        CopyVarToVar(from_var=UNKNOWN_70EF, to_var=PRIMARY_TEMP_7000),
        RunEventAsSubroutine(E2650_CASINO_GRATE_GUY_CHECK_IF_SIDEQUEST_COMPLETED),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2637_run_dialog_135"]),
        RunEventAsSubroutine(
            E2649_CASINO_GRATE_GUY_RANDOM_PRIZE_GRANTER,
            identifier="EVENT_2637_set_var_to_random_grant",
        ),
        Jmp(["EVENT_2637_run_dialog_79"]),
        RunDialog(
            dialog_id=DI3308_LOOK_THE_OTHER_WAY_PRIZE,
            above_object=Bowser,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_2637_run_dialog_135",
        ),
        SetBit(CASINO_PRIZE_WON),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        RunDialog(
            dialog_id=DI3310_LOOK_THE_OTHER_WAY_RETRY,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_2637_run_dialog_79",
        ),
        JmpIfDialogOptionBSelected(["EVENT_2637_pause_138"]),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        Jmp(["EVENT_2637_action_queue_sync_9"]),
        Pause(10, identifier="EVENT_2637_pause_138"),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        Return(),
    ]
)
