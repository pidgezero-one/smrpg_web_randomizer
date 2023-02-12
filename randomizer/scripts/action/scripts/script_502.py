#A0502_MUSHROOM_DERBY_UNKNOWN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	BPL262728(),
	SetWalkingSpeed(NORMAL),
	StartLoopNTimes(2),
	JumpToHeight(height=64, silent=True),
	ShiftNortheastPixels(2),
	Pause(1, identifier="ACTION_502_pause_5"),
	JmpIfMarioInAir(["ACTION_502_pause_5"]),
	Pause(4),
	EndLoop(),
	SetBit(TEMP_7043_2),
	Jmp(["ACTION_500_db_0"])
])
