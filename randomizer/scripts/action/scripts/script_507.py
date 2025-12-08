"""A0507_SPARKLE_LINE_LOOPED"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(
            index=15,
            is_mold=True,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_507_set_sprite_sequence_0"),
        Pause(8),
        SetSpriteSequence(
            index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(8),
        Jmp(["ACTION_507_set_sprite_sequence_0"]),
    ]
)
