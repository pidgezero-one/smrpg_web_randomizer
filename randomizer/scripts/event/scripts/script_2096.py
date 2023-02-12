# E2096_HINO_MART_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASShiftSoutheastPixels(8), ASFaceSouthwest(), ASShadowOff()],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftNorthPixels(2),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASShiftNorthPixels(2),
                ASShiftWestPixels(1),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASShiftNorthPixels(3),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
            ],
        ),
        SetBit(TEMP_7043_2),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
