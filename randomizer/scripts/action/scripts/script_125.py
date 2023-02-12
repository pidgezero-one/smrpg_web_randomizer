#A0125_MK_BRANCH_HALLWAY_HENCHMAN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetBit(TEMP_7043_5, identifier="ACTION_125_set_bit_0"),
	SetVarToRandom(PRIMARY_TEMP_700C, 2),
	Inc(PRIMARY_TEMP_700C),
	LoadMemory(PRIMARY_TEMP_700C),
	JmpToSubroutine(["ACTION_103_clear_solidity_bits_0"]),
	EndLoop(),
	JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_106_set_animation_speed_0"]),
	FaceSouthwest(),
	Jmp(["ACTION_125_set_bit_0"])
])
