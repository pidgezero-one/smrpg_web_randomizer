# pylint: disable=C0301

"""E0943_KEEP_SECOND_BOSS_ANIMATION_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(FASTER),
                ASFixedFCoordOn(),
                ASPause(20),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=False),
                ASPause(45),
            ]),
        Return(),
    ]
)
