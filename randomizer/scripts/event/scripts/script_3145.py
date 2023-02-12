# E3145_SEWERS_FLIPPABLE_CHEST

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(LANDS_END_GROTTO_BARREL_FLIPPED, ["EVENT_3145_set_4"]),
	JmpToEvent(E0173_CHEST_2_CONTAINER),
	SetBit(SEWERS_FLIPPED_CHEST_OPENED, identifier="EVENT_3145_set_4"),
	JmpToEvent(E0174_CHEST_3_CONTAINER),
	Return()
])
