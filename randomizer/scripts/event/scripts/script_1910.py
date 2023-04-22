# pylint: disable=C0301

"""E1910_ABYSS_CONVEYOR_BELT_SHYPER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FreezeAllNPCsUntilReturn(),
        JmpIfRandom1of2(["EVENT_1910_set_short_4"]),
        SetVarToConst(BATTLE_PACK_ID, 122),
        Jmp(["EVENT_1909_start_battle_700E_5"]),
        SetVarToConst(BATTLE_PACK_ID, 123, identifier="EVENT_1910_set_short_4"),
        Jmp(["EVENT_1909_start_battle_700E_5"]),
    ]
)
