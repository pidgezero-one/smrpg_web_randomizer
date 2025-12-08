# pylint: disable=C0301

"""E3237_SHIP_PASSWORD_BOX_6"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpToSubroutine(["EVENT_3237_jmp_if_bit_set_5"]),
        Inc(TEMP_702E),
        JmpIfVarNotEqualsConst(TEMP_702E, 5, ["EVENT_3232_jmp_4"]),
        SetVarToConst(TEMP_702E, 0),
        Jmp(["EVENT_3237_clear_bit_9"]),
        JmpIfBitSet(
            TEMP_7043_0,
            ["EVENT_3237_end_all_11"],
            identifier="EVENT_3237_jmp_if_bit_set_5"),
        SetBit(TEMP_7044_0),
        SetTempSyncActionScript(MEM_70A8, A0337_VARIOUS_SHIP_OBJECTS),
        Return(),
        ClearBit(TEMP_7043_7, identifier="EVENT_3237_clear_bit_9"),
        Return(),
        EndAll(identifier="EVENT_3237_end_all_11"),
    ]
)
