# E1643_PURTEND_STORE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	JmpIfBitClear(SHUFFLE_ONE_FIREWORKS_ENABLED, ["EVENT_1643_run_dialog_2"]),
	RunDialog(dialog_id=DI1160_PURTEND_STORE_DISABLED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI1124_PURTEND_STORE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1643_run_dialog_2"),
	JmpIfDialogOptionBSelected(["EVENT_1643_pause_23"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	StoreItemAmountTo7000(ShinyStone),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1643_run_dialog_20"]),
	StoreItemAmountTo7000(Fireworks),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1643_run_dialog_27"]),
	RunDialog(dialog_id=DI1295_PURTEND_STORE_PROMPT_TO_TRADE_FIREWORKS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_1643_pause_23"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RemoveOneOfItemFromInventory(Fireworks),
	RunDialog(dialog_id=DI1154_PURTEND_STORE_THANKS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetVarToConst(ITEM_ID, ShinyStone),
	SetVarToConst(PRIMARY_TEMP_7000, 1155),
	RunEventAsSubroutine(E3827_GRANT_ITEM_STANDARD_SOUND),
	Return(),
	RunDialog(dialog_id=DI1153_PURTEND_STORE_SOLD_OUT, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_1643_run_dialog_20"),
	RunDialogForDuration(dialog_id=DI1154_PURTEND_STORE_THANKS, duration=1, sync=False),
	Return(),
	Pause(10, identifier="EVENT_1643_pause_23"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RunDialog(dialog_id=DI1154_PURTEND_STORE_THANKS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return(),
	RunDialog(dialog_id=DI1296_PURTEND_STORE_NEED_FIREWORKS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1643_run_dialog_27"),
	Return()
])
