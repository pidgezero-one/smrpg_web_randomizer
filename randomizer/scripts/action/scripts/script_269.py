#A0269_BLOOBER_TAIL

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetMovementsBits(bit_0=True, cant_walk_under=True),
	SetSpriteSequence(index=8, is_sequence=True, looping=True),
	Pause(20),
	SetPriority(3),
	SetWalkingSpeed(SLOW, identifier="ACTION_269_set_animation_speed_4"),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=COORD_F, pixel=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_269_set_sprite_sequence_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_269_set_sprite_sequence_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_269_set_sprite_sequence_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_269_set_sprite_sequence_12"]),
	SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
	Jmp(["ACTION_269_shift_z_down_steps_13"]),
	SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_269_set_sprite_sequence_12"),
	ShiftZDownSteps(5, identifier="ACTION_269_shift_z_down_steps_13"),
	CopyVarToVar(from_var=TEMP_7032, to_var=PRIMARY_TEMP_700C),
	FaceEast7C(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_269_set_sprite_sequence_22"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_269_set_sprite_sequence_22"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_269_set_sprite_sequence_22"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_269_set_sprite_sequence_22"]),
	SetSpriteSequence(index=8, is_sequence=True, looping=True),
	Jmp(["ACTION_269_clear_solidity_bits_23"]),
	SetSpriteSequence(index=8, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_269_set_sprite_sequence_22"),
	ClearSolidityBits(cant_pass_walls=True, identifier="ACTION_269_clear_solidity_bits_23"),
	SetWalkingSpeed(FAST),
	SetSolidityBits(cant_pass_walls=True),
	StartLoopNTimes(39),
	ShiftZUpPixels(2),
	ShiftFDirectionPixels(1),
	EndLoop(),
	Jmp(["ACTION_269_set_animation_speed_4"])
])
