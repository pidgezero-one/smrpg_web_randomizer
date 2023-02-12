# E0007_SET_70A7_TO_RANDOM_TIER_3_CONSUMABLE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToRandom(PRIMARY_TEMP_7000, 10),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_7_set_3"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_7_set_4"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_7_set_5"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_7_set_6"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_7_set_7"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_7_set_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_7_set_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_7_set_10"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_7_set_11"]),
	SetVarToConst(ITEM_ID, MaxMushroom),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, RoyalSyrup, identifier="EVENT_7_set_3"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, YoshiAde, identifier="EVENT_7_set_4"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FireBomb, identifier="EVENT_7_set_5"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, IceBomb, identifier="EVENT_7_set_6"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FlowerJar, identifier="EVENT_7_set_7"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, MukuCookie, identifier="EVENT_7_set_8"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, Megalixir, identifier="EVENT_7_set_9"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, Crystalline, identifier="EVENT_7_set_10"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, PowerBlast, identifier="EVENT_7_set_11"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM)
])
