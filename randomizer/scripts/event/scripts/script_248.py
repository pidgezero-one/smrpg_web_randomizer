# E0248_NPC_QUEST_6_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_248_room_7_logic"]),
	Return(),
	SetVarToConst(PRIMARY_TEMP_7000, 20, identifier="EVENT_248_room_7_logic"),
	JmpToEvent(E0158_NPC_QUEST_GRANT_MULTI_FROG_COIN),
	Return()
])
