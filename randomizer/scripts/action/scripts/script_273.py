#A0273_VOLCANO_DRY_BONES_COLLAPSE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Set700CToObjectCoord(object=DUMMY_0X07, coord=COORD_F, pixel=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_273_set_sprite_sequence_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_273_set_sprite_sequence_8"]),
	SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	Pause(360),
	Jmp(["ACTION_272_play_sound_17"]),
	SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_273_set_sprite_sequence_8"),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	Pause(360),
	Jmp(["ACTION_272_play_sound_42"])
])
