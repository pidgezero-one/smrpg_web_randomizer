"""A0678_SAMUS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 22, ["ACTION_678_set_sprite_sequence_7"]
        ),
        SequenceLoopingOn(),
        SetSequenceSpeed(FAST),
        Pause(32),
        SetSequenceSpeed(SLOW),
        Return(),
        SetSpriteSequence(
            index=0,
            is_mold=True,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_678_set_sprite_sequence_7"),
        Pause(40),
        SetSpriteSequence(
            index=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(4),
        SetSpriteSequence(
            index=2, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(8),
        Jmp(["ACTION_678_set_sprite_sequence_7"]),
    ]
)
