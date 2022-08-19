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
	SetPriority(3, identifier="ACTION_168_set_priority_0"),
	FixedFCoordOn(),
	SequenceLoopingOn(identifier="ACTION_168_sequence_looping_on_2"),
	SetWalkingSpeed(speed=VERY_SLOW),
	SetSequenceSpeed(speed=VERY_FAST),
	ShiftNorthwestPixels(8),
	Pause(20),
	SetWalkingSpeed(speed=FAST),
	SetSequenceSpeed(speed=SLOW),
	JumpToHeight(height=36, silent=True),
	ShiftSoutheastPixels(8),
	Pause(25),
	Jmp(["ACTION_168_sequence_looping_on_2"])
])
