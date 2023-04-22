# pylint: disable=C0301

"""E0335_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TEMP_70A9, 22),
        SetVarToConst(SECONDARY_TEMP_7024, 5),
        JmpToEvent(E0264_RETURN),
    ]
)
