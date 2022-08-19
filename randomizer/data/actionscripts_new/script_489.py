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
	SetSpriteSequence(index=6, is_mold=True, is_sequence=True),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=3, destinations=["ACTION_489_set_animation_speed_4"], identifier="ACTION_489_db_1"),
	Pause(1),
	Jmp(["ACTION_489_db_1"]),
	SetSequenceSpeed(speed=SLOW, identifier="ACTION_489_set_animation_speed_4"),
	SetSpriteSequence(index=7, looping_off=True),
	Pause(48),
	SequenceLoopingOn(),
	SetSequenceSpeed(speed=NORMAL),
	Jmp(["ACTION_405_sequence_looping_on_0"])
])
