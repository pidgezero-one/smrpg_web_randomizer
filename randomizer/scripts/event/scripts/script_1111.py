# E1111_FROGFUCIUS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	StoreItemAmountTo7000(CricketPie),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1111_remove_one_from_inventory_10"]),
	StoreItemAmountTo7000(CricketJam),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1111_check_if_pie_exchanged"]),
	JmpToEvent(E0947_FROGFUCIUS_HINT_MAIN_CHECKS, identifier="EVENT_1111_run_dialog_6"),
	Return(),
	RemoveOneOfItemFromInventory(CricketPie, identifier="EVENT_1111_remove_one_from_inventory_10"),
	SetBit(CRICKET_PIE_EXCHANGED),
	RunEventAsSubroutine(E0203_UNLOCK_FOREST_IF_GATED_BY_CRICKET_PIE),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	StoreItemAmountTo7000(CricketJam),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1111_ret_6__"]),
	JmpIfBitClear(CRICKET_PIE_EXCHANGED, ["EVENT_1111_dia"], identifier="EVENT_1111_check_if_pie_exchanged"),
	RemoveOneOfItemFromInventory(CricketJam),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	Return(identifier="EVENT_1111_ret_6__"),
	RunDialog(dialog_id=DI2759_FROGFUCIUS_CRICKET_JAM_WITHOUT_PIE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1111_dia"),
	Jmp(["EVENT_1111_run_dialog_6"])
])
