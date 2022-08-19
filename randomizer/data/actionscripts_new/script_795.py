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
	SetVarToRandom(PRIMARY_TEMP_700C, 80, identifier="ACTION_795_set_var_to_random_0"),
	DecVarFrom700C(Z_COORD_2),
	JmpIfComparisonResultIsGreaterOrEqual(["ACTION_795_jmp_to_subroutine_9"]),
	DecVarFrom700C(TEMP_7030),
	JmpIfComparisonResultIsGreaterOrEqual(["ACTION_795_jmp_to_subroutine_13"]),
	JmpToSubroutine(["ACTION_795_set_animation_speed_17"]),
	JmpToSubroutine(["ACTION_795_dec_short_42"]),
	JmpIfVarEqualsConst(TEMP_702E, 1, ["ACTION_795_shift_northeast_pixels_29"]),
	Jmp(["ACTION_795_set_var_to_random_0"]),
	JmpToSubroutine(["ACTION_795_set_animation_speed_25"], identifier="ACTION_795_jmp_to_subroutine_9"),
	JmpToSubroutine(["ACTION_795_dec_short_42"]),
	JmpIfVarEqualsConst(TEMP_702E, 1, ["ACTION_795_shift_northeast_pixels_29"]),
	Jmp(["ACTION_795_set_var_to_random_0"]),
	JmpToSubroutine(["ACTION_795_set_animation_speed_21"], identifier="ACTION_795_jmp_to_subroutine_13"),
	JmpToSubroutine(["ACTION_795_dec_short_42"]),
	JmpIfVarEqualsConst(TEMP_702E, 1, ["ACTION_795_shift_northeast_pixels_29"]),
	Jmp(["ACTION_795_set_var_to_random_0"]),
	SetSequenceSpeed(speed=FAST, identifier="ACTION_795_set_animation_speed_17"),
	SetWalkingSpeed(speed=VERY_SLOW),
	Walk1StepNortheast(),
	Return(),
	SetSequenceSpeed(speed=FAST, identifier="ACTION_795_set_animation_speed_21"),
	SetWalkingSpeed(speed=SLOW),
	Walk1StepNortheast(),
	Return(),
	SetSequenceSpeed(speed=VERY_FAST, identifier="ACTION_795_set_animation_speed_25"),
	SetWalkingSpeed(speed=NORMAL),
	Walk1StepNortheast(),
	Return(),
	ShiftNortheastPixels(8, identifier="ACTION_795_shift_northeast_pixels_29"),
	JmpIfBitClear(UNKNOWN_MUSHROOM_DERBY_7085_4, ["ACTION_795_set_animation_speed_39"]),
	JmpIfBitSet(TEMP_7043_5, ["ACTION_795_set_animation_speed_39"]),
	JmpIfBitSet(TEMP_7043_6, ["ACTION_795_set_animation_speed_39"]),
	JmpIfBitSet(TEMP_7044_6, ["ACTION_795_set_animation_speed_39"]),
	SetBit(TEMP_7043_7),
	ShiftNortheastPixels(8),
	SetSequenceSpeed(speed=SLOW),
	FaceSouthwest(),
	Jmp(["ACTION_677_jmp_if_random_above_66_0"]),
	SetSequenceSpeed(speed=SLOW, identifier="ACTION_795_set_animation_speed_39"),
	ShiftNortheastPixels(8),
	Return(),
	Dec(TEMP_702E, identifier="ACTION_795_dec_short_42"),
	Return()
])
