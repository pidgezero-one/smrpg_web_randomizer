# pylint: disable=C0301

"""E3488_MIDAS_RIVER_COIN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        SetSyncActionScript(MEM_70A8, A0470_COLLECT_MIDAS_COIN),
        Inc(TEMP_702A),
        Return(),
    ]
)
