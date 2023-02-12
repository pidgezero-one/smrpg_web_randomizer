# E0635_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUNROUTINE_3

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfRandom2of3(['EVENT_635_set_24', 'EVENT_635_set_28']),
	SetVarToConst(ITEM_ID, MidMushroom),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	Return(),
	SetVarToConst(ITEM_ID, MaxMushroom, identifier="EVENT_635_set_24"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	Return(),
	SetVarToConst(ITEM_ID, PickMeUp, identifier="EVENT_635_set_28"),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM),
	Return()
])
