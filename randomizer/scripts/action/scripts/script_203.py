"""A0203_SHIP_PASSWORD_BOSS_REVEAL"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpIfVarEqualsConst(
            CURRENT_OVERWORLD_MARKER_ID, 50, ["ACTION_203_set_animation_speed_28"]
        ),
        VisibilityOff(),
        WalkEastPixels(6),
        ShiftZUpPixels(5),
        ResetProperties(),
        FaceSouthwest(),
        Pause(60),
        VisibilityOn(),
        SetSpriteSequence(index=0, is_sequence=True, looping=False),
        Pause(16),
        PlaySound(sound=SO118_BECKONING_TENTACLE, channel=4),
        Pause(56),
        SetSpriteSequence(index=1, is_sequence=True, looping=True),
        Pause(60),
        SetSpriteSequence(index=2, is_sequence=True, looping=False),
        Pause(24),
        VisibilityOff(),
        Return(),
        SetWalkingSpeed(SLOW, identifier="ACTION_203_set_animation_speed_28"),
        SetSequenceSpeed(FAST),
        Walk1StepFDirection(),
        TurnRandomDirection(),
        Walk1StepFDirection(),
        JmpIfRandom1of2(["ACTION_203_set_animation_speed_28"]),
        FaceMario(),
        SetWalkingSpeed(NORMAL),
        SetSequenceSpeed(VERY_FAST),
        Walk1StepFDirection(),
        Jmp(["ACTION_203_set_animation_speed_28"]),
    ]
)
