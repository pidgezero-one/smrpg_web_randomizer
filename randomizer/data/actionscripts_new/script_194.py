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
	SetSpriteSequence(index=0, is_sequence=True, mirror_sprite=True, identifier="ACTION_194_set_sprite_sequence_0"),
	Pause(5, identifier="ACTION_194_pause_1"),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=4, destinations=["ACTION_194_set_sprite_sequence_4"]),
	Jmp(["ACTION_194_pause_1"]),
	SetSpriteSequence(index=3, is_sequence=True, mirror_sprite=True, identifier="ACTION_194_set_sprite_sequence_4"),
	Pause(5, identifier="ACTION_194_pause_5"),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=4, destinations=["ACTION_194_pause_5"]),
	Jmp(["ACTION_194_set_sprite_sequence_0"])
])
