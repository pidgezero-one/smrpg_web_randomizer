"""A0385_LOOK_UP_AT_TOWER_SEESAW_CHEST"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceSouth(),
        Pause(2),
        FaceSouthwest(),
        Pause(2),
        FaceWest(),
        Pause(2),
        FaceNorthwest(),
        Pause(2),
        FaceNorth(),
        Pause(2),
        FaceNortheast(),
        Pause(2),
        FaceEast(),
        Pause(2),
        FaceSoutheast(),
        Pause(6),
        SetSpriteSequence(index=10, sprite_offset=2, is_sequence=True, looping=False),
        Pause(64),
        SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
        FaceSouth(),
        ResetProperties(),
        Return(),
    ]
)
