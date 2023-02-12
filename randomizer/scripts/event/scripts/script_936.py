# E0936_PECK_SUBROUTINE_LEFT_STATUE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSequencePlaybackOn(),
                ASSetAllSpeeds(NORMAL),
                ASPause(3),
                ASFaceSouthwest(),
                ASSetSpriteSequence(
                    index=0, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(15),
                ASSequenceLoopingOn(),
                ASSetSpriteSequence(index=3, looping=False),
                ASPause(19),
                ASSetSpriteSequence(
                    index=0,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASFaceSoutheast(),
            ],
        ),
        Return(),
    ]
)
