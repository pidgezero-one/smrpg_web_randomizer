#A0377_MOVE_6_DIAGONAL

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	TransferXYZFPixels(x=6, y=250, z=0, direction=EAST),
	SetSequenceSpeed(SLOW),
	SequenceLoopingOn(),
	Return()
])
