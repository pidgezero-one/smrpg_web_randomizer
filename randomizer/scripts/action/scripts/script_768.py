"""A0768_LANDS_END_UNDERGROUND_GECKO"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 262, ["ACTION_768_set_priority_21"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 270, ["ACTION_768_set_priority_21"]),
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 65517),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(5),
        EndLoop(),
        SequenceLoopingOn(),
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(FAST, identifier="ACTION_768_set_animation_speed_10"),
        TurnClockwise45Degrees(),
        Walk1StepFDirection(),
        SetSequenceSpeed(SLOW),
        Pause(60),
        SetSequenceSpeed(FAST),
        TurnRandomDirection(),
        Walk1StepFDirection(),
        SetSequenceSpeed(VERY_SLOW),
        Pause(30),
        Jmp(["ACTION_768_set_animation_speed_10"]),
        SetPriority(3, identifier="ACTION_768_set_priority_21"),
        SequenceLoopingOn(),
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 65517),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(2),
        EndLoop(),
        FaceMario(identifier="ACTION_768_face_mario_28"),
        SetSequenceSpeed(FAST),
        Pause(32),
        FaceMario(),
        SetSequenceSpeed(VERY_SLOW),
        Pause(32),
        Jmp(["ACTION_768_face_mario_28"]),
    ]
)
