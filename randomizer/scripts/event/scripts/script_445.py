# E0445_GOOMBA_THUMPIN_BEGINS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	EnableControls([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	RunBackgroundEvent(event_id=E0447_GOOMBA_THUMPIN_SPAWNS, return_on_level_exit=True),
	SetVarToConst(PRIMARY_TEMP_7000, 30),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
	PlayMusicAtDefaultVolume(M47_GRATE_GUYS_CASINO),
	Jmp(["EVENT_446_set_short_20"])
])
