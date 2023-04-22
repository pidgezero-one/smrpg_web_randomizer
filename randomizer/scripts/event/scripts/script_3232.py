# pylint: disable=C0301

"""E3232_SHIP_PASSWORD_BOX_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpToSubroutine(["EVENT_3237_jmp_if_bit_set_5"]),
        Inc(SECONDARY_TEMP_7024),
        JmpIfVarNotEqualsConst(SECONDARY_TEMP_7024, 5, ["EVENT_3232_jmp_4"]),
        SetVarToConst(SECONDARY_TEMP_7024, 0),
        Jmp(["EVENT_3237_clear_bit_9"], identifier="EVENT_3232_jmp_4"),
    ]
)
