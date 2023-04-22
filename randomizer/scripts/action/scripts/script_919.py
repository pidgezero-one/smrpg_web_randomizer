"""A0919_SHIP_FIRST_NOTE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(3),
        SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
        Return(),
    ]
)
