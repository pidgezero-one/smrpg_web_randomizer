# pylint: disable=C0301

"""E2576_TOWER_8BIT_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(target=NPC_1, subscript=[ASWalkNorthwestPixels(4)]),
        ActionQueueSync(target=NPC_2, subscript=[ASWalkNorthwestPixels(4)]),
        ActionQueueSync(target=NPC_3, subscript=[ASWalkNortheastPixels(4)]),
        ActionQueueAsync(target=NPC_4, subscript=[ASWalkNortheastPixels(4)]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
