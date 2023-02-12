#A0653_SLOW_ROTATING_PLATFORM

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3),
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 455, ["ACTION_653_set_700C_to_pressed_button_6"]),
	Set700CToPressedButton(),
	CompareVarToConst(PRIMARY_TEMP_700C, 30),
	JmpIfComparisonResultIsGreaterOrEqual(["ACTION_653_set_vram_priority_11"]),
	Set700CToPressedButton(identifier="ACTION_653_set_700C_to_pressed_button_6"),
	AddConstToVar(PRIMARY_TEMP_700C, 65534),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=ACTIVE_NPC),
	Db(bytearray(b'\x97\x10')),
	Jmp(["ACTION_653_set_700C_to_pressed_button_6"]),
	SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES, identifier="ACTION_653_set_vram_priority_11"),
	Set700CToPressedButton(identifier="ACTION_653_set_700C_to_pressed_button_12"),
	AddConstToVar(PRIMARY_TEMP_700C, 65534),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=ACTIVE_NPC),
	TransferToObjectXY(MEM_70A8),
	Jmp(["ACTION_653_set_700C_to_pressed_button_12"])
])
