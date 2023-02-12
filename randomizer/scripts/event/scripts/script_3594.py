# E3594_GET_ITEM_FROM_CHAPEL_HENCHMAN_1

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpToSubroutine(["EVENT_3593_pause_22"]),
	FreezeAllNPCsUntilReturn(),
	JmpIfBitSet(CHAPEL_ITEM_2_RETRIEVED, ["EVENT_3594_jmp_to_subroutine_10"]),
	SetVarToConst(PRIMARY_TEMP_7000, 1),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	UnfreezeAllNPCs(),
	SetBit(CHAPEL_ITEM_2_RETRIEVED),
	Return(),
	JmpToSubroutine(["EVENT_3593_pause_22"], identifier="EVENT_3594_jmp_to_subroutine_10"),
	FreezeAllNPCsUntilReturn(),
	SetVarToConst(PRIMARY_TEMP_7000, 1),
	RunDialog(dialog_id=DI2496_WHERES_THE_CROWN, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
