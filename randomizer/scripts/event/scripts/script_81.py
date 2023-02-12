# E0081_MARIO_LANDS_SUBROUTINE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
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
                    1, identifier="EVENT_81_action_queue_async_4_SUBSCRIPT_pause_1"
                ),
                ASJmpIfMarioInAir(["EVENT_81_action_queue_async_4_SUBSCRIPT_pause_1"]),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASJumpToHeight(108),
                ASShadowOn(),
                ASWalk1StepSouth(),
                ASPause(
                    1, identifier="EVENT_81_action_queue_async_4_SUBSCRIPT_pause_8"
                ),
                ASJmpIfMarioInAir(["EVENT_81_action_queue_async_4_SUBSCRIPT_pause_8"]),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
        ),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        ClearBit(TEMP_7044_7),
        Return(identifier="EVENT_81_ret_9"),
    ]
)
