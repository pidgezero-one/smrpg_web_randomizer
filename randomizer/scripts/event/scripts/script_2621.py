# pylint: disable=C0301

"""E2621_FACTORY_3RD_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunBackgroundEvent(
            event_id=E2620_FACTORY_3RD_ROOM_BACKGROUND_NPCS_BONK_CONVEYOR,
            return_on_level_exit=True),
        JmpIfObjectNotInSpecificLevel(
            NPC_10, R472_FACTORY_GROUNDS_AREA_03, ["EVENT_2621_jmp_if_bit_clear_3"]
        ),
        ActionQueueSync(target=NPC_10, subscript=[ASWalkNortheastPixels(8)]),
        JmpIfBitClear(
            TEMP_7044_7,
            ["EVENT_2621_sequence_setter_2"],
            identifier="EVENT_2621_jmp_if_bit_clear_3"),
        EnableControls([]),
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
            ]),
        RunEventAsSubroutine(
            E0857_INNER_FACTORY_3RD_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOn(),
                ASPause(
                    1, identifier="EVENT_2621_action_queue_async_8_SUBSCRIPT_pause_1"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2621_action_queue_async_8_SUBSCRIPT_pause_1"]
                ),
                ASJumpToHeight(108),
                ASShadowOn(),
                ASWalk1StepSouth(),
                ASPause(
                    1, identifier="EVENT_2621_action_queue_async_8_SUBSCRIPT_pause_6"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2621_action_queue_async_8_SUBSCRIPT_pause_6"]
                ),
            ]),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        ClearBit(TEMP_7044_7),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2595_ret_13"]),
        RunEventAsSubroutine(E3916_INNER_FACTORY_STAR_PIECE_SIGNAL),
        Return(),
        RunEventAsSubroutine(
            E0857_INNER_FACTORY_3RD_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
            identifier="EVENT_2621_sequence_setter_2"),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
