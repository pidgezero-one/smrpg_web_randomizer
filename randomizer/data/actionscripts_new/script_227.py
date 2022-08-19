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
	SetSequenceSpeed(speed=VERY_SLOW),
	SetSpriteSequence(index=10, sprite_offset=2, is_sequence=True),
	Pause(98),
	SetSequenceSpeed(speed=SLOW),
	Pause(162),
	SetSequenceSpeed(speed=NORMAL),
	Pause(162),
	SetSequenceSpeed(speed=FAST),
	Pause(214),
	SetSequenceSpeed(speed=FASTER),
	Pause(216),
	SetSequenceSpeed(speed=VERY_FAST),
	Pause(384),
	SetWalkingSpeed(speed=VERY_SLOW),
	AddZCoord1Step(),
	Return()
])
