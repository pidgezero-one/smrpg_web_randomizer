# E3098_PROGRESSIVE_EGG_NPC_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	StoreItemAmountTo7000(MysteryEgg),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3098_set_298"]),
	StoreItemAmountTo7000(LambsLure),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3098_set_294"]),
	StoreItemAmountTo7000(SheepAttack),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3098_subroutine"]),
	SetVarToConst(ITEM_ID, MysteryEgg),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SheepAttack, identifier="EVENT_3098_subroutine"),
	RemoveOneOfItemFromInventory(SheepAttack),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SheepAttack, identifier="EVENT_3098_set_294"),
	RemoveOneOfItemFromInventory(LambsLure),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, LambsLure, identifier="EVENT_3098_set_298"),
	RemoveOneOfItemFromInventory(MysteryEgg),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM)
])
