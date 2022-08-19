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
	FaceSouth(),
	Pause(2),
	FaceSouthwest(),
	Pause(2),
	FaceWest(),
	Pause(2),
	FaceNorthwest(),
	Pause(2),
	FaceNorth(),
	Pause(2),
	FaceNortheast(),
	Pause(2),
	FaceEast(),
	Pause(2),
	FaceSoutheast(),
	Pause(6),
	SetSpriteSequence(index=10, sprite_offset=2, looping_off=True, is_sequence=True),
	Pause(64),
	SetSpriteSequence(index=12, is_mold=True, is_sequence=True),
	FaceSouth(),
	ResetProperties(),
	Return()
])
