"""A0440_SHIP_2ND_GRAPER_ROOM_DRY_BONES"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(NORMAL, identifier="ACTION_440_set_animation_speed_0"),
        SetWalkingSpeed(SLOW),
        Walk1StepFDirection(),
        TurnRandomDirection(),
        Jmp(["ACTION_440_set_animation_speed_0"]),
    ]
)
