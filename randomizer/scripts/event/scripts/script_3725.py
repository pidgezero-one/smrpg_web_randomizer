# E3725_NIMBUS_CASTLE_NOTE_HALLWAY_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASTransferXYZFPixels(x=4, y=2, z=28, direction=NORTHEAST),
                ASSetPriority(3),
            ],
        ),
        SetBit(NOTE_DIRECTION),
        SetSyncActionScript(NPC_2, A0977_NOTE_WITHOUT_KNIFE),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
