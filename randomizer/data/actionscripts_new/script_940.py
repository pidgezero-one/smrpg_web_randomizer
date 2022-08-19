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
	PlaySound(sound=S121_AXEM_RANGER_TELEPORT, channel=4),
	JmpIfBitSet(TEMP_7044_0, ["ACTION_940_set_sprite_sequence_5"]),
	SetSpriteSequence(index=0, looping_off=True, is_sequence=True),
	Pause(8),
	Return(),
	SetSpriteSequence(index=1, looping_off=True, is_sequence=True, identifier="ACTION_940_set_sprite_sequence_5"),
	Pause(8),
	Return()
])
