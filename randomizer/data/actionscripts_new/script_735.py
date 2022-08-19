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
	SetAllSpeeds(speed=FAST),
	ClearSolidityBits(cant_pass_walls=True),
	JmpIfBitSet(MINES_BOSS_1_DEFEATED, ["ACTION_730_clear_solidity_bits_54"], identifier="ACTION_735_jmp_if_bit_set_3"),
	VisibilityOff(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 21, ["ACTION_735_transfer_to_xyzf_29"]),
	SetBit(TEMP_7044_6),
	JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 17, ["ACTION_735_pause_14"]),
	JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 27, ["ACTION_735_pause_17"]),
	JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 23, ["ACTION_735_pause_20"]),
	JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 25, ["ACTION_735_pause_23"]),
	JmpIfVarEqualsConst(MINES_MIDBOSS_POSITION, 19, ["ACTION_735_pause_26"]),
	Pause(200, identifier="ACTION_735_pause_14"),
	SetVarToConst(MINES_MIDBOSS_POSITION, 27),
	Jmp(["ACTION_735_jmp_if_bit_set_3"]),
	Pause(200, identifier="ACTION_735_pause_17"),
	SetVarToConst(MINES_MIDBOSS_POSITION, 23),
	Jmp(["ACTION_735_jmp_if_bit_set_3"]),
	Pause(100, identifier="ACTION_735_pause_20"),
	SetVarToConst(MINES_MIDBOSS_POSITION, 25),
	Jmp(["ACTION_735_jmp_if_bit_set_3"]),
	Pause(200, identifier="ACTION_735_pause_23"),
	SetVarToConst(MINES_MIDBOSS_POSITION, 19),
	Jmp(["ACTION_735_jmp_if_bit_set_3"]),
	Pause(100, identifier="ACTION_735_pause_26"),
	SetVarToConst(MINES_MIDBOSS_POSITION, 21),
	Jmp(["ACTION_735_jmp_if_bit_set_3"]),
	TransferToXYZF(x=16, y=58, z=4, direction=EAST, identifier="ACTION_735_transfer_to_xyzf_29"),
	JmpIfBitSet(TEMP_7044_6, ["ACTION_735_face_southeast_37"]),
	SetWalkingSpeed(speed=FASTEST),
	ShiftSoutheastSteps(2),
	SetWalkingSpeed(speed=FAST),
	SetBit(TEMP_7044_6),
	VisibilityOn(),
	Jmp(["ACTION_735_object_memory_clear_bit_40"]),
	Pause(1, identifier="ACTION_735_face_southeast_37"),
	FaceSoutheast(),
	VisibilityOn(),
	ShiftSoutheastSteps(2),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4], identifier="ACTION_735_object_memory_clear_bit_40"),
	SetSolidityBits(cant_walk_through=True),
	PlaySound(sound=S011_WHOOSH_AWAY, channel=4),
	ShiftSoutheastSteps(3),
	SequenceLoopingOn(),
	Pause(8),
	JumpToHeight(64),
	ShiftSoutheastSteps(2),
	SequenceLoopingOff(),
	Pause(16),
	ShiftNortheastSteps(5),
	ShiftSoutheastSteps(5),
	SetVarToConst(MINES_MIDBOSS_POSITION, 17),
	Jmp(["ACTION_735_jmp_if_bit_set_3"])
])
