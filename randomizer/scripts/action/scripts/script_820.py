#A0820_JUMP_OFF_SPINNING_FLOWER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	PlaySound(sound=SO010_TRAMPOLINE, channel=4),
	JmpIfBitSet(SPINNING_FLOWER_2, ["ACTION_820_set_animation_speed_3"]),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetWalkingSpeed(FASTER, identifier="ACTION_820_set_animation_speed_3"),
	JumpToHeight(height=136, silent=True),
	ShiftFDirectionPixels(3, identifier="ACTION_820_shift_f_direction_pixels_5"),
	JmpIfMarioInAir(["ACTION_820_shift_f_direction_pixels_5"]),
	SetWalkingSpeed(NORMAL),
	SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	Return()
])
