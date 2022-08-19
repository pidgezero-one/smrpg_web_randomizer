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
	SetSequenceSpeed(speed=NORMAL, identifier="ACTION_799_set_animation_speed_0"),
	SetSpriteSequence(index=0, sprite_offset=4, is_sequence=True, mirror_sprite=True),
	Pause(66),
	ResetProperties(),
	FaceNorthwest(),
	SetSequenceSpeed(speed=VERY_FAST),
	Return()
])
