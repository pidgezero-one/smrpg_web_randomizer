# E1795_LANDS_END_UNDERGROUND_LOWER_LEVEL_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RemoveObjectFromCurrentLevel(NPC_18),
	RemoveObjectFromCurrentLevel(NPC_19),
	JmpIfBitClear(LANDS_END_CHEST_1_PAID, ["EVENT_1795_jmp_if_bit_clear_6"]),
	RemoveObjectFromCurrentLevel(NPC_16),
	SummonObjectToCurrentLevel(NPC_18),
	SetSyncActionScript(NPC_18, A0014_FLOATING_CHEST),
	JmpIfBitClear(LANDS_END_CHEST_2_PAID, ["EVENT_1795_run_event_as_subroutine_10"], identifier="EVENT_1795_jmp_if_bit_clear_6"),
	RemoveObjectFromCurrentLevel(NPC_16),
	SummonObjectToCurrentLevel(NPC_19),
	SetSyncActionScript(NPC_19, A0014_FLOATING_CHEST),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1795_run_event_as_subroutine_10"),
	Return()
])
