# E3587_SET_70AE_TO_70A8

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	Return()
])
