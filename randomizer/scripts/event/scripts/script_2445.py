# E2445_TOWER_SMALL_SAVE_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO000_SILENCE, channel=6),
        JmpIfBitClear(TEMP_7044_7, ["EVENT_2445_fade_in_from_black_async_12"]),
        EnableControlsUntilReturn([]),
        FreezeCamera(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASShadowOff(),
                ASResetProperties(),
                ASFaceSouth(),
                ASFloatingOff(),
                ASSequencePlaybackOff(),
                ASSetPriority(3),
            ],
        ),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOn(),
                ASPause(
                    1, identifier="EVENT_2445_action_queue_async_6_SUBSCRIPT_pause_1"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2445_action_queue_async_6_SUBSCRIPT_pause_1"]
                ),
                ASJumpToHeight(108),
                ASShadowOn(),
                ASWalk1StepSouth(),
                ASPause(
                    1, identifier="EVENT_2445_action_queue_async_6_SUBSCRIPT_pause_6"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2445_action_queue_async_6_SUBSCRIPT_pause_6"]
                ),
            ],
        ),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        ClearBit(TEMP_7044_7),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2445_ret_11"]),
        RunEventAsSubroutine(E3899_BOOSTER_TOWER_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_2445_ret_11"),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2445_fade_in_from_black_async_12"
        ),
        Return(),
    ]
)
