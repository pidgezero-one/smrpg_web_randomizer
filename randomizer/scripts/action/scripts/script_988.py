#A0988_SMITHY_COMPONENT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpIfBitSet(TEMP_7043_2, ["ACTION_988_set_animation_speed_3"]),
	TransferXYZFPixels(x=252, y=6, z=30, direction=NORTHEAST),
	SetSpriteSequence(index=3, is_sequence=True, looping=True),
	SetWalkingSpeed(SLOW, identifier="ACTION_988_set_animation_speed_3"),
	ShiftZDownPixels(1),
	Pause(8),
	ShiftZDownPixels(1),
	Pause(12),
	ShiftZUpPixels(1),
	Pause(8),
	ShiftZUpPixels(1),
	Pause(12),
	JmpIfBitSet(TEMP_7043_5, ["ACTION_988_ret_14"]),
	Jmp(["ACTION_988_set_animation_speed_3"]),
	Return(identifier="ACTION_988_ret_14")
])
