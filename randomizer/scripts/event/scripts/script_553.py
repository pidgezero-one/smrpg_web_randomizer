# pylint: disable=C0301

"""E0553_ROSE_TOWN_OCCUPIED_ARROW_CONTROL_4"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_256_ret_0"]),
        SetBit(TEMP_7044_6),
        SetBit(TEMP_7044_1),
        Return(),
    ]
)
