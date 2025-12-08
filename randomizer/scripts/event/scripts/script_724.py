# pylint: disable=C0301

"""E0724_NIMBUS_CROCO_HOUSE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_0,
            R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING,
            ["EVENT_257_fade_in_from_black_async_0"]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASTransferXYZFPixels(x=0, y=0, z=2, direction=EAST)]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
