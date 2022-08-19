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
	Pause(90),
	SetWalkingSpeed(speed=SLOW),
	SetSequenceSpeed(speed=FAST),
	ShiftSouthwestSteps(3, identifier="ACTION_983_shift_southwest_steps_3"),
	Pause(30),
	SetSequenceSpeed(speed=NORMAL),
	SetSpriteSequence(index=3, is_sequence=True),
	Pause(40),
	ResetProperties(),
	SetSequenceSpeed(speed=FAST),
	ShiftNortheastSteps(3),
	Pause(90),
	Jmp(["ACTION_983_shift_southwest_steps_3"])
])
