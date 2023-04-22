# pylint: disable=C0301

"""E0304_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TEMP_70A9, 21),
        SetVarToConst(SECONDARY_TEMP_7024, 1),
        JmpToEvent(E0264_RETURN),
    ]
)
