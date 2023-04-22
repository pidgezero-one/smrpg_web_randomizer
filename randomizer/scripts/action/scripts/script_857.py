"""A0857_PLAYER_DENIES_GARDENER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(),
        SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
        Pause(16),
        SetSequenceSpeed(VERY_FAST),
        PlaySound(sound=SO056_SHAKE_HEAD, channel=4),
        SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True),
        Pause(24),
        SetSequenceSpeed(NORMAL),
        SetSpriteSequence(
            index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        SequenceLoopingOff(),
        Return(),
    ]
)
