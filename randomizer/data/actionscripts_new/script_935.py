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
	SetSolidityBits(cant_pass_walls=True),
	SetWalkingSpeed(speed=FASTEST),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	ShiftZUpSteps(8),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	FloatingOff(),
	SetVarToRandom(PRIMARY_TEMP_700C, 8, identifier="ACTION_935_set_var_to_random_6"),
	FaceEast7C(),
	ShiftFDirectionSteps(2),
	JmpIfRandom1of2(["ACTION_935_set_var_to_random_6"]),
	JmpIfRandom1of2(["ACTION_935_set_var_to_random_6"]),
	VisibilityOn(),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	FloatingOn(),
	SetBit(TEMP_7043_2),
	SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetAllSpeeds(speed=SLOW),
	JumpToHeight(height=0, silent=True),
	Pause(1, identifier="ACTION_935_pause_18"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_935_pause_18"]),
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_935_set_animation_speed_20"),
	SetSequenceSpeed(speed=FAST),
	Walk1StepFDirection(),
	JumpToHeight(height=0, silent=True),
	TurnRandomDirection(),
	Walk1StepFDirection(),
	JmpIfRandom1of2(["ACTION_935_set_animation_speed_20"]),
	FaceMario(),
	SetWalkingSpeed(speed=NORMAL),
	SetSequenceSpeed(speed=VERY_FAST),
	Walk1StepFDirection(),
	Jmp(["ACTION_935_set_animation_speed_20"])
])
