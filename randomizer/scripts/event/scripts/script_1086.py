# pylint: disable=C0301

"""E1086_MELODY_BAY_SWIM_ANIMATION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PauseActionScript(MARIO),
        UnfreezeCamera(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNortheast(),
                ASJumpToHeight(64),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\x00\x02\x00\xff")),
                ASPause(16),
                ASBPL262728(),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=14,
                    sprite_offset=1,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                )
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO093_JUMP_INTO_WATER, channel=6),
                ASPause(10),
                ASWalkToXYCoords(x=15, y=32),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNortheast(),
                ASPause(10),
                ASJumpToHeight(64),
                ASDb(bytearray(b" \x03")),
                ASDb(bytearray(b"$\x00\x02\x00\xff")),
                ASPause(16),
                ASBPL262728(),
            ],
        ),
        Return(),
    ]
)
