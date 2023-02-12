# E3295_SHIP_COLLECT_BARREL_PRIZE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(UNKNOWN_707D_5, ["EVENT_3295_ret_6"]),
	SetBit(UNKNOWN_707D_5),
	JmpToEvent(E3077_SHIP_PUZZLE_MUSHROOM),
	Return(identifier="EVENT_3295_ret_6")
])
