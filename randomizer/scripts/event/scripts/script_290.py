# E0290_MUSHROOM_KINGDOM_SHOP_LOGIC

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(MUSHROOM_KINGDOM_SHOPKEEPER_FREE_ITEM_GRANTED, ["EVENT_290_jmp_if_bit_set_355_"]),
	SetBit(MUSHROOM_KINGDOM_SHOPKEEPER_FREE_ITEM_GRANTED),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	Return(),
	JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_290_open_shop_364"], identifier="EVENT_290_jmp_if_bit_set_355_"),
	StoreItemAmountTo7000(RareFrogCoin),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_290_run_event_as_subroutine_359_"]),
	JmpToEvent(E0284_OPEN_MUSHROOM_KINGDOM_SHOP, identifier="EVENT_290_open_shop_364"),
	RemoveOneOfItemFromInventory(RareFrogCoin, identifier="EVENT_290_run_event_as_subroutine_359_"),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	Return()
])
