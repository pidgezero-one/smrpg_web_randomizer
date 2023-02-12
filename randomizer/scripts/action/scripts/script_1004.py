#A1004_KEEP_1ST_BOSS_SUMMON_ANIMATION

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceSouthwest(),
	PlaySound(sound=SO044_GHOST_FLOAT, channel=4),
	StartLoopNTimes(1),
	VisibilityOn(),
	Pause(2),
	VisibilityOff(),
	Pause(4),
	EndLoop(),
	StartLoopNTimes(1),
	VisibilityOn(),
	Pause(2),
	VisibilityOff(),
	Pause(2),
	EndLoop(),
	StartLoopNTimes(1),
	VisibilityOn(),
	Pause(1),
	VisibilityOff(),
	Pause(1),
	EndLoop(),
	VisibilityOn(),
	SetSequenceSpeed(NORMAL),
	SetSpriteSequence(index=10, is_sequence=True, looping=False),
	Return()
])
