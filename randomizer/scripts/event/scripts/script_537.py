# pylint: disable=C0301

"""E0537_ROSE_TOWN_TREASURE_HOUSE_2F_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASTransferXYZFPixels(x=248, y=252, z=0, direction=EAST),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
            ],
        ),
        FadeOutMusicToVolume(duration=1, volume=96),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
