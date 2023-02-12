# E2576_TOWER_8BIT_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(target=NPC_1, subscript=[ASShiftNorthwestPixels(4)]),
        ActionQueueSync(target=NPC_2, subscript=[ASShiftNorthwestPixels(4)]),
        ActionQueueSync(target=NPC_3, subscript=[ASShiftNortheastPixels(4)]),
        ActionQueueAsync(target=NPC_4, subscript=[ASShiftNortheastPixels(4)]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
