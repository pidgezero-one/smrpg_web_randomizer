# E1579_MIDAS_RIVER_BARREL_SUBROUTINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_5, ["EVENT_1579_ret_6"]),
	ClearBit(TEMP_7044_3),
	SetBit(TEMP_7043_5),
	SetVarToConst(X_COORD_2, 10),
	SetVarToConst(Y_COORD_2, 85),
	JmpToEvent(E1573_MIDAS_RIVER_BARREL_SUBROUTINE),
	Return(identifier="EVENT_1579_ret_6")
])
