# pylint: disable=C0301

"""E0683_MARRYMORE_LIBERATED_EXTERIOR_GREEN_TOAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASClearSolidityBits(cant_walk_through=True),
                ASFaceSoutheast(),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(FASTEST),
                ASWalkSouthwestPixels(2),
                ASStartLoopNTimes(2),
                ASWalkNortheastPixels(4),
                ASWalkSouthwestPixels(4),
                ASEndLoop(),
                ASWalkNortheastPixels(2),
            ],
        ),
        RunDialog(
            dialog_id=DI2200_MARRYMORE_PHOTO,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ActionQueueAsync(
            target=NPC_5, subscript=[ASSetSolidityBits(cant_walk_through=True)]
        ),
        Return(),
    ]
)
