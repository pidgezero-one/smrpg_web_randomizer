"""A0714_LANDS_END_SLOW_RANDOM_MOVING_ENEMIES"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 457, ["ACTION_714_set_animation_speed_19"]
        ),
        SetPriority(3),
        SequenceLoopingOn(),
        ShadowOn(),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(VERY_SLOW),
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 65517),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(1),
        EndLoop(),
        TurnClockwise45Degrees(identifier="ACTION_714_turn_clockwise_45_degrees_12"),
        WalkFDirectionSteps(2),
        TurnRandomDirection(),
        WalkFDirectionSteps(2),
        FaceMario(),
        Walk1StepFDirection(),
        Jmp(["ACTION_714_turn_clockwise_45_degrees_12"]),
        SetWalkingSpeed(SLOW, identifier="ACTION_714_set_animation_speed_19"),
        SetSequenceSpeed(NORMAL),
        FaceMario(identifier="ACTION_714_face_mario_21"),
        WalkFDirectionSteps(2),
        TurnRandomDirection(),
        Walk1StepFDirection(),
        TurnClockwise45Degrees(),
        Walk1StepFDirection(),
        Jmp(["ACTION_714_face_mario_21"]),
    ]
)
