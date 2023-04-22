# pylint: disable=C0301

"""E3235_SHIP_PASSWORD_BOX_4"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpToSubroutine(["EVENT_3237_jmp_if_bit_set_5"]),
        Inc(TEMP_702A),
        JmpIfVarNotEqualsConst(TEMP_702A, 5, ["EVENT_3232_jmp_4"]),
        SetVarToConst(TEMP_702A, 0),
        Jmp(["EVENT_3237_clear_bit_9"]),
    ]
)
