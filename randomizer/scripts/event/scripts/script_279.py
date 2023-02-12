# E0279_UNKNOWN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
	AddCoins(PRIMARY_TEMP_7000),
	PlaySound(sound=SO013_COIN, channel=6),
	SetSyncActionScript(MEM_70A8, A0470_COLLECT_MIDAS_COIN),
	Return()
])
