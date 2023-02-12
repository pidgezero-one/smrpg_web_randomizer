# E1295_TOWER_CHECKERBOARD_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_7,
            subscript=[ASShiftSoutheastPixels(8), ASShiftSouthwestPixels(8)],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[ASShiftSoutheastPixels(8), ASShiftSouthwestPixels(8)],
        ),
        ActionQueueSync(
            target=NPC_9,
            subscript=[ASShiftSoutheastPixels(8), ASShiftSouthwestPixels(8)],
        ),
        ActionQueueSync(
            target=NPC_10,
            subscript=[ASShiftSoutheastPixels(8), ASShiftSouthwestPixels(8)],
        ),
        ActionQueueSync(
            target=NPC_11,
            subscript=[ASShiftSoutheastPixels(8), ASShiftSouthwestPixels(8)],
        ),
        ActionQueueSync(
            target=NPC_12,
            subscript=[ASShiftSoutheastPixels(8), ASShiftSouthwestPixels(8)],
        ),
        ActionQueueSync(
            target=NPC_13,
            subscript=[ASShiftSoutheastPixels(8), ASShiftSouthwestPixels(8)],
        ),
        ActionQueueSync(
            target=NPC_14,
            subscript=[ASShiftSoutheastPixels(8), ASShiftSouthwestPixels(8)],
        ),
        ActionQueueSync(
            target=NPC_15,
            subscript=[ASShiftSoutheastPixels(8), ASShiftSouthwestPixels(8)],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[ASShiftSoutheastPixels(8), ASShiftSouthwestPixels(8)],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASShiftSoutheastPixels(8), ASShiftSouthwestPixels(8)],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASShiftSoutheastPixels(8), ASShiftSouthwestPixels(8)],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[ASShiftSoutheastPixels(8), ASShiftSouthwestPixels(8)],
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[ASShiftSoutheastPixels(8), ASShiftSouthwestPixels(8)],
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
