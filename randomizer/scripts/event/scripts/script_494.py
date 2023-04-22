# pylint: disable=C0301

"""E0494_PIPE_VAULT_PIRANHA_TIMER_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_7, ["EVENT_256_ret_0"]),
        SetBit(TEMP_7043_7),
        ClearBit(TEMP_7044_0),
        JmpIfBitSet(TEMP_7044_4, ["EVENT_494_clear_bit_7"]),
        ClearBit(TEMP_7044_3),
        SetBit(TEMP_7044_4),
        Return(),
        ClearBit(TEMP_7044_4, identifier="EVENT_494_clear_bit_7"),
        SetBit(TEMP_7044_3),
        Return(),
    ]
)
