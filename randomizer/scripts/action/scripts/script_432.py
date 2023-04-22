"""A0432_SEWER_FOUR_RATS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ObjectMemorySetBit(
            arg_1=0x0B, bits=[3], identifier="ACTION_432_object_memory_set_bit_0"
        ),
        SetWalkingSpeed(SLOW),
        SetPriority(2),
        StartLoopNTimes(3),
        WalkFDirectionSteps(3),
        TurnClockwise45DegreesNTimes(2),
        Pause(6),
        TurnClockwise45DegreesNTimes(2),
        Pause(6),
        TurnClockwise45DegreesNTimes(2),
        Pause(6),
        TurnClockwise45DegreesNTimes(2),
        Pause(6),
        TurnClockwise45DegreesNTimes(2),
        EndLoop(),
        TurnClockwise45DegreesNTimes(2),
        StartLoopNTimes(3),
        WalkFDirectionSteps(3),
        TurnClockwise45DegreesNTimes(6),
        Pause(6),
        TurnClockwise45DegreesNTimes(6),
        Pause(6),
        TurnClockwise45DegreesNTimes(6),
        Pause(6),
        TurnClockwise45DegreesNTimes(6),
        Pause(6),
        TurnClockwise45DegreesNTimes(6),
        EndLoop(),
        TurnClockwise45DegreesNTimes(6),
        Jmp(["ACTION_432_object_memory_set_bit_0"]),
    ]
)
