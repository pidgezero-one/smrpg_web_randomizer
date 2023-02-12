# E3811_NIMBUS_INNER_CELLAR_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_1,
            subscript=[ASTransferXYZFPixels(x=0, y=0, z=2, direction=EAST)],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[ASTransferXYZFPixels(x=0, y=0, z=2, direction=EAST)],
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
