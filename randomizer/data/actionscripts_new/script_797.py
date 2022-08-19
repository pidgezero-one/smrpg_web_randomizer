#classes
from randomizer.types.actionscripts.commands import *
from randomizer.types.actionscripts.classes import ActionScript
#ids
from randomizer.types.eventscripts.constants.script_ids import *
from randomizer.types.actionscripts.constants.script_ids import *
from randomizer.types.packets.constants.packet_ids import *
from randomizer.types.constants.sound_names import *
from randomizer.types.constants.directions import *
#types
from randomizer.types.constants.area_objects import *
from randomizer.types.constants.coords import *
from randomizer.types.actionscripts.constants.sequence_speeds import *
from randomizer.types.actionscripts.constants.vram_priority import *
from randomizer.types.variables.variables import *

script = ActionScript([
	SetVarToRandom(PRIMARY_TEMP_700C, 80, identifier="ACTION_797_set_var_to_random_0"),
	DecVarFrom700C(ROSE_WAY_7038),
	JmpIfComparisonResultIsGreaterOrEqual(["ACTION_797_jmp_to_subroutine_9"]),
	DecVarFrom700C(ROSE_WAY_703A),
	JmpIfComparisonResultIsGreaterOrEqual(["ACTION_797_jmp_to_subroutine_13"]),
	JmpToSubroutine(["ACTION_797_set_animation_speed_17"]),
	JmpToSubroutine(["ACTION_797_dec_short_43"]),
	JmpIfVarEqualsConst(Z_COORD_1, 1, ["ACTION_797_shift_northeast_pixels_29"]),
	Jmp(["ACTION_797_set_var_to_random_0"]),
	JmpToSubroutine(["ACTION_797_set_animation_speed_25"], identifier="ACTION_797_jmp_to_subroutine_9"),
	JmpToSubroutine(["ACTION_797_dec_short_43"]),
	JmpIfVarEqualsConst(Z_COORD_1, 1, ["ACTION_797_shift_northeast_pixels_29"]),
	Jmp(["ACTION_797_set_var_to_random_0"]),
	JmpToSubroutine(["ACTION_797_set_animation_speed_21"], identifier="ACTION_797_jmp_to_subroutine_13"),
	JmpToSubroutine(["ACTION_797_dec_short_43"]),
	JmpIfVarEqualsConst(Z_COORD_1, 1, ["ACTION_797_shift_northeast_pixels_29"]),
	Jmp(["ACTION_797_set_var_to_random_0"]),
	SetSequenceSpeed(speed=FAST, identifier="ACTION_797_set_animation_speed_17"),
	SetWalkingSpeed(speed=VERY_SLOW),
	Walk1StepNortheast(),
	Return(),
	SetSequenceSpeed(speed=FAST, identifier="ACTION_797_set_animation_speed_21"),
	SetWalkingSpeed(speed=SLOW),
	Walk1StepNortheast(),
	Return(),
	SetSequenceSpeed(speed=VERY_FAST, identifier="ACTION_797_set_animation_speed_25"),
	SetWalkingSpeed(speed=NORMAL),
	Walk1StepNortheast(),
	Return(),
	ShiftNortheastPixels(8, identifier="ACTION_797_shift_northeast_pixels_29"),
	JmpIfBitSet(TEMP_7043_5, ["ACTION_797_set_animation_speed_39"]),
	JmpIfBitSet(TEMP_7043_7, ["ACTION_797_set_animation_speed_39"]),
	JmpIfBitSet(TEMP_7043_6, ["ACTION_797_set_animation_speed_39"]),
	SetBit(TEMP_7044_6),
	ClearBit(UNKNOWN_MUSHROOM_DERBY_7085_4),
	ShiftNortheastPixels(8),
	SetSequenceSpeed(speed=SLOW),
	SetVarToConst(Z_COORD_1, 0),
	Return(),
	SetSequenceSpeed(speed=SLOW, identifier="ACTION_797_set_animation_speed_39"),
	ShiftNortheastPixels(8),
	SetVarToConst(Z_COORD_1, 0),
	Return(),
	Dec(Z_COORD_1, identifier="ACTION_797_dec_short_43"),
	Return()
])
