# E0281_CLEAR_EXP_STAR_BITS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	ClearBit(EXP_STAR_BIT_1),
	ClearBit(EXP_STAR_BIT_2),
	ClearBit(EXP_STAR_BIT_3),
	ClearBit(EXP_STAR_BIT_4),
	SetVarToConst(COIN_COUNTER_1, 0),
	SetVarToConst(COIN_COUNTER_2, 0),
	SetVarToConst(COIN_COUNTER_3, 0),
	SetVarToConst(COIN_COUNTER_4, 0),
	SetVarToConst(COIN_COUNTER_5, 0),
	SetVarToConst(COIN_COUNTER_6, 0),
	Return()
])
