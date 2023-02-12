#A0428_YOSHI_FINISH_RACE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]),
	Pause(1, identifier="ACTION_428_pause_2"),
	JmpIfBitSet(TEMP_7043_2, ["ACTION_431_set_animation_speed_0"]),
	Jmp(["ACTION_428_pause_2"])
])
