# E1114_SUMMON_TADPOLE_SHOPS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_5, ["EVENT_1114_ret_4"]),
	SetSyncActionScript(NPC_0, A0087_SHOP_TADPOLE),
	SetSyncActionScript(NPC_1, A0088_SHOP_TADPOLE),
	Return(identifier="EVENT_1114_ret_4")
])
