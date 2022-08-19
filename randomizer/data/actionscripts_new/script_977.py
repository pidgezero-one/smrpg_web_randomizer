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
	JmpIfBitSet(NOTE_DIRECTION, ["ACTION_977_set_sprite_sequence_3"]),
	SetSpriteSequence(index=1, is_sequence=True),
	Jmp(["ACTION_977_set_priority_4"]),
	SetSpriteSequence(index=1, is_sequence=True, mirror_sprite=True, identifier="ACTION_977_set_sprite_sequence_3"),
	SetPriority(3, identifier="ACTION_977_set_priority_4"),
	ClearBit(NOTE_DIRECTION),
	Return()
])
