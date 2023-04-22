# pylint: disable=C0301

"""E0539_ROSE_TOWN_SHOP_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TEMP_70A9, 20),
        SetVarToConst(SECONDARY_TEMP_7024, 3),
        JmpToEvent(E0264_RETURN),
    ]
)
