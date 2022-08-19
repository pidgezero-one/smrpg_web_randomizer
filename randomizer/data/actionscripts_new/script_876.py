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
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, mirror_sprite=True, identifier="ACTION_876_set_sprite_sequence_0"),
	Pause(170),
	SetSpriteSequence(index=16, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=17, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=16, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(5),
	SetSpriteSequence(index=16, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=17, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=16, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(120),
	SetSpriteSequence(index=16, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=17, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=16, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(3),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, mirror_sprite=True),
	Jmp(["ACTION_876_set_sprite_sequence_0"])
])
