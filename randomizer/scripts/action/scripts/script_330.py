"""A0330_MARRYMORE_HEAD_CHEF"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(NORMAL, identifier="ACTION_330_set_animation_speed_0"),
        SetSequenceSpeed(FAST),
        WalkSoutheastSteps(3),
        FaceSouthwest(),
        SetSpriteSequence(index=3, is_sequence=True, looping=True),
        Pause(20),
        ResetProperties(),
        WalkNorthwestSteps(3),
        Pause(60),
        JmpIfRandom1of2(["ACTION_330_set_animation_speed_0"]),
        WalkSouthwestSteps(2, identifier="ACTION_330_shift_southwest_steps_10"),
        FaceNorthwest(),
        Pause(30),
        WalkNortheastSteps(2),
        FaceNorthwest(),
        Pause(60),
        JmpIfRandom1of2(["ACTION_330_shift_southwest_steps_10"]),
        Jmp(["ACTION_330_set_animation_speed_0"]),
    ]
)
