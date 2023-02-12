#A0657_PIPE_VAULT_THWOMP

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOff(identifier="ACTION_657_shadow_off_0"),
	SetWalkingSpeed(NORMAL),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	ClearBit(TEMP_7043_4),
	ShiftZUpPixels(10),
	ShiftZUpPixels(6),
	ShiftZUpSteps(4),
	JmpIfRandom1of2(["ACTION_657_pause_9"]),
	Pause(60),
	Pause(30, identifier="ACTION_657_pause_9"),
	SetWalkingSpeed(FASTEST),
	ShiftZDownSteps(4),
	SetBit(TEMP_7043_4),
	DecZCoord1Step(),
	PlaySound(sound=SO073_THWOMP_STOMP, channel=4),
	SetBit(TEMP_7043_1),
	SetSequenceSpeed(FAST),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	Pause(2),
	ClearBit(TEMP_7043_1),
	Pause(28),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	Jmp(["ACTION_657_shadow_off_0"])
])
