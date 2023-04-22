# pylint: disable=C0301

"""E2096_HINO_MART_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0,
            subscript=[ASWalkSoutheastPixels(8), ASFaceSouthwest(), ASShadowOff()],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASWalkNorthPixels(2),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASWalkNorthPixels(2),
                ASWalkWestPixels(1),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASWalkNorthPixels(3),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
            ],
        ),
        SetBit(TEMP_7043_2),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
