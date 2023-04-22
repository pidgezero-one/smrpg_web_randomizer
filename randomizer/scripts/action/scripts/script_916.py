"""A0916_SEQ_1_FALLING"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOff(),
        SetSpriteSequence(index=1, is_sequence=True, looping=True),
        Jmp(["ACTION_917_pause_2"]),
    ]
)
