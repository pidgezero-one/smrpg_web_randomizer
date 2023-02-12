# E3519_CHEST_DIFFERENTIATOR_NPC_4_OR_OTHER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfVarEqualsConst(ACTIVE_NPC, 24, ["EVENT_3519_chest_2"]),
	JmpToEvent(E1936_KEEP_ROTATING_ROOM_CHEST_1),
	JmpToEvent(E1937_KEEP_ROTATING_ROOM_CHEST_2, identifier="EVENT_3519_chest_2")
])
