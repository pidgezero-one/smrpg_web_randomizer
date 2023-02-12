#A1005_KEEP_BATTLE_ROOM_SUMMON_ENEMY

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpIfBitSet(KEEP_BOSS_1_DEFEATED, ["ACTION_1005_ret_30"]),
	Pause(25),
	ResetProperties(),
	Pause(10),
	PlaySound(sound=SO044_GHOST_FLOAT, channel=4),
	StartLoopNTimes(2),
	VisibilityOn(),
	Pause(1),
	VisibilityOff(),
	Pause(1),
	EndLoop(),
	StartLoopNTimes(2),
	VisibilityOn(),
	Pause(2),
	VisibilityOff(),
	Pause(2),
	EndLoop(),
	StartLoopNTimes(1),
	VisibilityOn(),
	Pause(2),
	VisibilityOff(),
	Pause(4),
	EndLoop(),
	StartLoopNTimes(1),
	VisibilityOn(),
	Pause(1),
	VisibilityOff(),
	Pause(6),
	EndLoop(),
	VisibilityOff(),
	Return(identifier="ACTION_1005_ret_30")
])
