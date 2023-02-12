# E2384_GARDENERS_HOUSE_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetPriority(3),
                ASShiftNorthPixels(6),
                ASSetSpriteSequence(
                    index=14, is_mold=True, is_sequence=True, looping=True
                ),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetPriority(3),
                ASShiftEastPixels(5),
                ASShiftNorthPixels(3),
                ASSetSpriteSequence(
                    index=14, is_mold=True, is_sequence=True, looping=True
                ),
            ],
        ),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_mold=True, is_sequence=True, looping=True
                )
            ],
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
