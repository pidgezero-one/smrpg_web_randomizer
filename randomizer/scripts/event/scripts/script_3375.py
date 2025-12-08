# pylint: disable=C0301

"""E3375_KEEP_SET_DOOR_ORDER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, OW04_BOWSERS_KEEP),
        SetVarToConst(KEEP_DOORS_EXIT_TYPE_1, 0),
        SetVarToConst(KEEP_DOORS_EXIT_TYPE_2, 0),
        SetVarToConst(UNKNOWN_70E7, 0),
        SetVarToConst(UNKNOWN_70E8, 0),
        SetVarToConst(UNKNOWN_70E9, 0),
        ClearBit(TEMP_7043_0),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        ClearBit(TEMP_7043_3),
        ClearBit(TEMP_7043_4),
        ClearBit(TEMP_7043_5),
        SetVarToConst(ROSE_WAY_703C, 1),
        SetVarToRandom(
            PRIMARY_TEMP_7000, 6, identifier="EVENT_3375_set_var_to_random_13"
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 24),
        JmpIfMem704XAt7000BitSet(["EVENT_3375_set_var_to_random_13"]),
        SetMem704XAt7000Bit(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 25, ["EVENT_3375_set_7000_to_70A0_short_mem_28"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 26, ["EVENT_3375_set_7000_to_70A0_short_mem_33"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 27, ["EVENT_3375_set_7000_to_70A0_short_mem_39"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 28, ["EVENT_3375_set_7000_to_70A0_short_mem_44"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 29, ["EVENT_3375_set_7000_to_70A0_short_mem_50"]
        ),
        CopyVarToVar(from_var=UNKNOWN_70E7, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=ROSE_WAY_703C, to_var=ROSE_WAY_703E),
        VarShiftLeft(ROSE_WAY_703E, 252),
        Mem7000OrVar(ROSE_WAY_703E),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E7),
        Jmp(["EVENT_3375_inc_short_54"]),
        CopyVarToVar(
            from_var=UNKNOWN_70E7,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3375_set_7000_to_70A0_short_mem_28"),
        CopyVarToVar(from_var=ROSE_WAY_703C, to_var=ROSE_WAY_703E),
        Mem7000OrVar(ROSE_WAY_703E),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E7),
        Jmp(["EVENT_3375_inc_short_54"]),
        CopyVarToVar(
            from_var=UNKNOWN_70E8,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3375_set_7000_to_70A0_short_mem_33"),
        CopyVarToVar(from_var=ROSE_WAY_703C, to_var=ROSE_WAY_703E),
        VarShiftLeft(ROSE_WAY_703E, 252),
        Mem7000OrVar(ROSE_WAY_703E),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E8),
        Jmp(["EVENT_3375_inc_short_54"]),
        CopyVarToVar(
            from_var=UNKNOWN_70E8,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3375_set_7000_to_70A0_short_mem_39"),
        CopyVarToVar(from_var=ROSE_WAY_703C, to_var=ROSE_WAY_703E),
        Mem7000OrVar(ROSE_WAY_703E),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E8),
        Jmp(["EVENT_3375_inc_short_54"]),
        CopyVarToVar(
            from_var=UNKNOWN_70E9,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3375_set_7000_to_70A0_short_mem_44"),
        CopyVarToVar(from_var=ROSE_WAY_703C, to_var=ROSE_WAY_703E),
        VarShiftLeft(ROSE_WAY_703E, 252),
        Mem7000OrVar(ROSE_WAY_703E),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E9),
        Jmp(["EVENT_3375_inc_short_54"]),
        CopyVarToVar(
            from_var=UNKNOWN_70E9,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3375_set_7000_to_70A0_short_mem_50"),
        CopyVarToVar(from_var=ROSE_WAY_703C, to_var=ROSE_WAY_703E),
        Mem7000OrVar(ROSE_WAY_703E),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_70E9),
        Inc(ROSE_WAY_703C, identifier="EVENT_3375_inc_short_54"),
        CompareVarToConst(ROSE_WAY_703C, 7),
        JmpIfLoadedMemoryIsAboveOrEqual0(["EVENT_3375_set_var_to_random_13"]),
        Return(),
    ]
)
