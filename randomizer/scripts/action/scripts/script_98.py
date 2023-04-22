"""A0098_WALK_RANDOM_DIRECTIONS_NO_SOLIDITY_CHANGE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(VERY_SLOW, identifier="ACTION_98_set_animation_speed_0"),
        Walk1StepSouthwest(),
        JmpIfRandom1of2(["ACTION_98_pause_6"]),
        Walk1StepNortheast(identifier="ACTION_98_walk_1_step_northeast_3"),
        JmpIfRandom1of2(["ACTION_98_pause_12"]),
        Jmp(["ACTION_98_set_animation_speed_0"]),
        Pause(30, identifier="ACTION_98_pause_6"),
        FaceNorthwest(),
        Pause(30),
        FaceSoutheast(),
        Pause(30),
        Jmp(["ACTION_98_walk_1_step_northeast_3"]),
        Pause(30, identifier="ACTION_98_pause_12"),
        FaceSoutheast(),
        Pause(30),
        FaceNorthwest(),
        Pause(30),
        Jmp(["ACTION_98_set_animation_speed_0"]),
    ]
)
