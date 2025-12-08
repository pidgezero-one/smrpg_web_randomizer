"""A0877_MONSTRO_THWOMP"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(
            index=1,
            is_mold=True,
            is_sequence=True,
            looping=True,
            identifier="ACTION_877_set_sprite_sequence_0"),
        Pause(5),
        SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
        Pause(5),
        SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
        Pause(5),
        SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
        Pause(60),
        SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
        Pause(5),
        SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
        Pause(5),
        SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
        Pause(5),
        SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
        Pause(140),
        Jmp(["ACTION_877_set_sprite_sequence_0"]),
    ]
)
