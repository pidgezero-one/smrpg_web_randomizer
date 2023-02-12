# E1431_SUMMON_MIDDLE_GOOMBA_IN_MUSHROOM_WAY_2

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfObjectNotInSpecificLevel(NPC_6, R204_MUSHROOM_WAY_AREA_02, ["EVENT_1431_ret_4"]),
	JmpIfBitSet(TEMP_7044_3, ["EVENT_1431_ret_4"]),
	SetSyncActionScript(NPC_6, A0541_MIDDLE_GOOMBA_IN_MUSHROOM_WAY_2),
	Return(),
	Return(identifier="EVENT_1431_ret_4")
])
