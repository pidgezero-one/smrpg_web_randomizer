# pylint: disable=C0301

"""E1801_FREESTANDING_FLOWER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        RemoveObjectAt70A8FromCurrentLevel(),
        SetVarToConst(PRIMARY_TEMP_7000, 1),
        Add7000ToMaxFP(),
        SetTempSyncActionScript(MEM_70A8, A1016_FREESTANDING_FLOWER_PICKED_UP),
        Return(),
    ]
)
