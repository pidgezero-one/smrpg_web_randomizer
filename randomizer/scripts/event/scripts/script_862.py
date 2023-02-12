# E0862_DOJO_2ND_BOSS_CHALLENGE_SUBROUTINE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(height=53, silent=True),
                ASShiftNortheastSteps(1),
                ASPause(20),
                ASFixedFCoordOff(),
                ASFaceSouthwest(),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=3, is_sequence=True, looping=False),
                ASPause(45),
            ],
        ),
        Return(),
    ]
)
