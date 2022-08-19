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
	FixedFCoordOn(),
	SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	SetSpriteSequence(index=2, is_sequence=True),
	SequenceLoopingOn(),
	SetSequenceSpeed(speed=NORMAL),
	Pause(1, identifier="ACTION_780_pause_5"),
	JmpIfBitClear(TEMP_7044_5, ["ACTION_780_pause_5"]),
	SetPriority(3),
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 319, ["ACTION_780_object_memory_modify_bits_44"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 403, ["ACTION_780_object_memory_modify_bits_44"]),
	Set700CToPressedButton(),
	DecVarFrom700C(SECONDARY_TEMP_7024),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_780_face_south_19"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_780_face_southwest_17"]),
	FaceNorth(),
	Jmp(["ACTION_780_jmp_if_bit_clear_39"]),
	FaceSouthwest(identifier="ACTION_780_face_southwest_17"),
	Jmp(["ACTION_780_jmp_if_bit_clear_30"]),
	FaceSouth(identifier="ACTION_780_face_south_19"),
	JmpIfBitClear(TEMP_7043_2, ["ACTION_780_set_animation_speed_24"], identifier="ACTION_780_jmp_if_bit_clear_20"),
	SetWalkingSpeed(speed=FAST),
	ClearSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
	Jmp(["ACTION_780_walk_1_step_f_direction_26"]),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_780_set_animation_speed_24"),
	SetSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
	Walk1StepFDirection(identifier="ACTION_780_walk_1_step_f_direction_26"),
	TurnClockwise45DegreesNTimes(7),
	ShiftFDirectionSteps(2),
	TurnClockwise45DegreesNTimes(6),
	JmpIfBitClear(TEMP_7043_2, ["ACTION_780_set_animation_speed_34"], identifier="ACTION_780_jmp_if_bit_clear_30"),
	SetWalkingSpeed(speed=FAST),
	ClearSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
	Jmp(["ACTION_780_shift_f_direction_steps_36"]),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_780_set_animation_speed_34"),
	SetSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
	ShiftFDirectionSteps(2, identifier="ACTION_780_shift_f_direction_steps_36"),
	TurnClockwise45DegreesNTimes(7),
	Walk1StepFDirection(),
	JmpIfBitClear(TEMP_7043_2, ["ACTION_780_pause_42"], identifier="ACTION_780_jmp_if_bit_clear_39"),
	Pause(24),
	Jmp(["ACTION_780_jmp_if_bit_clear_20"]),
	Pause(96, identifier="ACTION_780_pause_42"),
	Jmp(["ACTION_780_jmp_if_bit_clear_20"]),
	ObjectMemoryModifyBits(arg_1=0x09, set_flags=[5], clear_bits=[4, 6], identifier="ACTION_780_object_memory_modify_bits_44"),
	SetSolidityBits(cant_jump_through=True, bit_4=True, cant_walk_through=True),
	Set700CToPressedButton(),
	DecVarFrom700C(TEMP_7026),
	JmpIfLoadedMemoryIs0(["ACTION_780_set_animation_speed_53"]),
	SetWalkingSpeed(speed=SLOW),
	TurnClockwise45Degrees(),
	Walk1StepFDirection(),
	Jmp(["ACTION_780_object_memory_modify_bits_44"]),
	SetWalkingSpeed(speed=NORMAL, identifier="ACTION_780_set_animation_speed_53"),
	FaceMario(),
	JmpIfObjectWithinRange(object=MARIO, usually=0, tiles=4, destinations=["ACTION_780_set_animation_speed_67"]),
	JmpIfRandom2of3(['ACTION_780_turn_clockwise_45_degrees_n_times_60', 'ACTION_780_turn_clockwise_45_degrees_n_times_63']),
	TurnClockwise45DegreesNTimes(2),
	Pause(8),
	Jmp(["ACTION_780_walk_1_step_f_direction_65"]),
	TurnClockwise45DegreesNTimes(4, identifier="ACTION_780_turn_clockwise_45_degrees_n_times_60"),
	Pause(8),
	Jmp(["ACTION_780_walk_1_step_f_direction_65"]),
	TurnClockwise45DegreesNTimes(6, identifier="ACTION_780_turn_clockwise_45_degrees_n_times_63"),
	Pause(8),
	Walk1StepFDirection(identifier="ACTION_780_walk_1_step_f_direction_65"),
	Jmp(["ACTION_780_object_memory_modify_bits_44"]),
	SetWalkingSpeed(speed=FAST, identifier="ACTION_780_set_animation_speed_67"),
	TurnClockwise45DegreesNTimes(4),
	Walk1StepFDirection(),
	TurnClockwise45DegreesNTimes(4),
	Pause(4),
	JmpIfRandom2of3(['ACTION_780_turn_clockwise_45_degrees_n_times_75', 'ACTION_780_turn_clockwise_45_degrees_n_times_77']),
	TurnClockwise45DegreesNTimes(3),
	Jmp(["ACTION_780_walk_1_step_f_direction_78"]),
	TurnClockwise45DegreesNTimes(4, identifier="ACTION_780_turn_clockwise_45_degrees_n_times_75"),
	Jmp(["ACTION_780_walk_1_step_f_direction_78"]),
	TurnClockwise45DegreesNTimes(5, identifier="ACTION_780_turn_clockwise_45_degrees_n_times_77"),
	Walk1StepFDirection(identifier="ACTION_780_walk_1_step_f_direction_78"),
	Jmp(["ACTION_780_object_memory_modify_bits_44"])
])
