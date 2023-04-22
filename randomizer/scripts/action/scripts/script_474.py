"""A0474_BANDITS_WAY_2_CHEST_ROOM_CHEST"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(),
        Set700CToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 78, ["ACTION_474_set_priority_27"]),
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 65517),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(9),
        EndLoop(),
        SetAllSpeeds(SLOW, identifier="ACTION_474_set_animation_speed_8"),
        WalkFDirectionSteps(2),
        Pause(21),
        TurnClockwise45DegreesNTimes(2),
        Walk1StepFDirection(),
        TurnClockwise45DegreesNTimes(2),
        WalkFDirectionSteps(2),
        Pause(37),
        StartLoopNTimes(1),
        TurnClockwise45DegreesNTimes(6),
        Walk1StepFDirection(),
        TurnClockwise45DegreesNTimes(6),
        WalkFDirectionSteps(2),
        Pause(21),
        EndLoop(),
        TurnClockwise45DegreesNTimes(2),
        Walk1StepFDirection(),
        TurnClockwise45DegreesNTimes(2),
        Jmp(["ACTION_474_set_animation_speed_8"]),
        SetPriority(3, identifier="ACTION_474_set_priority_27"),
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        SetSolidityBits(bit_4=True, cant_walk_through=True),
        VisibilityOn(),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(VERY_SLOW),
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 65517),
        LoadMemory(PRIMARY_TEMP_700C),
        Pause(16),
        EndLoop(),
        Jmp(["ACTION_714_turn_clockwise_45_degrees_12"]),
    ]
)
