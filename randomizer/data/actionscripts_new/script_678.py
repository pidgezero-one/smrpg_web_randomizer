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
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_678_set_sprite_sequence_7"]),
	SequenceLoopingOn(),
	SetSequenceSpeed(speed=FAST),
	Pause(32),
	SetSequenceSpeed(speed=SLOW),
	Return(),
	SetSpriteSequence(index=0, is_mold=True, is_sequence=True, mirror_sprite=True, identifier="ACTION_678_set_sprite_sequence_7"),
	Pause(40),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(4),
	SetSpriteSequence(index=2, is_mold=True, is_sequence=True, mirror_sprite=True),
	Pause(8),
	Jmp(["ACTION_678_set_sprite_sequence_7"])
])
