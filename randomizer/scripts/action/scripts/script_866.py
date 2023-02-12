#A0866_MOVE_HINOPIO_TO_ITEM_SHOP

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ClearBit(TEMP_7043_2),
	SetBit(TEMP_7043_1),
	SetAllSpeeds(VERY_FAST),
	ShiftNorthwestSteps(4),
	FaceSouthwest(),
	Return()
])
