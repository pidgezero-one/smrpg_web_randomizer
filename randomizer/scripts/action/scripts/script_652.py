#A0652_FOREST_FIRST_WIGGLER_AFTER_RUNNING_AWAY

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOff(),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	Return()
])
