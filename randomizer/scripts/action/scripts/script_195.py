"""A0195_BOMB_EXPLOSION_FASTER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
        SetSpriteSequence(index=1, looping=False),
        Pause(16),
        VisibilityOff(),
        Return(),
    ]
)
