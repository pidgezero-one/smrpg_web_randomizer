# E2080_MUSTY_FEARS_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(INVISIBLE_ITEMS_ANYWHERE, ["EVENT_2080_action_queue_async_1"]),
        ActionQueueAsync(target=NPC_1, subscript=[ASVisibilityOff()]),
        ActionQueueAsync(
            target=NPC_2, subscript=[ASVisibilityOn(), ASSequenceLoopingOn()]
        ),
        ActionQueueAsync(
            target=NPC_3, subscript=[ASVisibilityOn(), ASSequenceLoopingOn()]
        ),
        ActionQueueAsync(
            target=NPC_4, subscript=[ASVisibilityOn(), ASSequenceLoopingOn()]
        ),
        Jmp(["EVENT_2080_fade_in_from_black_async_2"]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASShiftNorthwestPixels(4),
                ASShiftNorthPixels(9),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASSetVRAMPriority(NORMAL_PRIORITY),
            ],
            identifier="EVENT_2080_action_queue_async_1",
        ),
        FadeInFromBlack(sync=False, identifier="EVENT_2080_fade_in_from_black_async_2"),
        RunEventAsSubroutine(E0091_INVISIBLE_ITEM_SUMMONER),
        Return(),
    ]
)
