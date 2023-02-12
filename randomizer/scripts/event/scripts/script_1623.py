# E1623_BELOME_FORTUNE_BRICK

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(UNKNOWN_BELOME_TEMPLE, ["EVENT_1692_clear_bit_0"]),
	Return()
])
