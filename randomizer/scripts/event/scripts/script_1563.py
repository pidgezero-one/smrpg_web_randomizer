# pylint: disable=C0301

"""E1563_LANDS_END_MARIO_OOB"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Db(bytearray(b"\xc7\x94")),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO058_INSERT, channel=4),
                ASPause(30),
                ASSetSequenceSpeed(SLOW),
                ASSetSpriteSequence(
                    index=8, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPlaySound(sound=SO034_SQUIRM_WRITHE, channel=4),
                ASPause(30),
                ASPlaySound(sound=SO034_SQUIRM_WRITHE, channel=4),
                ASPause(30),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(
                    index=6, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPlaySound(sound=SO034_SQUIRM_WRITHE, channel=4),
                ASPause(40),
                ASResetProperties(),
                ASPause(20),
                ASPlaySound(sound=SO034_SQUIRM_WRITHE, channel=4),
                ASStartLoopNTimes(3),
                ASTurnClockwise45DegreesNTimes(7),
                ASPause(3),
                ASEndLoop(),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
                ASStartLoopNTimes(4),
                ASPlaySound(sound=SO043_POP_UP_FROM_WATER, channel=6),
                ASPause(10),
                ASEndLoop(),
                ASSetSequenceSpeed(VERY_FAST),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASPlaySound(sound=SO024_TAPPING_FEET, channel=4),
                ASPause(50),
                ASSetSequenceSpeed(NORMAL),
                ASResetProperties(),
                ASJumpToHeight(112),
                ASRunAwayShift(),
                ASSetAllSpeeds(NORMAL),
            ]),
        Return(),
    ]
)
