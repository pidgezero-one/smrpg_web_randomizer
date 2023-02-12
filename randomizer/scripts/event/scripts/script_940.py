# E0940_STATUE_SUBROUTINE_2

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASShiftToXYCoords(x=7, y=66),
                ASSetSpriteSequence(
                    index=0, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(20),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=False),
                ASPause(45),
            ],
        ),
        Return(),
    ]
)
