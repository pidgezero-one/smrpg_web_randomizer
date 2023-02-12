# E3723_NIMBUS_CASTLE_OUTER_CELLAR_GIFT_GUARD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(RED_CELLAR_GUARD_ITEM_GRANTED, ["EVENT_3723_run_dialog_85"]),
	SetVarToConst(TEMP_70AE, 16),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	SetBit(RED_CELLAR_GUARD_ITEM_GRANTED),
	ClearBit(TEMP_704C_0),
	ClearBit(GUEST_DROPPED_OFF),
	Return(),
	RunDialog(dialog_id=DI3648_NEED_CASTLE_KEY_1, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_3723_run_dialog_85"),
	Return()
])
