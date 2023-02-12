# E2057_MONSTROMAMA_HOUSE_1F_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftSouthwestPixels(8),
                ASShiftNorthwestPixels(2),
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
                ASShiftNortheastPixels(3),
                ASFaceSouthwest(),
                ASSequenceLoopingOn(),
            ],
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
