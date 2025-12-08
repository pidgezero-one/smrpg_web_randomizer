# pylint: disable=C0301

"""E2060_MONSTROMAMA_HOUSE_2F_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASWalkNorthwestPixels(3),
                ASWalkNortheastPixels(14),
                ASSetSpriteSequence(
                    index=9,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASShadowOff(),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASWalkNorthwestPixels(5),
                ASWalkSouthwestPixels(3),
            ]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASWalkNortheastPixels(5),
                ASWalkSoutheastPixels(3),
                ASFaceSouthwest(),
                ASSequenceLoopingOn(),
            ]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
