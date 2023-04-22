"""A0029_POST_THRONE_FIRST_BIRD"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(SLOW),
        SequenceLoopingOn(),
        Jmp(["ACTION_98_set_animation_speed_0"]),
    ]
)
