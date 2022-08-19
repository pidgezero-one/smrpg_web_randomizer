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
	SetPriority(3),
	SetSpriteSequence(index=10, is_sequence=True),
	SequenceLoopingOn(),
	Pause(1, identifier="ACTION_348_pause_3"),
	JmpIfBitClear(TEMP_7044_7, ["ACTION_348_pause_3"]),
	ResetProperties(),
	SequenceLoopingOff(),
	Return()
])
