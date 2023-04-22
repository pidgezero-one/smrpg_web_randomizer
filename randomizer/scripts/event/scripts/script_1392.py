# pylint: disable=C0301

"""E1392_MARIOS_HOUSE_INTERIOR_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASSetWalkingSpeed(VERY_FAST), ASWalkSouthwestPixels(2)],
        ),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[ASSetWalkingSpeed(VERY_FAST), ASWalkNorthPixels(4)],
        ),
        PaletteSet(palette_set=33, row=7),
        PlayMusicAtDefaultVolume(M14_MARIOS_PAD),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
