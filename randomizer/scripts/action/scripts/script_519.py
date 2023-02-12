#A0519_TOWER_BOSS_PEEKING_BEHIND_ENTRANCE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Pause(1, identifier="ACTION_519_placeholder"),
	FaceSouthwest(),
	FixedFCoordOn(),
	Pause(120),
	SetWalkingSpeed(NORMAL),
	ShiftSouthPixels(15),
	Pause(120),
	Pause(120),
	Pause(120),
	Pause(120),
	ShiftNorthPixels(15),
	Pause(60),
	Jmp(["ACTION_519_placeholder"]),
	VisibilityOff(),
	Return()
])
