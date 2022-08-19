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
	SetObjectMemoryBits(arg_1=0x0B, bits=[1], identifier="ACTION_656_set_object_memory_bits_0"),
	SetSolidityBits(cant_walk_through=True),
	SetSolidityBits(bit_4=True),
	SetVarToConst(TEMP_702A, 7),
	SetVarToConst(ROSE_WAY_703A, 20),
	SetSequenceSpeed(speed=FAST, identifier="ACTION_656_set_animation_speed_5"),
	SetWalkingSpeed(speed=VERY_SLOW),
	Walk1StepNortheast(),
	JmpToSubroutine(["ACTION_656_dec_short_29"]),
	JmpIfVarEqualsConst(ROSE_WAY_703A, 0, ["ACTION_656_set_animation_speed_21"]),
	JmpIfRandom2of3(['ACTION_656_set_animation_speed_5', 'ACTION_656_jmp_if_var_equals_const_12']),
	Jmp(["ACTION_656_set_animation_speed_5"]),
	JmpIfVarEqualsConst(TEMP_702A, 0, ["ACTION_656_set_animation_speed_5"], identifier="ACTION_656_jmp_if_var_equals_const_12"),
	SetSequenceSpeed(speed=VERY_FAST),
	SetWalkingSpeed(speed=SLOW),
	Walk1StepNortheast(),
	JmpToSubroutine(["ACTION_656_dec_short_29"]),
	JmpIfVarEqualsConst(ROSE_WAY_703A, 0, ["ACTION_656_set_animation_speed_21"]),
	JmpToSubroutine(["ACTION_656_dec_short_31"]),
	JmpIfRandom2of3(['ACTION_656_jmp_if_var_equals_const_12', 'ACTION_656_set_animation_speed_5']),
	Jmp(["ACTION_656_jmp_if_var_equals_const_12"]),
	SetSequenceSpeed(speed=NORMAL, identifier="ACTION_656_set_animation_speed_21"),
	FaceSouthwest(),
	Pause(60),
	SetWalkingSpeed(speed=SLOW),
	ShiftSouthwestSteps(20),
	FaceNortheast(),
	Pause(60),
	Jmp(["ACTION_656_set_object_memory_bits_0"]),
	Dec(ROSE_WAY_703A, identifier="ACTION_656_dec_short_29"),
	Return(),
	Dec(TEMP_702A, identifier="ACTION_656_dec_short_31"),
	Return()
])
