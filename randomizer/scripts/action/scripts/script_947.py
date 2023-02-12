#A0947_FOREST_1ST_UNDERGROUND_RAT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOff(),
	Pause(96),
	VisibilityOn(),
	SetPriority(0, identifier="ACTION_947_set_priority_3"),
	Pause(160),
	SetPriority(3),
	PlaySound(sound=SO111_SLEEPING, channel=4),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
	Pause(8),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	Pause(8),
	SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
	Pause(8),
	SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
	Pause(8),
	SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
	Pause(8),
	SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True),
	Pause(24),
	SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
	Pause(4),
	SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
	Pause(4),
	SetSpriteSequence(index=2, is_mold=True, is_sequence=True, looping=True),
	Pause(4),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	Pause(4),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	Pause(4),
	Jmp(["ACTION_947_set_priority_3"])
])
