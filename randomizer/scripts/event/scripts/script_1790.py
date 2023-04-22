# pylint: disable=C0301

"""E1790_LANDS_END_UNDERGROUND_UPPER_PIT_ROOM_LOADER_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASFaceSouthwest(),
                ASPause(8),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(FASTEST),
                ASWalkNorthwestSteps(2),
                ASFixedFCoordOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASFaceSouthwest(),
                ASPause(8),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(FASTEST),
                ASWalkSoutheastSteps(2),
                ASFixedFCoordOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASFaceSouthwest(),
                ASPause(8),
                ASPause(4),
                ASObjectMemorySetBit(arg_1=0x0B, bits=[3]),
            ],
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASFaceSouthwest(),
                ASPause(8),
                ASPause(4),
                ASObjectMemorySetBit(arg_1=0x0B, bits=[3]),
            ],
        ),
        Return(),
    ]
)
