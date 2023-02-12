# E2476_BEAN_VALLEY_5_PIPE_AREA_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SummonObjectToSpecificLevel(
            NPC_2, R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM
        ),
        ActionQueueSync(
            target=NPC_0, subscript=[ASShiftSouthPixels(1), ASShiftSouthwestPixels(4)]
        ),
        ActionQueueSync(
            target=NPC_1, subscript=[ASShiftZDownPixels(1), ASShiftSouthwestPixels(4)]
        ),
        ActionQueueSync(
            target=NPC_3, subscript=[ASShiftZDownPixels(1), ASShiftSouthwestPixels(4)]
        ),
        ActionQueueSync(
            target=NPC_4, subscript=[ASShiftZDownPixels(1), ASShiftSouthwestPixels(4)]
        ),
        ActionQueueSync(
            target=NPC_5, subscript=[ASShiftZDownPixels(1), ASShiftSouthwestPixels(4)]
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASShiftSoutheastPixels(7),
                ASShiftSouthwestPixels(1),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASShiftSoutheastPixels(7),
                ASShiftSouthwestPixels(1),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASShiftSoutheastPixels(7),
                ASShiftSouthwestPixels(1),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_10,
            subscript=[
                ASShiftSoutheastPixels(7),
                ASShiftSouthwestPixels(1),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_11,
            subscript=[
                ASShiftSoutheastPixels(7),
                ASShiftSouthwestPixels(1),
                ASVisibilityOff(),
            ],
        ),
        RunBackgroundEvent(
            event_id=E2477_BEAN_VALLEY_PIRANHA_PLANT_ANIMATIONS,
            return_on_level_exit=True,
        ),
        JmpIfBitClear(TEMP_7044_7, ["EVENT_2476_fade_in_from_black_async_15"]),
        RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2476_ret_14"]),
        RunEventAsSubroutine(E3911_BEAN_VALLEY_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_2476_ret_14"),
        FadeInFromBlack(
            sync=False, identifier="EVENT_2476_fade_in_from_black_async_15"
        ),
        JmpIfBitClear(DIRECTIONAL_7047_0, ["EVENT_2476_ret_21"]),
        ClearBit(DIRECTIONAL_7047_0),
        FreezeCamera(),
        SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
        UnfreezeCamera(),
        Return(identifier="EVENT_2476_ret_21"),
    ]
)
