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
	SetWalkingSpeed(speed=SLOW),
	SetSequenceSpeed(speed=FASTER),
	ShiftSouthwestSteps(1, identifier="ACTION_528_shift_southwest_steps_2"),
	ShiftSoutheastSteps(12),
	ShiftSouthwestSteps(3),
	ShiftSoutheastSteps(1),
	ShiftSouthwestSteps(4),
	ShiftNorthwestSteps(1),
	ShiftSouthwestSteps(2),
	ShiftNorthwestSteps(6),
	ShiftSouthwestSteps(1),
	ShiftNorthwestSteps(7),
	ShiftSouthwestSteps(2),
	ShiftNorthwestSteps(8),
	VisibilityOff(),
	ShiftToXYCoords(x=12, y=11),
	VisibilityOn(),
	ShiftSouthwestSteps(2),
	ShiftSoutheastSteps(1),
	ShiftSouthwestSteps(1),
	ShiftSoutheastSteps(1),
	ShiftSouthwestSteps(1),
	ShiftSoutheastSteps(3),
	ShiftSouthwestSteps(1),
	ShiftSoutheastSteps(2),
	Jmp(["ACTION_528_shift_southwest_steps_2"])
])
