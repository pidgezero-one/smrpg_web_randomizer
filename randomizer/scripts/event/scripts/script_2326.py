# E2326_BOOSTER_PASS_2ND_ROOM_SPINY_SUMMONER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfObjectInCurrentLevel(NPC_2, ["EVENT_2326_ret_4"]),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_2326_ret_4"]),
	SetBit(TEMP_7043_2),
	SetSyncActionScript(NPC_2, A0691_BOOSTER_PASS_SPINY),
	Return(identifier="EVENT_2326_ret_4")
])
