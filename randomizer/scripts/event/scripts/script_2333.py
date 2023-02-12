# E2333_BOOSTER_PASS_2ND_ROOM_SPINY_SUMMONER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfObjectInCurrentLevel(NPC_3, ["EVENT_2333_ret_4"]),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_2333_ret_4"]),
	SetBit(TEMP_7043_3),
	SetSyncActionScript(NPC_3, A0694_BOOSTER_PASS_SPINY),
	Return(identifier="EVENT_2333_ret_4")
])
