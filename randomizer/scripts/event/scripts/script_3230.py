# E3230_CANCEL_STAR_IN_SEA

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7044_6, ["EVENT_3230_ret_5"]),
	JmpIfBitClear(TEMP_7076_0, ["EVENT_3230_ret_5"]),
	JmpIfBitSet(EXP_STAR_BIT_5, ["EVENT_3230_ret_5"]),
	SetVarToConst(TIMER_7022, 1),
	SetBit(TEMP_7044_6),
	Return(identifier="EVENT_3230_ret_5")
])
