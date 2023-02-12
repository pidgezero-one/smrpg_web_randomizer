#A0402_FOREST_TRUNK_AREA_UNDERGROUND_AMANITA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(SLOW),
	SequenceLoopingOn(),
	JmpIfRandom1of2(["ACTION_402_set_var_to_random_5"], identifier="ACTION_402_jmp_if_random_above_128_2"),
	TurnRandomDirection(),
	Pause(8),
	SetVarToRandom(PRIMARY_TEMP_700C, 2, identifier="ACTION_402_set_var_to_random_5"),
	Inc(PRIMARY_TEMP_700C),
	ShiftZ20Steps(),
	Jmp(["ACTION_402_jmp_if_random_above_128_2"])
])
