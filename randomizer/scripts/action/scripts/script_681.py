#A0681_MUSHROOM_DERBY_UNKNOWN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=True, identifier="ACTION_681_set_sprite_sequence_0"),
	JumpToHeight(height=108, silent=True),
	Pause(1, identifier="ACTION_681_pause_2"),
	JmpIfBitSet(TEMP_7043_1, ["ACTION_681_ret_7"]),
	JmpIfMarioInAir(["ACTION_681_pause_2"]),
	Pause(30),
	Jmp(["ACTION_681_set_sprite_sequence_0"]),
	Return(identifier="ACTION_681_ret_7")
])
