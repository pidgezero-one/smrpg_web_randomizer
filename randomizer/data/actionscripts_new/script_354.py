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
	SequenceLoopingOn(),
	SetPriority(3),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_354_face_northeast_20"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_354_set_solidity_bits_30"]),
	SetSolidityBits(cant_jump_through=True),
	FaceSoutheast(),
	SetObjectMemoryBits(arg_1=0x0B, bits=[1], identifier="ACTION_354_set_object_memory_bits_7"),
	SetWalkingSpeed(speed=SLOW),
	AddZCoord1Step(),
	StartLoopNTimes(7),
	TurnClockwise45DegreesNTimes(7),
	Walk1StepFDirection(),
	Pause(16),
	JmpIfRandom1of2(["ACTION_354_end_loop_16"]),
	Pause(16),
	EndLoop(identifier="ACTION_354_end_loop_16"),
	DecZCoord1Step(),
	Pause(20),
	Jmp(["ACTION_354_set_object_memory_bits_7"]),
	FaceNortheast(identifier="ACTION_354_face_northeast_20"),
	SetWalkingSpeed(speed=NORMAL, identifier="ACTION_354_set_animation_speed_21"),
	ShiftZUpSteps(3),
	ShiftZDownSteps(2),
	JmpIfBitSet(TEMP_7043_3, ["ACTION_354_set_solidity_bits_30"]),
	DecZCoord1Step(),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftFDirectionSteps(4),
	TurnClockwise45DegreesNTimes(4),
	Jmp(["ACTION_354_set_animation_speed_21"]),
	SetSolidityBits(cant_pass_walls=True, identifier="ACTION_354_set_solidity_bits_30"),
	SetSolidityBits(cant_pass_npcs=True, bit_7=True),
	SetAllSpeeds(speed=FAST, identifier="ACTION_354_set_animation_speed_32"),
	StartLoopNTimes(1),
	TurnClockwise45Degrees(),
	ShiftFDirectionSteps(2),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=X, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_700C, 3072),
	JmpIfComparisonResultIsLesser(["ACTION_354_set_animation_speed_42"]),
	SetAllSpeeds(speed=NORMAL),
	EndLoop(),
	Jmp(["ACTION_354_set_animation_speed_32"]),
	SetAllSpeeds(speed=FAST, identifier="ACTION_354_set_animation_speed_42"),
	ShiftSoutheastSteps(3),
	ShiftNortheastSteps(6),
	Jmp(["ACTION_354_set_animation_speed_32"])
])
