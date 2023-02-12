#A0867_MOVE_HINOPIO_TO_ARMOR_SHOP

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ClearBit(TEMP_7043_2),
	SetBit(TEMP_7043_3),
	SetAllSpeeds(VERY_FAST),
	ShiftSoutheastSteps(4),
	FaceSouthwest(),
	Return()
])
