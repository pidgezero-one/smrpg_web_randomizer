#A0674_ROSE_TOWN_LIBERATED_WATER_KID

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Pause(64),
	JmpToSubroutine(["ACTION_672_visibility_off_10"]),
	FaceNorthwest(),
	SequenceLoopingOff(),
	Pause(32),
	StartLoopNTimes(2),
	SetWalkingSpeed(VERY_FAST),
	ShiftZUpPixels(8),
	SetWalkingSpeed(VERY_SLOW),
	ShiftZDownPixels(8),
	EndLoop(),
	SetWalkingSpeed(SLOW),
	Pause(30),
	JmpToSubroutine(["ACTION_672_shift_northeast_steps_26"]),
	Pause(30),
	SetBit(TEMP_7044_0),
	Return()
])
