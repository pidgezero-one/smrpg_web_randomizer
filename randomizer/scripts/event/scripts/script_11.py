# E0011_SET_70A7_TO_RANDOM_TIER_3_EQUIP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToRandom(PRIMARY_TEMP_7000, 10),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_11_set_0"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_11_set_1"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_11_set_2"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_11_set_3"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_11_set_4"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_11_set_5"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_11_set_6"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_11_set_7"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_11_set_8"]),
	SetVarToConst(ITEM_ID, RoyalDress),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SonicCymbal, identifier="EVENT_11_set_0"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SuperSlap, identifier="EVENT_11_set_1"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, UltraHammer, identifier="EVENT_11_set_2"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, MegaGlove, identifier="EVENT_11_set_3"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, StickyGlove, identifier="EVENT_11_set_4"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, WarFan, identifier="EVENT_11_set_5"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, StarGun, identifier="EVENT_11_set_6"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, HeroShirt, identifier="EVENT_11_set_7"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, PrincePants, identifier="EVENT_11_set_8"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM)
])
