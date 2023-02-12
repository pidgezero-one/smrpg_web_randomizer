# E3769_NIMBUS_CASTLE_LIBERATED_BRIDGE_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_1,
            subscript=[ASTransferXYZFPixels(x=0, y=0, z=2, direction=EAST)],
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
