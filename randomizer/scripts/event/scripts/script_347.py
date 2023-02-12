# E0347_TOADSTOOLS_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASSetWalkingSpeed(FASTEST), ASShiftSouthwestPixels(4)],
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
