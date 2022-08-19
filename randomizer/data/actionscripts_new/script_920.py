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
	PlaySound(sound=S117_SPINNING_MONSTER, channel=4),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=F, pixel=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_920_set_sprite_sequence_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_920_set_sprite_sequence_14"]),
	SetSpriteSequence(index=6, is_mold=True, is_sequence=True),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	Pause(240),
	PlaySound(sound=S117_SPINNING_MONSTER, channel=4),
	SetSpriteSequence(index=8, looping_off=True),
	Pause(36),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	Return(),
	SetSpriteSequence(index=6, is_mold=True, is_sequence=True, mirror_sprite=True, identifier="ACTION_920_set_sprite_sequence_14"),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	Pause(120),
	SetSpriteSequence(index=8, looping_off=True, mirror_sprite=True),
	Pause(36),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	Return()
])
