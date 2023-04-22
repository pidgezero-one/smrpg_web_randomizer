# pylint: disable=C0301

"""E1911_ABYSS_MACHINE_MACK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FreezeAllNPCsUntilReturn(),
        SetVarToConst(BATTLE_PACK_ID, 211),
        Jmp(["EVENT_1909_start_battle_700E_5"]),
    ]
)
