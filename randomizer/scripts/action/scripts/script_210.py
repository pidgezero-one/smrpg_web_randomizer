#A0210_GOOMBA_THUMPIN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JumpToHeight(height=96, silent=True),
	SetWalkingSpeed(FAST),
	Pause(4),
	SetWalkingSpeed(NORMAL),
	Pause(1, identifier="ACTION_210_pause_4"),
	JmpIfMarioInAir(["ACTION_210_pause_4"]),
	SetWalkingSpeed(NORMAL),
	Return()
])
