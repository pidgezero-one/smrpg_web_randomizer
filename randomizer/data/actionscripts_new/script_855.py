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
	OverwriteSolidity(),
	SetWalkingSpeed(speed=SLOW),
	WalkToXYCoords(x=24, y=18),
	PlaySound(sound=S031_SPINNING_FLOWER, channel=4),
	StartLoopNTimes(1),
	FaceSouthwest(),
	Pause(3),
	FaceWest(),
	Pause(3),
	FaceNorthwest(),
	Pause(3),
	FaceNorth(),
	Pause(3),
	FaceNortheast(),
	Pause(3),
	FaceEast(),
	Pause(3),
	FaceSoutheast(),
	Pause(3),
	FaceSouth(),
	Pause(3),
	EndLoop(),
	SetSpriteSequence(index=1, sprite_offset=3, is_sequence=True),
	FaceSouth(),
	PlaySound(sound=S022_CLOSE_DOOR, channel=4),
	Return()
])
