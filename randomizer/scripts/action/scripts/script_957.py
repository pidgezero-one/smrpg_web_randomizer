#A0957_FACTORY_CONVEYOR_PAINT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3),
	ShiftWestPixels(8),
	VisibilityOff(identifier="ACTION_957_visibility_off_2"),
	Pause(1),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_957_visibility_off_2"]),
	ClearBit(TEMP_7043_0),
	VisibilityOn(),
	SetSpriteSequence(index=0, looping=False),
	PlaySound(sound=SO146_MACHINE_TRANSFORM, channel=4),
	Pause(36),
	Jmp(["ACTION_957_visibility_off_2"])
])
