"""A0918_SEQ_5_FALLING"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOff(),
        SetSpriteSequence(index=5, is_sequence=True, looping=True),
        Jmp(["ACTION_917_pause_2"]),
    ]
)
