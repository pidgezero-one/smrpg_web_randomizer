# pylint: disable=C0301

"""E1341_ELDER_KEY_PRIZE_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkNortheastPixels(9),
                ASWalkNorthwestPixels(5),
                ASFaceSoutheast(),
                ASObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
            ]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
