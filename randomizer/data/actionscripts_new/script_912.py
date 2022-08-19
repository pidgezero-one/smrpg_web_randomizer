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
	FloatingOff(),
	VisibilityOff(),
	SetSpriteSequence(index=4, is_sequence=True),
	Pause(9),
	VisibilityOn(),
	Pause(1, identifier="ACTION_912_pause_5"),
	JmpIfBitClear(MIMIC_3_CLEARED, ["ACTION_912_pause_5"]),
	JmpIfBitSet(RUN_AWAY, ["ACTION_912_pause_10"]),
	SetSpriteSequence(index=6, is_sequence=True),
	Pause(18),
	Pause(6, identifier="ACTION_912_pause_10"),
	VisibilityOff(),
	Return()
])
