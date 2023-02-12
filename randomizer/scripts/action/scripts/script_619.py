#A0619_MINES_CENTER_CROOK

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpIfBitSet(MINES_HENCHMAN_MIDDLE_DEFEATED, ["ACTION_617_visibility_off_10"]),
	JmpIfBitSet(MINES_BOSS_1_DEFEATED, ["ACTION_617_visibility_off_10"]),
	Return()
])
