"""A0441_MINES_QUAD_BOMB_SQUAD"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(NORMAL, identifier="ACTION_441_set_animation_speed_0"),
        FaceSoutheast(),
        FixedFCoordOff(),
        SequenceLoopingOn(),
        SetWalkingSpeed(SLOW),
        WalkSoutheastSteps(7),
        FixedFCoordOn(),
        WalkNorthwestSteps(7),
        Jmp(["ACTION_441_set_animation_speed_0"]),
    ]
)
