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
	Pause(21, identifier="ACTION_754_pause_0"),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	SetSpriteSequence(index=10, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(1),
	ShiftToXYCoords(x=3, y=43),
	SetSpriteSequence(index=8, looping_off=True, mirror_sprite=True),
	Pause(160),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	Pause(60),
	SetSpriteSequence(index=9, looping_off=True, mirror_sprite=True),
	Pause(292),
	ShiftToXYCoords(x=0, y=0),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	Pause(48),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	SetSpriteSequence(index=10, is_mold=True, is_sequence=True),
	Pause(1),
	ShiftToXYCoords(x=15, y=43),
	SetSpriteSequence(index=8, looping_off=True),
	Pause(160),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	Pause(60),
	SetSpriteSequence(index=9, looping_off=True),
	Pause(292),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	VisibilityOff(),
	Pause(48),
	SetSpriteSequence(index=10, is_mold=True, is_sequence=True),
	Pause(1),
	ShiftToXYCoords(x=11, y=19),
	VisibilityOn(),
	SetSpriteSequence(index=8, looping_off=True),
	Pause(160),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	Pause(60),
	SetSpriteSequence(index=9, looping_off=True),
	Pause(292),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	VisibilityOff(),
	Pause(48),
	SetSpriteSequence(index=10, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(1),
	ShiftToXYCoords(x=15, y=11),
	VisibilityOn(),
	SetSpriteSequence(index=8, looping_off=True, mirror_sprite=True),
	Pause(160),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	Pause(60),
	SetSpriteSequence(index=9, looping_off=True, mirror_sprite=True),
	Pause(292),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	VisibilityOff(),
	Pause(48),
	SetSpriteSequence(index=10, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(1),
	ShiftToXYCoords(x=1, y=15),
	VisibilityOn(),
	SetSpriteSequence(index=8, looping_off=True, mirror_sprite=True),
	Pause(160),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	Pause(60),
	SetSpriteSequence(index=9, looping_off=True, mirror_sprite=True),
	Pause(292),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	VisibilityOff(),
	Pause(21),
	Jmp(["ACTION_754_pause_0"])
])
