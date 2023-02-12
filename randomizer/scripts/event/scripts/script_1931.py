# E1931_TREASURE_CHEST_FAILURE_MIMIC_FIGHT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	StartBattleAtBattlefield(158, BF21_KERO_SEWERS),
	JmpIfBitSet(GAME_OVER, ["EVENT_1931_reset_and_choose_game_366"]),
	Return(),
	ResetAndChooseGame(identifier="EVENT_1931_reset_and_choose_game_366"),
	Return()
])
