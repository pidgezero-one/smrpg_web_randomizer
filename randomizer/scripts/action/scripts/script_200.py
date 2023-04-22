"""A0200_COIN_SNAKE_TAIL"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(index=1, is_sequence=True, looping=True),
        Jmp(["ACTION_318_visibility_off_0"]),
    ]
)
