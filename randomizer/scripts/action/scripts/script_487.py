#A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Set700CToPressedButton(identifier="ACTION_487_set_700C_to_pressed_button_0"),
	AddConstToVar(PRIMARY_TEMP_700C, 65516),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(1),
	EndLoop(),
	JumpToHeight(64, identifier="ACTION_487_jump_to_height_5"),
	Pause(1),
	JmpIfMarioInAir(["ACTION_487_jump_to_height_5"]),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_487_set_700C_to_pressed_button_0"]),
	Return()
])
