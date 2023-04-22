"""A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(identifier="ACTION_384_sequence_looping_on_0"),
        SetSpriteSequence(index=6, is_sequence=True, looping=True),
        Pause(16),
        SetSequenceSpeed(VERY_FAST),
        PlaySound(sound=SO056_SHAKE_HEAD, channel=4),
        SetSpriteSequence(index=8, is_sequence=True, looping=True),
        Pause(24),
        SetSequenceSpeed(NORMAL),
        SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
        SequenceLoopingOff(),
        Return(),
    ]
)
