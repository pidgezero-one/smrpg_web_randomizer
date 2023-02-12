# E3608_LANDS_END_PURCHASABLE_CHEST

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfVarEqualsConst(ACTIVE_NPC, 39, ["EVENT_3608_chest_2"]),
	JmpToEvent(E1793_LANDS_END_PURCHASABLE_CHEST_1_SUBROUTINE),
	JmpToEvent(E3929_LANDS_END_PURCHASABLE_CHEST_2_SUBROUTINE, identifier="EVENT_3608_chest_2")
])
