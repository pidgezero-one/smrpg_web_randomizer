"""A0231_RIDE_YOSHI"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceNortheast(),
        SetSpriteSequence(
            index=6, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Return(),
    ]
)
