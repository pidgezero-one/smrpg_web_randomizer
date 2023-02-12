# E1704_BANDITS_WAY_2_SPINNY_FLOWER_2

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(SPINNING_FLOWER_2),
	SetVarToConst(X_COORD_2, 5721),
	JmpToEvent(E1537_SPINNING_FLOWER_CORE_LOGIC)
])
