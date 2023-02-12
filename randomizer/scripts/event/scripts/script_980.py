# E0980_FROGFUCIUS_HINT_MARRYMORE_SUITE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CopyVarToVar(from_var=UNKNOWN_70D7, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 200),
	JmpIfComparisonResultIsLesser(["EVENT_991_marrymore_inn"]),
	Return()
])
