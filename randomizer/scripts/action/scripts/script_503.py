#A0503_MUSHROOM_DERBY_PLAYER_WHEN_COOKIE_USED

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	BPL262728(),
	SetWalkingSpeed(FAST),
	SetSequenceSpeed(VERY_FAST),
	ShiftNortheastSteps(3),
	SetBit(TEMP_7043_2),
	ClearBit(TEMP_7043_4),
	Jmp(["ACTION_500_db_0"])
])
