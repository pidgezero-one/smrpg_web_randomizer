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
	SetSpriteSequence(index=8, is_sequence=True),
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 319, ["ACTION_713_pause_33"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 403, ["ACTION_713_pause_33"]),
	SetPriority(3),
	JmpIfBitSet(TEMP_7043_4, ["ACTION_713_set_animation_speed_8"], identifier="ACTION_713_jmp_if_bit_set_6"),
	PlaySound(sound=S009_GREEN_SWITCH, channel=4),
	SetAllSpeeds(speed=FAST, identifier="ACTION_713_set_animation_speed_8"),
	ShiftZUpPixels(8),
	ShiftZDownPixels(8),
	SetAllSpeeds(speed=NORMAL),
	ClearBit(TEMP_7043_1),
	ClearSolidityBits(cant_walk_through=True),
	VisibilityOff(),
	SetVarToConst(TEMP_70AE, 0),
	Pause(56),
	SetVarToRandom(PRIMARY_TEMP_700C, 8),
	Inc(PRIMARY_TEMP_700C),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(8),
	EndLoop(),
	PlaySound(sound=S009_GREEN_SWITCH, channel=4),
	SetAllSpeeds(speed=FAST),
	SetBit(TEMP_7043_1),
	ClearBit(TEMP_7043_4),
	VisibilityOn(),
	SetSolidityBits(cant_walk_through=True),
	ShiftZUpPixels(8),
	ShiftZDownPixels(8),
	SetAllSpeeds(speed=NORMAL),
	Pause(100),
	Jmp(["ACTION_713_jmp_if_bit_set_6"]),
	Pause(1, identifier="ACTION_713_pause_33"),
	JmpIfBitClear(TEMP_7044_5, ["ACTION_713_pause_33"]),
	JmpIfBitSet(TEMP_7043_4, ["ACTION_713_set_animation_speed_37"], identifier="ACTION_713_jmp_if_bit_set_35"),
	PlaySound(sound=S009_GREEN_SWITCH, channel=4),
	SetAllSpeeds(speed=FAST, identifier="ACTION_713_set_animation_speed_37"),
	ShiftZUpPixels(8),
	ShiftZDownPixels(8),
	SetAllSpeeds(speed=NORMAL),
	ClearBit(TEMP_7043_1),
	ClearSolidityBits(cant_walk_through=True),
	VisibilityOff(),
	SetVarToConst(TEMP_70AE, 0),
	SetVarToRandom(PRIMARY_TEMP_700C, 32768),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7034),
	CompareVarToConst(PRIMARY_TEMP_700C, 16384),
	JmpIfComparisonResultIsLesser(["ACTION_713_set_51"]),
	SetVarToConst(PRIMARY_TEMP_700C, 1),
	Jmp(["ACTION_713_add_short_mem_52"]),
	SetVarToConst(PRIMARY_TEMP_700C, 0, identifier="ACTION_713_set_51"),
	AddVarTo700C(SECONDARY_TEMP_7024, identifier="ACTION_713_add_short_mem_52"),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7026),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70A9),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	SetBit(TEMP_7044_4),
	SetObjectMemoryBits(arg_1=0x0E),
	Db(bytearray(b'\x97\x11')),
	ClearBit(TEMP_7044_4),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_700C),
	DecVarFrom700C(SECONDARY_TEMP_7024),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_713_set_object_memory_bits_66"]),
	SetObjectMemoryBits(arg_1=0x0E, bits=[1]),
	Jmp(["ACTION_713_pause_67"]),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0], identifier="ACTION_713_set_object_memory_bits_66"),
	Pause(1, identifier="ACTION_713_pause_67"),
	PlaySound(sound=S009_GREEN_SWITCH, channel=4),
	SetAllSpeeds(speed=FAST),
	SetBit(TEMP_7043_1),
	ClearBit(TEMP_7043_4),
	SetSolidityBits(cant_walk_through=True),
	VisibilityOn(),
	ShiftZUpPixels(8),
	ShiftZDownPixels(8),
	SetAllSpeeds(speed=NORMAL),
	Pause(100),
	Jmp(["ACTION_713_jmp_if_bit_set_35"])
])
