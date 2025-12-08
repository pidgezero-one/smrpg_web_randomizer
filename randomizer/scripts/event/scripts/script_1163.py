# pylint: disable=C0301

"""E1163_SEASIDE_LIBERATED_BEACH"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASSetPriority(3),
                ASShiftZDownPixels(6),
                ASWalkNorthwestPixels(2),
                ASFaceSouthwest(),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
                ASShadowOff(),
                ASPause(1),
            ]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
