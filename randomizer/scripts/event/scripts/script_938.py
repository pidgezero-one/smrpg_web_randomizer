# pylint: disable=C0301

"""E0938_PECK_SUBROUTINE_RIGHT_STATUE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetSpriteSequence(index=0, is_mold=True, looping=True),
                ASFaceSouthwest(),
            ],
        ),
        Return(),
    ]
)
