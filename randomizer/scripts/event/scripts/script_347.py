# pylint: disable=C0301

"""E0347_TOADSTOOLS_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASSetWalkingSpeed(FASTEST), ASWalkSouthwestPixels(4)],
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
