# E3397_MIDAS_CAVE_PROGRESSIVE_EGG_GRANTER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	StoreItemAmountTo7000(MysteryEgg),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3397_set_298"]),
	StoreItemAmountTo7000(LambsLure),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3397_set_294"]),
	StoreItemAmountTo7000(SheepAttack),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3397_subroutine"]),
	SetVarToConst(ITEM_ID, MysteryEgg),
	JmpToEvent(E2820_ASYNC_NO_ANIMATION_ITEM),
	SetVarToConst(ITEM_ID, SheepAttack, identifier="EVENT_3397_subroutine"),
	RemoveOneOfItemFromInventory(SheepAttack),
	JmpToEvent(E2820_ASYNC_NO_ANIMATION_ITEM),
	SetVarToConst(ITEM_ID, SheepAttack, identifier="EVENT_3397_set_294"),
	RemoveOneOfItemFromInventory(LambsLure),
	JmpToEvent(E2820_ASYNC_NO_ANIMATION_ITEM),
	SetVarToConst(ITEM_ID, LambsLure, identifier="EVENT_3397_set_298"),
	RemoveOneOfItemFromInventory(MysteryEgg),
	JmpToEvent(E2820_ASYNC_NO_ANIMATION_ITEM)
])
