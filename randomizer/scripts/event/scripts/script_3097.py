# E3097_JUICE_BAR_CARD_NPC_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	StoreItemAmountTo7000(AltoCard),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3097_set_298"]),
	StoreItemAmountTo7000(TenorCard),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3097_set_294"]),
	SetVarToConst(ITEM_ID, AltoCard),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SopranoCard, identifier="EVENT_3097_set_294"),
	RemoveOneOfItemFromInventory(TenorCard),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, TenorCard, identifier="EVENT_3097_set_298"),
	RemoveOneOfItemFromInventory(AltoCard),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM)
])
