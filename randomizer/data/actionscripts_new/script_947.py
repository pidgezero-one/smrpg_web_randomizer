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
	VisibilityOff(),
	Pause(96),
	VisibilityOn(),
	SetPriority(0, identifier="ACTION_947_set_priority_3"),
	Pause(160),
	SetPriority(3),
	PlaySound(sound=S111_SLEEPING, channel=4),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True),
	Pause(8),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	Pause(8),
	SetSpriteSequence(index=2, is_mold=True, is_sequence=True),
	Pause(8),
	SetSpriteSequence(index=3, is_mold=True, is_sequence=True),
	Pause(8),
	SetSpriteSequence(index=4, is_mold=True, is_sequence=True),
	Pause(8),
	SetSpriteSequence(index=5, is_mold=True, is_sequence=True),
	Pause(24),
	SetSpriteSequence(index=4, is_mold=True, is_sequence=True),
	Pause(4),
	SetSpriteSequence(index=3, is_mold=True, is_sequence=True),
	Pause(4),
	SetSpriteSequence(index=2, is_mold=True, is_sequence=True),
	Pause(4),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	Pause(4),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	Pause(4),
	Jmp(["ACTION_947_set_priority_3"])
])
