# E3516_CHEST_DIFFERENTIATOR_NPC_3_OR_OTHER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfVarEqualsConst(ACTIVE_NPC, 23, ["EVENT_3516_chest_2"]),
	JmpToEvent(E0174_CHEST_3_CONTAINER),
	JmpToEvent(E0175_CHEST_4_CONTAINER, identifier="EVENT_3516_chest_2")
])
