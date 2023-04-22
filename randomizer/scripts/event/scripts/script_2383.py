# pylint: disable=C0301

"""E2383_ABYSS_BOLT_FAR_SIDE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(DIRECTIONAL_7045_0),
        ClearBit(DIRECTIONAL_7045_1),
        ClearBit(DIRECTIONAL_7045_2),
        SetBit(DIRECTIONAL_7045_3),
        ClearBit(DIRECTIONAL_7045_4),
        ClearBit(TEMP_7043_0),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        ClearBit(TEMP_7043_3),
        ClearBit(TEMP_7043_4),
        Return(),
    ]
)
