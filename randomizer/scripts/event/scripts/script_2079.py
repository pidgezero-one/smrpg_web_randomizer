# pylint: disable=C0301

"""E2079_MONSTRO_TOWN_EXTERIOR_LOADER_FROM_SAVE_BOX"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControlsUntilReturn([]),
        FreezeCamera(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASShadowOff(),
                ASResetProperties(),
                ASFaceSouth(),
                ASFloatingOff(),
                ASSequencePlaybackOff(),
            ]),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOn(),
                ASPause(
                    1, identifier="EVENT_2079_action_queue_async_4_SUBSCRIPT_pause_1"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2079_action_queue_async_4_SUBSCRIPT_pause_1"]
                ),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASShadowOn(),
                ASJumpToHeight(165),
                ASPause(20),
                ASSetSolidityBits(cant_pass_walls=True),
                ASWalk1StepSouth(),
                ASPause(
                    1, identifier="EVENT_2079_action_queue_async_4_SUBSCRIPT_pause_10"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2079_action_queue_async_4_SUBSCRIPT_pause_10"]
                ),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ]),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        ClearBit(TEMP_7044_7),
        Return(),
    ]
)
