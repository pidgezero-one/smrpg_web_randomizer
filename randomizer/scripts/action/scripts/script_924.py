"""A0924_SEA_ZEOSTAR"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToPressedButton(),
        JmpIf700CAnyBitsSet(bits=[], destinations=["ACTION_924_set_sprite_sequence_4"]),
        SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
        Return(),
        SetSpriteSequence(
            index=4,
            is_mold=True,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_924_set_sprite_sequence_4"),
        Return(),
    ]
)
