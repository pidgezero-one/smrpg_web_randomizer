#A0819_LANDS_END_GECKO_CANNON

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3),
	SequenceLoopingOff(),
	FixedFCoordOn(),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65516),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(9),
	EndLoop(),
	SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True, identifier="ACTION_819_set_sprite_sequence_8"),
	Pause(16),
	SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65515),
	AddConstToVar(PRIMARY_TEMP_700C, 25),
	SetMem704XAt700CBit(),
	AddConstToVar(PRIMARY_TEMP_700C, 4),
	SetMem704XAt700CBit(),
	Pause(16),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65515),
	AddConstToVar(PRIMARY_TEMP_700C, 25),
	ClearMem704XAt700CBit(),
	AddConstToVar(PRIMARY_TEMP_700C, 4),
	ClearMem704XAt700CBit(),
	SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(16),
	SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(16),
	Jmp(["ACTION_819_set_sprite_sequence_8"])
])
