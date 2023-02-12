# E1921_ABYSS_MACHINE_BOWYER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FreezeAllNPCsUntilReturn(),
	SetVarToConst(BATTLE_PACK_ID, 212),
	Jmp(["EVENT_1909_start_battle_700E_5"])
])
