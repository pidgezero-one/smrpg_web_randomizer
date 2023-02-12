# E1572_MIDAS_RIVER_COIN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(TEMP_7044_2),
	DisableObjectTrigger(MEM_70A8),
	SetSyncActionScript(MEM_70A8, A0470_COLLECT_MIDAS_COIN),
	Inc(TEMP_702A),
	ClearBit(TEMP_7044_2),
	Return()
])
