# E0440_PIPE_VAULT_FIREBALL_BACKGROUND

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(GAME_OVER, ["EVENT_440_reset_and_choose_game_5"]),
	JmpIfBitSet(RUN_AWAY, ["EVENT_440_ret_7"]),
	RemoveObjectAt70A8FromCurrentLevel(),
	RemoveObjectFromCurrentLevel(MEM_70A8),
	Return(),
	ResetAndChooseGame(identifier="EVENT_440_reset_and_choose_game_5"),
	EndAll(),
	Return(identifier="EVENT_440_ret_7")
])
