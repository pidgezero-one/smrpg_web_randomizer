# E2641_FACTORY_1ST_ROOM_LOADER_AFTER_FIGHT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 1),
        JmpIfBitClear(FAST_TRAVEL_ENABLED, ["EVENT_2641_action_queue_async_15"]),
        SummonObjectToCurrentLevel(NPC_8),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[ASShiftSouthwestPixels(8)],
            identifier="EVENT_2641_action_queue_async_15",
        ),
        SetSyncActionScript(NPC_7, A0978_RANDOMLY_FACE_SOUTHWEST),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_mold=True, is_sequence=True, looping=True
                ),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
            ],
        ),
        RunEventAsSubroutine(
            E0859_INNER_FACTORY_1ST_ROOM_POST_FIGHT_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_2641_ret_4"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2641_ret_4"]),
        RunEventAsSubroutine(E3916_INNER_FACTORY_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_2641_ret_4"),
    ]
)
