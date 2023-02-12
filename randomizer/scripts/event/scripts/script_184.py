# E0184_NPC_QUEST_GRANT_SINGLE_FIREWORKS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(FIREWORKS_COUNTER, 5),
	SetVarToConst(ITEM_ID, Fireworks),
	JmpToEvent(E0160_NPC_QUEST_GRANT_ITEM)
])
