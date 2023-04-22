"""A0351_OERLIKONS_AND_3D_MAZE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpIfVarEqualsConst(
            CURRENT_OVERWORLD_MARKER_ID, 50, ["ACTION_351_set_animation_speed_28"]
        ),
        Db(bytearray(b"\xc8\x00")),
        TransferTo70167018(),
        SetPriority(3),
        SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
        VisibilityOn(identifier="ACTION_351_visibility_on_23"),
        Pause(30),
        VisibilityOff(),
        Pause(30),
        Jmp(["ACTION_351_visibility_on_23"]),
        SetWalkingSpeed(SLOW, identifier="ACTION_351_set_animation_speed_28"),
        SetSequenceSpeed(FAST),
        Walk1StepFDirection(),
        TurnRandomDirection(),
        Walk1StepFDirection(),
        JmpIfRandom1of2(["ACTION_351_set_animation_speed_28"]),
        FaceMario(),
        SetWalkingSpeed(NORMAL),
        SetSequenceSpeed(VERY_FAST),
        Walk1StepFDirection(),
        Jmp(["ACTION_351_set_animation_speed_28"]),
    ]
)
