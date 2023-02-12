#A0637_ROSE_TOWN_INITIAL_ARROW

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	TransferToXYZF(x=8, y=50, z=0, direction=SOUTHEAST),
	Jmp(["ACTION_638_set_bit_4"])
])
