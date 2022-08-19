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
	Pause(10, identifier="ACTION_800_pause_0"),
	SetSpriteSequence(index=0, sprite_offset=6, is_sequence=True, mirror_sprite=True),
	SetWalkingSpeed(speed=VERY_FAST),
	ShiftNortheastPixels(1),
	StartLoopNTimes(29),
	ShiftSouthwestPixels(2),
	ShiftNortheastPixels(2),
	EndLoop(),
	ShiftSouthwestPixels(1),
	SetWalkingSpeed(speed=FAST),
	Pause(16),
	ResetProperties(),
	FaceNorthwest(),
	Return()
])
