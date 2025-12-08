# pylint: disable=C0301

"""E0552_ROSE_TOWN_OCCUPIED_INTRO_TOAD_MOVEMENT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            ROSE_TOWN_WATER_PUMPERS_POSITION, ["EVENT_257_fade_in_from_black_async_0"]
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=14, y=11, z=0, direction=EAST),
                ASFaceNortheast(),
            ]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
