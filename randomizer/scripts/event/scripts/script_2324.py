# E2324_BOOSTER_PASS_2ND_ROOM_SPINY_SUMMONER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfObjectInCurrentLevel(NPC_1, ["EVENT_2324_ret_4"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_2324_ret_4"]),
	SetBit(TEMP_7043_1),
	SetSyncActionScript(NPC_1, A0693_BOOSTER_PASS_SPINY),
	Return(identifier="EVENT_2324_ret_4")
])
