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
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 463, ["ACTION_59_set_700C_to_object_coord_23"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 464, ["ACTION_59_set_700C_to_object_coord_23"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 465, ["ACTION_59_set_700C_to_object_coord_23"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 466, ["ACTION_59_set_700C_to_object_coord_23"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 467, ["ACTION_59_set_700C_to_object_coord_23"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 468, ["ACTION_59_set_700C_to_object_coord_23"]),
	ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
	SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
	FaceSouthwest(),
	SetWalkingSpeed(speed=FAST, identifier="ACTION_59_set_animation_speed_10"),
	ShiftFDirectionSteps(2),
	Pause(32),
	ShiftFDirectionSteps(2),
	Pause(32),
	ShiftFDirectionSteps(2),
	Pause(32),
	ShiftFDirectionSteps(2),
	Pause(32),
	JumpToHeight(height=60, silent=True),
	ShiftFDirectionSteps(2),
	TurnRandomDirection(),
	Jmp(["ACTION_59_set_animation_speed_10"]),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=F, pixel=True, identifier="ACTION_59_set_700C_to_object_coord_23"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_59_set_sprite_sequence_32"]),
	SetSpriteSequence(index=21, is_mold=True, is_sequence=True),
	Pause(8),
	SetSpriteSequence(index=22, is_mold=True, is_sequence=True),
	Pause(8),
	JmpIfBitClear(TEMP_7044_7, ["ACTION_59_set_700C_to_object_coord_23"]),
	SetSpriteSequence(index=0, is_sequence=True),
	Return(),
	SetSpriteSequence(index=21, is_mold=True, is_sequence=True, mirror_sprite=True, identifier="ACTION_59_set_sprite_sequence_32"),
	Pause(8),
	SetSpriteSequence(index=22, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(8),
	JmpIfBitClear(TEMP_7044_7, ["ACTION_59_set_700C_to_object_coord_23"]),
	SetSpriteSequence(index=0, is_sequence=True, mirror_sprite=True),
	Return()
])
