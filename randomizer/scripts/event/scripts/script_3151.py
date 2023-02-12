# E3151_ROSE_WAY_TOSSED_SHYGUYS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(BATTLE_PACK_ID, 20),
	RunEventAsSubroutine(E0017_FIGHT_REMOVE_TEMPORARILY),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3151_ret_6"]),
	Inc(TEMP_70AE),
	JmpIfVarNotEqualsConst(TEMP_70AE, 25, ["EVENT_3151_ret_6"]),
	SetSyncActionScript(NPC_0, A0439_ROSE_WAY_LAKITU),
	Return(identifier="EVENT_3151_ret_6")
])
