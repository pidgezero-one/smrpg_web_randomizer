#A0869_MOVE_HINOPIO_TO_INN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ClearBit(TEMP_7043_3),
	SetBit(TEMP_7043_2),
	SetAllSpeeds(VERY_FAST),
	ShiftNorthwestSteps(4),
	FaceSouthwest(),
	Return()
])
