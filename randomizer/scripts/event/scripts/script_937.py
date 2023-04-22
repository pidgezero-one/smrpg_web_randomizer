# pylint: disable=C0301

"""E0937_PECK_SUBROUTINE_MIDDLE_STATUE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSequencePlaybackOn(),
                ASSequenceLoopingOn(),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=3, is_sequence=True, looping=False),
                ASPause(20),
                ASSequenceLoopingOff(),
            ],
        ),
        Return(),
    ]
)
