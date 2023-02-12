#A0386_TOWER_SHOOT_BULLET_BILLS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceSoutheast(),
	Pause(18),
	FaceSouthwest(),
	Pause(18),
	SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True, identifier="ACTION_386_set_sprite_sequence_4"),
	Pause(4),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
	Pause(4),
	SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True),
	Pause(8),
	SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True),
	Pause(8),
	SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True),
	Pause(8),
	SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True),
	Pause(8),
	SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True),
	Pause(16),
	SetBit(TEMP_7043_3),
	SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True),
	Pause(4),
	SetSpriteSequence(index=20, is_mold=True, is_sequence=True, looping=True),
	Pause(4),
	SetSpriteSequence(index=23, is_mold=True, is_sequence=True, looping=True),
	Pause(24),
	SetSpriteSequence(index=22, is_mold=True, is_sequence=True, looping=True),
	Pause(8),
	Jmp(["ACTION_386_set_sprite_sequence_4"])
])
