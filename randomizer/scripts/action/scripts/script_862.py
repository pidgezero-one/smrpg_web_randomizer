"""A0862_ABYSS_1ST_BOSS_FIGHT_CAMERA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(FASTER, identifier="ACTION_862_set_animation_speed_0"),
        WalkEastPixels(4),
        WalkWestPixels(8),
        WalkEastPixels(4),
        Jmp(["ACTION_862_set_animation_speed_0"]),
    ]
)
