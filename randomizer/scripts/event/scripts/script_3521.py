# E3521_CHEST_DIFFERENTIATOR_NPC_12_13_OR_OTHER_CAMERA_B

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfVarEqualsConst(ACTIVE_NPC, 32, ["EVENT_3521_chest_2"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 33, ["EVENT_3521_chest_3"]),
	JmpToEvent(E1937_KEEP_ROTATING_ROOM_CHEST_2),
	JmpToEvent(E1938_KEEP_ROTATING_ROOM_CHEST_3, identifier="EVENT_3521_chest_2"),
	JmpToEvent(E1939_KEEP_ROTATING_ROOM_CHEST_4, identifier="EVENT_3521_chest_3")
])
