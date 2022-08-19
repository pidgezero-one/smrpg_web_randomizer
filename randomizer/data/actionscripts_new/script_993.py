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
	SetSequenceSpeed(speed=FAST),
	SetWalkingSpeed(speed=SLOW),
	ShiftNortheastSteps(5, identifier="ACTION_993_shift_northeast_steps_2"),
	FaceSouthwest(),
	FixedFCoordOn(),
	SetSequenceSpeed(speed=NORMAL),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftNortheastSteps(2),
	FixedFCoordOff(),
	FaceNortheast(),
	SetSequenceSpeed(speed=FAST),
	SetWalkingSpeed(speed=SLOW),
	ShiftNortheastSteps(3),
	SetSequenceSpeed(speed=VERY_FAST),
	SetWalkingSpeed(speed=NORMAL),
	ShiftNortheastSteps(1),
	ShiftSoutheastSteps(1),
	ShiftSouthwestSteps(1),
	SetSequenceSpeed(speed=FAST),
	SetWalkingSpeed(speed=SLOW),
	ShiftSouthwestSteps(10),
	ShiftNorthwestSteps(1),
	Jmp(["ACTION_993_shift_northeast_steps_2"])
])
