# E2812_MUSHROOM_WAY_3_UPPER_QUICK_SPINY

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_1, ["EVENT_2812_ret_2"]),
	SetSyncActionScript(NPC_3, A0495_FAST_SPINY),
	Return(identifier="EVENT_2812_ret_2")
])
