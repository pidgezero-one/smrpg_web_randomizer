"""A0906_COIN_CHEST"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOff(),
        Pause(9),
        VisibilityOn(),
        SetSpriteSequence(index=2, is_sequence=True, looping=True),
        ShiftZUpSteps(2),
        VisibilityOff(),
        Return(),
    ]
)
