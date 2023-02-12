# E2060_MONSTROMAMA_HOUSE_2F_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASShiftNorthwestPixels(3),
                ASShiftNortheastPixels(14),
                ASSetSpriteSequence(
                    index=9,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASShadowOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASShiftNorthwestPixels(5),
                ASShiftSouthwestPixels(3),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASShiftNortheastPixels(5),
                ASShiftSoutheastPixels(3),
                ASFaceSouthwest(),
                ASSequenceLoopingOn(),
            ],
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
