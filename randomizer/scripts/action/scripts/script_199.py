"""A0199_COIN_SNAKE_HEAD"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(index=1, is_sequence=True, looping=True),
        Jmp(["ACTION_317_set_solidity_bits_0"]),
    ]
)
