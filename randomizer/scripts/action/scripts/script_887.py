"""A0887_NIMBUS_RED_BIRD"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(SLOW, identifier="ACTION_887_set_animation_speed_0"),
        SetSequenceSpeed(NORMAL),
        WalkSoutheastSteps(3),
        JmpIfRandom1of2(["ACTION_887_walk_1_step_southwest_5"]),
        Pause(60),
        Walk1StepSouthwest(identifier="ACTION_887_walk_1_step_southwest_5"),
        JmpIfRandom1of2(["ACTION_887_shift_northwest_steps_8"]),
        Pause(30),
        WalkNorthwestSteps(3, identifier="ACTION_887_shift_northwest_steps_8"),
        JmpIfRandom1of2(["ACTION_887_walk_1_step_northeast_11"]),
        Pause(30),
        Walk1StepNortheast(identifier="ACTION_887_walk_1_step_northeast_11"),
        Jmp(["ACTION_887_set_animation_speed_0"]),
    ]
)
