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
	ShiftSouthwestSteps(2, identifier="ACTION_531_shift_southwest_steps_2"),
	ShiftNorthwestSteps(4),
	ShiftSouthwestSteps(1),
	ShiftNorthwestSteps(3),
	ShiftNortheastSteps(1),
	ShiftNorthwestSteps(1),
	VisibilityOff(),
	ShiftToXYCoords(x=12, y=11),
	VisibilityOn(),
	ShiftSouthwestSteps(3),
	ShiftSoutheastSteps(3),
	ShiftSouthwestSteps(4),
	ShiftSoutheastSteps(10),
	ShiftNortheastSteps(1),
	ShiftSoutheastSteps(6),
	ShiftSouthwestSteps(9),
	ShiftNorthwestSteps(6),
	ShiftSouthwestSteps(1),
	ShiftNorthwestSteps(7),
	Jmp(["ACTION_531_shift_southwest_steps_2"])
])
