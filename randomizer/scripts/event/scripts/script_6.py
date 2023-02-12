# E0006_SET_70A7_TO_RANDOM_TIER_2_CONSUMABLE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToRandom(PRIMARY_TEMP_7000, 10),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_6_set_3"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_6_set_4"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_6_set_5"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_6_set_6"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_6_set_7"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_6_set_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_6_set_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_6_set_10"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_6_set_11"]),
	SetVarToConst(ITEM_ID, MidMushroom),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, MapleSyrup, identifier="EVENT_6_set_3"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, Bracer, identifier="EVENT_6_set_4"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, Energizer, identifier="EVENT_6_set_5"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, BadMushroom, identifier="EVENT_6_set_6"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FlowerTab, identifier="EVENT_6_set_7"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, YoshiCandy, identifier="EVENT_6_set_8"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, Elixir, identifier="EVENT_6_set_9"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FreshenUp, identifier="EVENT_6_set_10"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FrightBomb, identifier="EVENT_6_set_11"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM)
])
