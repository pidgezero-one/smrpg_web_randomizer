# pylint: disable=C0301

"""E0870_TEST_SCRIPT_4"""

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
                ASSetSpriteSequence(index=1, is_sequence=True, looping=False),
                ASPause(120),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=False),
                ASPause(120),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASSetSequenceSpeed(FASTER),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=False),
                ASPause(120),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASSetSequenceSpeed(VERY_FAST),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=False),
                ASPause(120),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASSetSequenceSpeed(FASTEST),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=False),
                ASPause(120),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASMaximizeSequenceSpeed(),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=False),
                ASPause(120),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASMaximizeSequenceSpeed86(),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=False),
                ASPause(120),
                ASSetSpriteSequence(
                    index=0, is_mold=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        Return(),
    ]
)
