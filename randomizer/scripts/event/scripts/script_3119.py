# E3119_GOBY_BATTLE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(TEMP_707C_1),
	SetVarToConst(BATTLE_PACK_ID, 16),
	RunEventAsSubroutine(E0016_FIGHT_REMOVE_PERMANENTLY),
	Pause(1),
	ClearBit(TEMP_707C_1),
	Return()
])
