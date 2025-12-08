# pylint: disable=C0301

"""E2049_MONSTRO_SUPER_JUMP_HOUSE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASWalkNortheastPixels(7),
                ASWalkSoutheastPixels(2),
                ASFaceSouthwest(),
                ASSetSequenceSpeed(SLOW),
                ASSequenceLoopingOn(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASWalkNorthwestPixels(4),
                ASFaceSoutheast(),
                ASSetSequenceSpeed(SLOW),
                ASSequenceLoopingOn(),
            ]),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASSetSequenceSpeed(SLOW),
                ASSetSpriteSequence(index=7, is_sequence=True, looping=True),
            ]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
