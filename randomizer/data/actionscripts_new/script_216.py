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
	JmpIfRandom1of2(["ACTION_216_set_animation_speed_3"]),
	SetWalkingSpeed(speed=NORMAL),
	Jmp(["ACTION_216_set_6"]),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_216_set_animation_speed_3"),
	Jmp(["ACTION_216_set_6"]),
	SetWalkingSpeed(speed=FAST),
	SetVarToConst(PRIMARY_TEMP_700C, 3, identifier="ACTION_216_set_6"),
	ShiftZ20Steps(),
	JmpIfRandom1of2(["ACTION_216_jmp_if_bit_set_21"]),
	JmpIfBitSet(TEMP_7043_0, ["ACTION_216_turn_clockwise_45_degrees_n_times_12"]),
	TurnClockwise45DegreesNTimes(2),
	Jmp(["ACTION_216_pause_13"]),
	TurnClockwise45DegreesNTimes(6, identifier="ACTION_216_turn_clockwise_45_degrees_n_times_12"),
	Pause(10, identifier="ACTION_216_pause_13"),
	JmpIfRandom1of2(["ACTION_216_set_animation_speed_17"]),
	SetWalkingSpeed(speed=NORMAL),
	Jmp(["ACTION_216_set_6"]),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_216_set_animation_speed_17"),
	Jmp(["ACTION_216_set_6"]),
	SetWalkingSpeed(speed=FAST),
	Jmp(["ACTION_216_set_6"]),
	JmpIfBitSet(TEMP_7043_0, ["ACTION_216_turn_clockwise_45_degrees_n_times_28"], identifier="ACTION_216_jmp_if_bit_set_21"),
	TurnClockwise45DegreesNTimes(2),
	Pause(4),
	TurnClockwise45DegreesNTimes(2),
	Pause(4),
	SetBit(TEMP_7043_0),
	Jmp(["ACTION_216_set_6"]),
	TurnClockwise45DegreesNTimes(6, identifier="ACTION_216_turn_clockwise_45_degrees_n_times_28"),
	Pause(4),
	TurnClockwise45DegreesNTimes(6),
	Pause(4),
	ClearBit(TEMP_7043_0),
	Jmp(["ACTION_216_set_6"])
])
