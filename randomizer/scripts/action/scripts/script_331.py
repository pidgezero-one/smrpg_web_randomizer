"""A0331_MARRYMORE_2ND_CHEF"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(NORMAL, identifier="ACTION_331_set_animation_speed_0"),
        SetSequenceSpeed(FAST),
        WalkSouthwestSteps(2),
        WalkNorthwestSteps(2),
        Pause(30),
        WalkSoutheastSteps(2),
        WalkNortheastSteps(2),
        FaceSoutheast(),
        Pause(30),
        JmpIfRandom1of2(["ACTION_331_set_animation_speed_0"]),
        SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
        Pause(20),
        ResetProperties(),
        JmpIfRandom1of2(["ACTION_331_set_animation_speed_0"]),
        WalkNorthwestSteps(2, identifier="ACTION_331_shift_northwest_steps_14"),
        Pause(60),
        WalkSoutheastSteps(2),
        Pause(60),
        JmpIfRandom1of2(["ACTION_331_shift_northwest_steps_14"]),
        SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
        Pause(20),
        ResetProperties(),
        Jmp(["ACTION_331_set_animation_speed_0"]),
    ]
)
