# pylint: disable=C0301

"""E0939_STATUE_SUBROUTINE_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASShiftToXYCoords(x=2, y=56),
                ASWalkSouthwestPixels(5),
                ASWalkSoutheastPixels(16),
                ASSequencePlaybackOff(),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASVisibilityOn(),
                ASPause(31),
                ASSetSpriteSequence(
                    index=5, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(31),
                ASSetSequenceSpeed(SLOW),
                ASSequencePlaybackOn(),
                ASSequenceLoopingOn(),
                ASSetSpriteSequence(index=4, looping=False, mirror_sprite=True),
                ASPause(66),
                ASSequenceLoopingOff(),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(17),
            ],
        ),
        Return(),
    ]
)
