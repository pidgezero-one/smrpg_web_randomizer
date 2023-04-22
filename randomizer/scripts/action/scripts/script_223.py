"""A0223_BIG_TOAD_SLEEPING"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(SLOW),
        SetSpriteSequence(index=5, is_sequence=True, looping=True),
        TransferXYZFPixels(x=250, y=252, z=0, direction=EAST),
        Return(),
    ]
)
