"""A0739_TOWER_SEESAW_CHEST_ITEM"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Pause(1),
        SetSpriteSequence(
            index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Return(),
    ]
)
