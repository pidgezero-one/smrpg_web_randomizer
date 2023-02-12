#A0279_KEEP_BARREL_COUNTING_OPTIONAL_BARREL

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	TransferXYZFPixels(x=252, y=254, z=0, direction=EAST),
	SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	VisibilityOn(),
	Return()
])
