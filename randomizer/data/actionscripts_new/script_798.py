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
	JmpIfRandom2of3(['ACTION_799_set_animation_speed_0', 'ACTION_800_pause_0']),
	SetSpriteSequence(index=2, sprite_offset=3, is_sequence=True),
	JumpToHeight(height=80, silent=True),
	Pause(1, identifier="ACTION_798_pause_3"),
	JmpIfMarioInAir(["ACTION_798_pause_3"]),
	JumpToHeight(height=80, silent=True),
	Pause(1, identifier="ACTION_798_pause_6"),
	JmpIfMarioInAir(["ACTION_798_pause_6"]),
	JumpToHeight(height=80, silent=True),
	Pause(1, identifier="ACTION_798_pause_9"),
	JmpIfMarioInAir(["ACTION_798_pause_9"]),
	ResetProperties(),
	FaceNorthwest(),
	Return()
])
