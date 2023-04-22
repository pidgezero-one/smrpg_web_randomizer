# pylint: disable=C0301

"""E2526_STAR_HILL_1ST_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_11, subscript=[ASWalkSouthwestPixels(4), ASWalkWestPixels(5)]
        ),
        ActionQueueSync(
            target=NPC_12, subscript=[ASWalkSouthwestPixels(4), ASWalkWestPixels(6)]
        ),
        ActionQueueSync(target=NPC_13, subscript=[ASWalkWestPixels(8)]),
        ActionQueueAsync(target=NPC_14, subscript=[ASWalkSoutheastPixels(6)]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
