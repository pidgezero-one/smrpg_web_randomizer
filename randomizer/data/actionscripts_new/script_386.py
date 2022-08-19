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
	FaceSoutheast(),
	Pause(18),
	FaceSouthwest(),
	Pause(18),
	SetSpriteSequence(index=9, is_mold=True, is_sequence=True, identifier="ACTION_386_set_sprite_sequence_4"),
	Pause(4),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
	Pause(4),
	SetSpriteSequence(index=13, is_mold=True, is_sequence=True),
	Pause(8),
	SetSpriteSequence(index=15, is_mold=True, is_sequence=True),
	Pause(8),
	SetSpriteSequence(index=16, is_mold=True, is_sequence=True),
	Pause(8),
	SetSpriteSequence(index=17, is_mold=True, is_sequence=True),
	Pause(8),
	SetSpriteSequence(index=18, is_mold=True, is_sequence=True),
	Pause(16),
	SetBit(TEMP_7043_3),
	SetSpriteSequence(index=19, is_mold=True, is_sequence=True),
	Pause(4),
	SetSpriteSequence(index=20, is_mold=True, is_sequence=True),
	Pause(4),
	SetSpriteSequence(index=23, is_mold=True, is_sequence=True),
	Pause(24),
	SetSpriteSequence(index=22, is_mold=True, is_sequence=True),
	Pause(8),
	Jmp(["ACTION_386_set_sprite_sequence_4"])
])
