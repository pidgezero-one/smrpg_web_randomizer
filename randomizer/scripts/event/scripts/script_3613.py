# E3613_CHEST_DIFFERENTIATOR_NPC_11_OR_OTHER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfVarEqualsConst(ACTIVE_NPC, 31, ["EVENT_3613_chest_2"]),
	JmpToEvent(E0172_CHEST_1_CONTAINER),
	JmpToEvent(E0173_CHEST_2_CONTAINER, identifier="EVENT_3613_chest_2")
])
