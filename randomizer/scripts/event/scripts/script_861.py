# pylint: disable=C0301

"""E0861_DOJO_1ST_BOSS_CHALLENGE_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(height=53, silent=True),
                ASWalkNortheastSteps(1),
                ASPause(20),
                ASFixedFCoordOff(),
                ASFaceSouthwest(),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=False),
                ASPause(45),
            ],
        ),
        Return(),
    ]
)
