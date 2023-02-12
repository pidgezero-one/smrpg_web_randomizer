#A0676_MUSHROOM_DERBY_UNKNOWN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetObjectMemoryBits(arg_1=0x0B, bits=[1], identifier="ACTION_676_set_object_memory_bits_0"),
	SetSolidityBits(cant_walk_through=True),
	SetSolidityBits(bit_4=True),
	SetVarToConst(TEMP_702C, 4),
	SetVarToConst(TEMP_7030, 20),
	SetSequenceSpeed(FAST, identifier="ACTION_676_set_animation_speed_5"),
	SetWalkingSpeed(VERY_SLOW),
	Walk1StepNortheast(),
	JmpToSubroutine(["ACTION_676_dec_short_29"]),
	JmpIfVarEqualsConst(TEMP_7030, 0, ["ACTION_676_set_animation_speed_21"]),
	JmpIfRandom2of3(['ACTION_676_set_animation_speed_5', 'ACTION_676_jmp_if_var_equals_const_12']),
	Jmp(["ACTION_676_set_animation_speed_5"]),
	JmpIfVarEqualsConst(TEMP_702C, 0, ["ACTION_676_set_animation_speed_5"], identifier="ACTION_676_jmp_if_var_equals_const_12"),
	SetSequenceSpeed(VERY_FAST),
	SetWalkingSpeed(SLOW),
	Walk1StepNortheast(),
	JmpToSubroutine(["ACTION_676_dec_short_29"]),
	JmpIfVarEqualsConst(TEMP_7030, 0, ["ACTION_676_set_animation_speed_21"]),
	JmpToSubroutine(["ACTION_676_dec_short_31"]),
	JmpIfRandom2of3(['ACTION_676_jmp_if_var_equals_const_12', 'ACTION_676_set_animation_speed_5']),
	Jmp(["ACTION_676_jmp_if_var_equals_const_12"]),
	SetSequenceSpeed(NORMAL, identifier="ACTION_676_set_animation_speed_21"),
	FaceSouthwest(),
	Pause(60),
	SetWalkingSpeed(SLOW),
	ShiftSouthwestSteps(20),
	FaceNortheast(),
	Pause(60),
	Jmp(["ACTION_676_set_object_memory_bits_0"]),
	Dec(TEMP_7030, identifier="ACTION_676_dec_short_29"),
	Return(),
	Dec(TEMP_702C, identifier="ACTION_676_dec_short_31"),
	Return()
])
