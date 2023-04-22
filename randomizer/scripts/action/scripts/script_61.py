"""A0061_SEWER_RATS_IN_A_LINE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ObjectMemorySetBit(
            arg_1=0x0B, bits=[3], identifier="ACTION_61_object_memory_set_bit_0"
        ),
        SetPriority(2),
        Set700CToPressedButton(),
        Mem700CAndConst(0x0003),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_61_pause_8"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_61_pause_9"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_61_pause_10"]),
        Pause(3),
        Pause(3, identifier="ACTION_61_pause_8"),
        Pause(3, identifier="ACTION_61_pause_9"),
        Pause(3, identifier="ACTION_61_pause_10"),
        WalkFDirectionSteps(2),
        Pause(5),
        TurnClockwise45DegreesNTimes(4),
        JmpIfRandom1of2(["ACTION_61_object_memory_set_bit_0"]),
        Pause(8),
        TurnClockwise45DegreesNTimes(4),
        Jmp(["ACTION_61_object_memory_set_bit_0"]),
    ]
)
