#A0876_MONSTRO_MIMIC

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_876_set_sprite_sequence_0"),
	Pause(170),
	SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(5),
	SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(120),
	SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=17, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	Jmp(["ACTION_876_set_sprite_sequence_0"])
])
