#A0135_HENCHMAN_IMPRESSING_JUMP_LADY

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ClearSolidityBits(cant_pass_walls=True),
	FloatingOff(),
	PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=6),
	SetWalkingSpeed(FASTEST),
	ShiftZUpPixels(9),
	SetWalkingSpeed(VERY_FAST),
	ShiftZUpPixels(5),
	SetWalkingSpeed(FAST),
	ShiftZUpPixels(3),
	SetWalkingSpeed(NORMAL),
	ShiftZUpPixels(2),
	SetWalkingSpeed(SLOW),
	ShiftZUpPixels(1),
	SetWalkingSpeed(VERY_SLOW),
	ShiftZUpPixels(1),
	SetWalkingSpeed(VERY_SLOW),
	ShiftZDownPixels(1),
	SetWalkingSpeed(SLOW),
	ShiftZDownPixels(1),
	SetWalkingSpeed(NORMAL),
	ShiftZDownPixels(2),
	SetWalkingSpeed(FAST),
	ShiftZDownPixels(3),
	SetWalkingSpeed(VERY_FAST),
	ShiftZDownPixels(5),
	SetWalkingSpeed(FASTEST),
	ShiftZDownPixels(9),
	JmpIfBitSet(TEMP_7043_5, ["ACTION_135_ret_29"]),
	Jmp(["ACTION_103_clear_solidity_bits_0"]),
	Return(identifier="ACTION_135_ret_29")
])
