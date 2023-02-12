# E0012_SET_70A7_TO_RANDOM_TIER_4_EQUIP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToRandom(PRIMARY_TEMP_7000, 10),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_12_set_0"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_12_set_1"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_12_set_2"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_12_set_3"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_12_set_4"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_12_set_5"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_12_set_6"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_12_set_7"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_12_set_8"]),
	SetVarToConst(ITEM_ID, Masher),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SuperSuit, identifier="EVENT_12_set_0"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, LazyShellArmor, identifier="EVENT_12_set_1"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, AttackScarf, identifier="EVENT_12_set_2"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, LazyShellWeapon, identifier="EVENT_12_set_3"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, QuartzCharm, identifier="EVENT_12_set_4"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, SafetyRing, identifier="EVENT_12_set_5"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, FryingPan, identifier="EVENT_12_set_6"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, JinxBelt, identifier="EVENT_12_set_7"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	SetVarToConst(ITEM_ID, ExpBooster, identifier="EVENT_12_set_8"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM)
])
