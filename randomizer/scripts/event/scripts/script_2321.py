# E2321_BOOSTER_PASS_2ND_ROOM_SPINY_SUMMONER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfObjectInCurrentLevel(NPC_0, ["EVENT_2321_ret_4"]),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_2321_ret_4"]),
	SetBit(TEMP_7043_0),
	SetSyncActionScript(NPC_0, A0694_BOOSTER_PASS_SPINY),
	Return(identifier="EVENT_2321_ret_4")
])
