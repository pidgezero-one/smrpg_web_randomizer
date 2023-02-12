# E1626_MOLEVILLE_CARBO_COOKIE_TRADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	JmpIfBitSet(BUCKET_PRIZE_GRANT_NO_WARP, ["EVENT_1626_return_shiny_stone"]),
	JmpIfBitSet(SHUFFLE_ONE_FIREWORKS_ENABLED, ["EVENT_1626_run_dialog_9"]),
	JmpIfBitClear(PROGRESSIVE_FIREWORKS_ENABLED, ["EVENT_1626_store_item_amount_7000_7"]),
	JmpIfBitSet(FIRST_CARBO_COOKIE_GIVEN, ["EVENT_1626_return_shiny_stone"]),
	StoreItemAmountTo7000(ShinyStone, identifier="EVENT_1626_store_item_amount_7000_7"),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1626_run_dialog_11"]),
	RunDialog(dialog_id=DI1156_BEAN_VALLEY_PLATFORM_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1626_run_dialog_9"),
	Return(),
	RunDialog(dialog_id=DI1159_ASK_TO_TRADE_COOKIE_FOR_STONE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1626_run_dialog_11"),
	JmpIfDialogOptionBSelected(["EVENT_1626_pause_21"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RemoveOneOfItemFromInventory(ShinyStone),
	SetVarToConst(ITEM_ID, CarboCookie),
	RunEventAsSubroutine(E0160_NPC_QUEST_GRANT_ITEM),
	Return(),
	Pause(10, identifier="EVENT_1626_pause_21"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Return(),
	StoreItemAmountTo7000(ShinyStone, identifier="EVENT_1626_return_shiny_stone"),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1626_run_dialog_9"]),
	RunDialog(dialog_id=DI1158_OFFER_TO_RETURN_SHINY_STONE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_1626_pause_21"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	SetVarToConst(ITEM_ID, ShinyStone),
	RunEventAsSubroutine(E0160_NPC_QUEST_GRANT_ITEM),
	Return()
])
