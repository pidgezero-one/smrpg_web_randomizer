#A0703_TOWER_CHOMP_GROUP

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpIfRandom2of3(['ACTION_703_set_700C_to_pressed_button_18', 'ACTION_703_set_700C_to_pressed_button_18'], identifier="ACTION_703_jmp_if_random_above_66_0"),
	JmpIfRandom1of2(["ACTION_703_set_700C_to_pressed_button_10"]),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_703_set_sprite_sequence_7"]),
	SetSpriteSequence(index=3, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(58),
	Jmp(["ACTION_703_jmp_if_random_above_66_0"]),
	SetSpriteSequence(index=3, is_sequence=True, looping=True, identifier="ACTION_703_set_sprite_sequence_7"),
	Pause(58),
	Jmp(["ACTION_703_jmp_if_random_above_66_0"]),
	Set700CToPressedButton(identifier="ACTION_703_set_700C_to_pressed_button_10"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_703_set_sprite_sequence_15"]),
	SetSpriteSequence(index=4, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(56),
	Jmp(["ACTION_703_jmp_if_random_above_66_0"]),
	SetSpriteSequence(index=4, is_sequence=True, looping=True, identifier="ACTION_703_set_sprite_sequence_15"),
	Pause(56),
	Jmp(["ACTION_703_jmp_if_random_above_66_0"]),
	Set700CToPressedButton(identifier="ACTION_703_set_700C_to_pressed_button_18"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_703_set_sprite_sequence_23"]),
	SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
	Pause(112),
	Jmp(["ACTION_703_jmp_if_random_above_66_0"]),
	SetSpriteSequence(index=0, is_sequence=True, looping=True, identifier="ACTION_703_set_sprite_sequence_23"),
	Pause(112),
	Jmp(["ACTION_703_jmp_if_random_above_66_0"])
])
