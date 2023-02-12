#A0962_FACTORY_3RD_BOSS_LEFT_HAMMER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOff(),
	SetWalkingSpeed(FASTEST),
	ShiftSouthwestPixels(6),
	Pause(1, identifier="ACTION_962_pause_3"),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_962_pause_3"]),
	SetSpriteSequence(index=3, looping=False),
	Pause(32),
	SetBit(TEMP_7043_3),
	Pause(4),
	ClearBit(TEMP_7043_0),
	Jmp(["ACTION_962_pause_3"])
])
