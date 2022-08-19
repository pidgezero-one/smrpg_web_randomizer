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
	SequenceLoopingOn(),
	SetSpriteSequence(index=6, is_sequence=True, mirror_sprite=True),
	Pause(16),
	SetSequenceSpeed(speed=VERY_FAST),
	PlaySound(sound=S056_SHAKE_HEAD, channel=4),
	SetSpriteSequence(index=8, is_sequence=True, mirror_sprite=True),
	Pause(24),
	SetSequenceSpeed(speed=NORMAL),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, mirror_sprite=True),
	SequenceLoopingOff(),
	Return()
])
