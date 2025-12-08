# pylint: disable=C0301

"""E0677_MARRYMORE_UNOCCUPIED_SANCTUARY_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_8,
            subscript=[ASTransferXYZFPixels(x=8, y=252, z=0, direction=EAST)]),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[ASTransferXYZFPixels(x=252, y=2, z=0, direction=EAST)]),
        ActionQueueAsync(
            target=NPC_12,
            subscript=[ASTransferXYZFPixels(x=252, y=2, z=0, direction=EAST)]),
        Pause(1),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASTransferXYZFPixels(x=4, y=4, z=0, direction=EAST)]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
