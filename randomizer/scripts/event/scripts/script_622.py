# E0622_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUBROUTINE_1

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfRandom1of2(["EVENT_622_grant_item_2_ret"]),
	JmpIfRandom2of3(['EVENT_622_grant_item_1_set', 'EVENT_622_grant_item_2_set']),
	SetVarToConst(PRIMARY_TEMP_7000, 30),
	JmpToEvent(E0159_NPC_QUEST_GRANT_COINS),
	Return(),
	SetVarToConst(ITEM_ID, Mushroom, identifier="EVENT_622_grant_item_1_set"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	Return(),
	SetVarToConst(ITEM_ID, MidMushroom, identifier="EVENT_622_grant_item_2_set"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	Return(identifier="EVENT_622_grant_item_2_ret")
])
