# E2793_STAR_HILL_ENTRANCE_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(target=NPC_0, subscript=[ASShiftWestPixels(16)]),
        FadeInFromBlack(sync=False),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2793_ret_2"]),
        RunEventAsSubroutine(E3903_STAR_HILL_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_2793_ret_2"),
    ]
)
