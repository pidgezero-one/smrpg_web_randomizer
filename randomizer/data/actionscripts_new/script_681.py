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
	SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, identifier="ACTION_681_set_sprite_sequence_0"),
	JumpToHeight(height=108, silent=True),
	Pause(1, identifier="ACTION_681_pause_2"),
	JmpIfBitSet(TEMP_7043_1, ["ACTION_681_ret_7"]),
	JmpIfMarioInAir(["ACTION_681_pause_2"]),
	Pause(30),
	Jmp(["ACTION_681_set_sprite_sequence_0"]),
	Return(identifier="ACTION_681_ret_7")
])
