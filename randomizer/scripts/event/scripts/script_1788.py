# pylint: disable=C0301

"""E1788_LANDS_END_UNDERGROUND_DOG_WALL_ROOM_LOADER_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(target=NPC_3, subscript=[ASFaceSouthwest()]),
        ActionQueueSync(target=NPC_4, subscript=[ASFaceSouthwest()]),
        ActionQueueSync(
            target=NPC_5,
            subscript=[ASFaceSouthwest(), ASObjectMemorySetBit(arg_1=0x0B, bits=[3])],
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[ASFaceSouthwest(), ASObjectMemorySetBit(arg_1=0x0B, bits=[3])],
        ),
        Return(),
    ]
)
