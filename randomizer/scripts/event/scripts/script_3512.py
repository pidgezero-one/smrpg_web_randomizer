# pylint: disable=C0301

"""E3512_BOOSTER_HILL_FLOWER_PICKUP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControlsUntilReturn([]),
        DisableObjectTrigger(NPC_8),
        SetAsyncActionScript(NPC_8, A0365_BOOSTER_HILL_LEFTOVER_FLOWERS_PICKED_UP),
        SetVarToConst(PRIMARY_TEMP_7000, 1),
        Add7000ToMaxFP(),
        Inc(BOOSTER_HILL_70B1),
        EnableControlsUntilReturn([B]),
        SetBit(UNKNOWN_704E_2),
        Return(),
    ]
)
