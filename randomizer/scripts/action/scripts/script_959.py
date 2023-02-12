#A0959_FINAL_FACTORY_ROOM_MASS_PRODUCED_NPC_PICKED_UP

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(FASTEST, identifier="ACTION_959_set_animation_speed_0"),
	ShadowOff(),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	ShiftWestPixels(4),
	SetWalkingSpeed(SLOW),
	SetBit(TEMP_7044_1),
	ShiftNorthSteps(2),
	ShiftNorthPixels(8),
	JmpIfBitSet(TEMP_7044_0, ["ACTION_959_shift_z_up_steps_11"], identifier="ACTION_959_jmp_if_bit_set_8"),
	Pause(1),
	Jmp(["ACTION_959_jmp_if_bit_set_8"]),
	ShiftZUpSteps(3, identifier="ACTION_959_shift_z_up_steps_11"),
	WalkToXYCoords(x=3, y=88),
	ShadowOn(),
	SetWalkingSpeed(VERY_SLOW),
	ShiftSoutheastPixels(8),
	SetWalkingSpeed(SLOW),
	ShiftZDownSteps(3),
	Pause(12),
	ClearBit(TEMP_7044_0),
	ClearBit(TEMP_7044_1),
	WalkToXYCoords(x=10, y=103),
	ShiftToXYCoords(x=1, y=77),
	JmpIfBitSet(TEMP_7044_2, ["ACTION_959_ret_25"]),
	Jmp(["ACTION_959_set_animation_speed_0"]),
	Return(identifier="ACTION_959_ret_25")
])
