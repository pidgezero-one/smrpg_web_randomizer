# E3929_LANDS_END_PURCHASABLE_CHEST_2_SUBROUTINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(LANDS_END_CHEST_2_USED),
	ClearBit(LANDS_END_CHEST_2_PAID),
	JmpToEvent(E0173_CHEST_2_CONTAINER)
])
