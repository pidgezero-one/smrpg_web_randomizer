# E3517_CHEST_DIFFERENTIATOR_NPC_1_2_3_OR_OTHER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfVarEqualsConst(ACTIVE_NPC, 21, ["EVENT_3517_chest_2"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 22, ["EVENT_3517_chest_3"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 23, ["EVENT_3517_chest_4"]),
	JmpToEvent(E0172_CHEST_1_CONTAINER),
	JmpToEvent(E0173_CHEST_2_CONTAINER, identifier="EVENT_3517_chest_2"),
	JmpToEvent(E0174_CHEST_3_CONTAINER, identifier="EVENT_3517_chest_3"),
	JmpToEvent(E0175_CHEST_4_CONTAINER, identifier="EVENT_3517_chest_4")
])
