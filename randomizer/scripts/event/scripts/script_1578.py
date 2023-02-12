# E1578_MIDAS_RIVER_BARREL_SUBROUTINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_4, ["EVENT_1578_ret_8"]),
	ClearBit(TEMP_7044_3),
	SetBit(TEMP_7043_4),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 1, ["EVENT_1578_set_short_5"]),
	RunBackgroundEvent(event_id=E1586_MIDAS_RIVER_BARREL_FISH_MOVEMENT, return_on_level_exit=True, bit_6=True),
	SetVarToConst(X_COORD_2, 24, identifier="EVENT_1578_set_short_5"),
	SetVarToConst(Y_COORD_2, 57),
	JmpToEvent(E1573_MIDAS_RIVER_BARREL_SUBROUTINE),
	Return(identifier="EVENT_1578_ret_8")
])
