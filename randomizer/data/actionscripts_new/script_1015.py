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
	SetSpriteSequence(index=0, is_mold=True),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
	Pause(110),
	Pause(60),
	SetSpriteSequence(index=6, is_mold=True),
	Pause(80),
	SetSpriteSequence(index=0, is_mold=True),
	Pause(20),
	SetSpriteSequence(index=6, is_mold=True, identifier="ACTION_1015_set_sprite_sequence_8"),
	Pause(5),
	SetSpriteSequence(index=0, is_mold=True),
	Pause(10),
	SetSpriteSequence(index=6, is_mold=True),
	Pause(20),
	SetSpriteSequence(index=0, is_mold=True),
	Pause(5),
	SetSpriteSequence(index=6, is_mold=True),
	Pause(10),
	SetSpriteSequence(index=0, is_mold=True),
	Pause(3),
	SetSpriteSequence(index=6, is_mold=True),
	Pause(5),
	SetSpriteSequence(index=0, is_mold=True),
	Pause(5),
	SetSpriteSequence(index=6, is_mold=True),
	Pause(15),
	SetSpriteSequence(index=0, is_mold=True),
	Pause(10),
	SetSpriteSequence(index=6, is_mold=True),
	Pause(15),
	SetSpriteSequence(index=0, is_mold=True),
	Pause(15),
	SetSpriteSequence(index=6, is_mold=True),
	Pause(7),
	SetSpriteSequence(index=0, is_mold=True),
	Pause(7),
	SetSpriteSequence(index=6, is_mold=True),
	Pause(40),
	SetSpriteSequence(index=0, is_mold=True),
	Jmp(["ACTION_1015_set_sprite_sequence_8"]),
	Return()
])
