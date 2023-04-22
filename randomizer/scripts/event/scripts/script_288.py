# pylint: disable=C0301

"""E0288_UNKNOWN_ROSE_TOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TEMP_70A9, 21),
        SetVarToConst(SECONDARY_TEMP_7024, 3),
        JmpToEvent(E0264_RETURN),
    ]
)
