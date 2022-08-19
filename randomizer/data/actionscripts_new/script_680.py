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
	SetSequenceSpeed(speed=SLOW),
	Pause(8, identifier="ACTION_680_pause_2"),
	SetSpriteSequence(index=21, sprite_offset=2, is_mold=True, is_sequence=True),
	Pause(8),
	ResetProperties(),
	Pause(1, identifier="ACTION_680_pause_6"),
	JmpIfBitSet(TEMP_7043_1, ["ACTION_680_ret_11"]),
	JmpIfMarioInAir(["ACTION_680_pause_6"]),
	Pause(30),
	Jmp(["ACTION_680_pause_2"]),
	Return(identifier="ACTION_680_ret_11")
])
