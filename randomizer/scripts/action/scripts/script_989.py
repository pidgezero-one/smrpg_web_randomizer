"""A0989_SMITHY_COMPONENT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
        Jmp(["ACTION_988_set_animation_speed_3"]),
    ]
)
