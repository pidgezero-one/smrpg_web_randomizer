# pylint: disable=C0301

"""E2674_TOWER_KNIFE_GUY_MINIGAME_BUSINESS_LOGIC_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7043_2, ["EVENT_2674_ret_6"]),
        JmpIfBitSet(TEMP_7043_4, ["EVENT_2674_ret_6"]),
        SetBit(TEMP_7043_4),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_2674_jmp_5"]),
        Jmp(["EVENT_2672_close_2"]),
        Jmp(["EVENT_2672_close_1"], identifier="EVENT_2674_jmp_5"),
        Return(identifier="EVENT_2674_ret_6"),
    ]
)
