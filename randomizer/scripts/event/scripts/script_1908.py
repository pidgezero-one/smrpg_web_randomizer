# E1908_ABYSS_MACHINE_AXEM_RED

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(BATTLE_PACK_ID, 214),
	StartBattleWithPackAt700E(),
	JmpIfBitSet(RUN_AWAY, ["EVENT_1904_fade_in_from_black_sync_15"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_1695_reset_and_choose_game_12"]),
	RemoveObjectFromCurrentLevel(MEM_70A8),
	DisableObjectTrigger(MEM_70A8),
	FadeInFromBlack(sync=False),
	SetSyncActionScript(MEM_70A8, A0826_ENEMY_FALL_ONTO_CONVEYOR),
	Return()
])
