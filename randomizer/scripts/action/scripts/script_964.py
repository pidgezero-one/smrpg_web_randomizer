#A0964_FACTORY_3RD_BOSS_RIGHT_HAMMER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOff(),
	SetWalkingSpeed(FASTEST),
	ShiftSouthwestPixels(6),
	Pause(1, identifier="ACTION_964_pause_3"),
	JmpIfBitClear(TEMP_7043_2, ["ACTION_964_pause_3"]),
	SetSpriteSequence(index=3, looping=False),
	Pause(32),
	SetBit(TEMP_7043_5),
	Pause(4),
	ClearBit(TEMP_7043_2),
	Jmp(["ACTION_964_pause_3"])
])
