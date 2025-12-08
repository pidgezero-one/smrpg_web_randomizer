# pylint: disable=C0301

"""E1295_TOWER_CHECKERBOARD_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_7,
            subscript=[ASWalkSoutheastPixels(8), ASWalkSouthwestPixels(8)]),
        ActionQueueSync(
            target=NPC_8,
            subscript=[ASWalkSoutheastPixels(8), ASWalkSouthwestPixels(8)]),
        ActionQueueSync(
            target=NPC_9,
            subscript=[ASWalkSoutheastPixels(8), ASWalkSouthwestPixels(8)]),
        ActionQueueSync(
            target=NPC_10,
            subscript=[ASWalkSoutheastPixels(8), ASWalkSouthwestPixels(8)]),
        ActionQueueSync(
            target=NPC_11,
            subscript=[ASWalkSoutheastPixels(8), ASWalkSouthwestPixels(8)]),
        ActionQueueSync(
            target=NPC_12,
            subscript=[ASWalkSoutheastPixels(8), ASWalkSouthwestPixels(8)]),
        ActionQueueSync(
            target=NPC_13,
            subscript=[ASWalkSoutheastPixels(8), ASWalkSouthwestPixels(8)]),
        ActionQueueSync(
            target=NPC_14,
            subscript=[ASWalkSoutheastPixels(8), ASWalkSouthwestPixels(8)]),
        ActionQueueSync(
            target=NPC_15,
            subscript=[ASWalkSoutheastPixels(8), ASWalkSouthwestPixels(8)]),
        ActionQueueSync(
            target=NPC_5,
            subscript=[ASWalkSoutheastPixels(8), ASWalkSouthwestPixels(8)]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASWalkSoutheastPixels(8), ASWalkSouthwestPixels(8)]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASWalkSoutheastPixels(8), ASWalkSouthwestPixels(8)]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[ASWalkSoutheastPixels(8), ASWalkSouthwestPixels(8)]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[ASWalkSoutheastPixels(8), ASWalkSouthwestPixels(8)]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
