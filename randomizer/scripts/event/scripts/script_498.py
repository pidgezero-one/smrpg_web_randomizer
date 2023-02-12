# E0498_PIPE_VAULT_FIRST_GOOMBA

from randomizer.scripts.event.script_imports import *

script = EventScript([
	StartBattleAtBattlefield(6, BF21_KERO_SEWERS),
	JmpIfBitSet(RUN_AWAY, ["EVENT_1008_set_temp_action_script_sync_7"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_287_reset_and_choose_game_0"]),
	RemoveObjectAt70A8FromCurrentLevel(),
	RemoveObjectFromCurrentLevel(MEM_70A8),
	FadeInFromBlack(sync=False),
	Return()
])
