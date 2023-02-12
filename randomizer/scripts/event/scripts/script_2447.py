# E2447_FOREST_SUMMON_FAST_AMANITA

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7044_0, ["EVENT_2447_ret_3"]),
	SetBit(TEMP_7044_0),
	SetSyncActionScript(NPC_6, A0181_FAST_AMANITA),
	Return(identifier="EVENT_2447_ret_3")
])
