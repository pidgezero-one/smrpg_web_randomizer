"""A0483_FOREST_OBTAINABLE_MUSHROOM"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(3),
        SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
        Return(),
    ]
)
