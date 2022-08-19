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
	SetPriority(2, identifier="ACTION_707_set_priority_0"),
	SetWalkingSpeed(speed=FAST),
	SetSequenceSpeed(speed=FASTER),
	SetSpriteSequence(index=0, is_sequence=True),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	ShiftNorthwestSteps(6),
	SequenceLoopingOn(),
	FixedFCoordOn(),
	JmpIfBitSet(TEMP_7043_6, ["ACTION_707_set_animation_speed_43"]),
	SetVarToRandom(PRIMARY_TEMP_700C, 60, identifier="ACTION_707_set_var_to_random_10"),
	CompareVarToConst(PRIMARY_TEMP_700C, 30),
	JmpIfComparisonResultIsLesser(["ACTION_707_jmp_if_bit_set_24"]),
	LoadMemory(PRIMARY_TEMP_700C, identifier="ACTION_707_load_mem_13"),
	Pause(1),
	EndLoop(),
	JmpIfBitSet(TEMP_7043_3, ["ACTION_707_jmp_if_bit_set_24"]),
	SetWalkingSpeed(speed=VERY_SLOW),
	SetSequenceSpeed(speed=FAST),
	SetSpriteSequence(index=0, is_sequence=True),
	ShiftNorthwestPixels(8),
	ShiftSoutheastPixels(8),
	JmpIfBitSet(TEMP_7043_6, ["ACTION_707_set_animation_speed_43"]),
	Jmp(["ACTION_707_set_var_to_random_10"]),
	JmpIfBitSet(TEMP_7043_6, ["ACTION_707_set_animation_speed_43"], identifier="ACTION_707_jmp_if_bit_set_24"),
	JmpIfVarEqualsConst(TEMP_70AE, 3, ["ACTION_707_load_mem_13"]),
	Inc(TEMP_70AE),
	SetWalkingSpeed(speed=SLOW),
	SetSequenceSpeed(speed=NORMAL),
	PlaySound(sound=S030_SURPRISED_MONSTER, channel=4),
	JumpToHeight(56),
	SetSpriteSequence(index=2, looping_off=True, is_sequence=True),
	Pause(32),
	SetSpriteSequence(index=1, is_sequence=True),
	SetSequenceSpeed(speed=FAST),
	ShiftNorthwestSteps(6),
	SetSpriteSequence(index=0, is_sequence=True),
	ShiftSoutheastSteps(3),
	JmpIfBitSet(TEMP_7043_6, ["ACTION_707_shift_southeast_steps_42"]),
	Dec(TEMP_70AE),
	ShiftSoutheastSteps(3),
	Jmp(["ACTION_707_set_var_to_random_10"]),
	ShiftSoutheastSteps(3, identifier="ACTION_707_shift_southeast_steps_42"),
	SetSequenceSpeed(speed=NORMAL, identifier="ACTION_707_set_animation_speed_43"),
	SetWalkingSpeed(speed=SLOW),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	Walk1StepSoutheast(identifier="ACTION_707_walk_1_step_southeast_46"),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=X, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_700C, 5888),
	JmpIfComparisonResultIsLesser(["ACTION_707_walk_1_step_southeast_46"]),
	Return()
])
