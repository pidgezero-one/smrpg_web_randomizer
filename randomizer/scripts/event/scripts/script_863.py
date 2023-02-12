# E0863_DOJO_2ND_BOSS_CHALLENGE_DEESCALATE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASVisibilityOn(),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(FAST),
                ASShiftNortheastSteps(1),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=3, is_sequence=True, looping=False),
                ASPause(18),
            ],
        ),
        Return(),
    ]
)
