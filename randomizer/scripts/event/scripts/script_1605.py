# E1605_TOWER_EXTERIOR_CANCEL_EXP_STAR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitClear(TEMP_7076_0, ["EVENT_1605_ret_9"]),
	JmpIfBitSet(EXP_STAR_BIT_5, ["EVENT_1605_ret_9"]),
	SetVarToConst(TIMER_7022, 1),
	ClearBit(EXP_STAR_BIT_6),
	Return(identifier="EVENT_1605_ret_9")
])
