# pylint: disable=C0301

"""E0867_TEST_SCRIPT_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=False),
                ASPause(120),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=False),
                ASPause(120),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASSetSequenceSpeed(FASTER),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=False),
                ASPause(120),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASSetSequenceSpeed(VERY_FAST),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=False),
                ASPause(120),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASSetSequenceSpeed(FASTEST),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=False),
                ASPause(120),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASMaximizeSequenceSpeed(),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=False),
                ASPause(120),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASMaximizeSequenceSpeed86(),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=False),
                ASPause(120),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        Return(),
    ]
)
