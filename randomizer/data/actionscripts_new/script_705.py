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
	SetVarToRandom(PRIMARY_TEMP_700C, 16, identifier="ACTION_705_set_var_to_random_0"),
	AddConstToVar(PRIMARY_TEMP_700C, 15),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(2),
	EndLoop(),
	JmpIfRandom2of3(['ACTION_705_set_animation_speed_14', 'ACTION_705_set_animation_speed_19']),
	Pause(31),
	JmpIfRandom2of3(['ACTION_705_set_animation_speed_14', 'ACTION_705_set_animation_speed_19']),
	SetWalkingSpeed(speed=VERY_FAST),
	JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
	ShiftSoutheastSteps(32),
	JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
	Pause(71),
	Jmp(["ACTION_705_set_var_to_random_0"]),
	SetWalkingSpeed(speed=FASTEST, identifier="ACTION_705_set_animation_speed_14"),
	JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
	ShiftSouthSteps(16),
	JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
	Pause(41),
	SetWalkingSpeed(speed=VERY_FAST, identifier="ACTION_705_set_animation_speed_19"),
	JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
	ShiftNorthwestSteps(32),
	JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
	Pause(71),
	Jmp(["ACTION_705_set_var_to_random_0"]),
	Return(identifier="ACTION_705_ret_25")
])
