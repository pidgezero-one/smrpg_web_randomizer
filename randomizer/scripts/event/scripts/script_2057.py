# pylint: disable=C0301

"""E2057_MONSTROMAMA_HOUSE_1F_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASWalkSouthwestPixels(8),
                ASWalkNorthwestPixels(2),
                ASSetSequenceSpeed(SLOW),
                ASSetSpriteSequence(
                    index=0, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(SLOW),
                ASWalkNortheastPixels(3),
                ASFaceSouthwest(),
                ASSequenceLoopingOn(),
            ],
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
