# E2526_STAR_HILL_1ST_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_11, subscript=[ASShiftSouthwestPixels(4), ASShiftWestPixels(5)]
        ),
        ActionQueueSync(
            target=NPC_12, subscript=[ASShiftSouthwestPixels(4), ASShiftWestPixels(6)]
        ),
        ActionQueueSync(target=NPC_13, subscript=[ASShiftWestPixels(8)]),
        ActionQueueAsync(target=NPC_14, subscript=[ASShiftSoutheastPixels(6)]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
