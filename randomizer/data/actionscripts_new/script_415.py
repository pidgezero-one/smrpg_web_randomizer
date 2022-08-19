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
	FaceNortheast(),
	SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, mirror_sprite=True),
	SetPriority(3),
	Db(bytearray(b' \x07')),
	Db(bytearray(b'$ \x01\xc0\xfe')),
	Db(bytearray(b'%\x00\x0f\x80\xff')),
	Pause(46),
	BPL262728(),
	PlaySound(sound=S058_INSERT, channel=4),
	OverwriteSolidity(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	Return()
])
