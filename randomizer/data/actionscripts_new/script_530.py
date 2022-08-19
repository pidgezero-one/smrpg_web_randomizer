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
	ShiftNorthwestSteps(10, identifier="ACTION_530_shift_northwest_steps_2"),
	ShiftSouthwestSteps(2),
	ShiftNorthwestSteps(6),
	ShiftSouthwestSteps(1),
	ShiftNorthwestSteps(5),
	VisibilityOff(),
	ShiftToXYCoords(x=12, y=11),
	VisibilityOn(),
	ShiftSouthwestSteps(4),
	ShiftSoutheastSteps(6),
	ShiftSouthwestSteps(3),
	ShiftSoutheastSteps(8),
	ShiftNortheastSteps(1),
	ShiftSoutheastSteps(4),
	ShiftSouthwestSteps(1),
	ShiftSoutheastSteps(1),
	ShiftSouthwestSteps(1),
	ShiftSoutheastSteps(1),
	ShiftSouthwestSteps(5),
	ShiftNorthwestSteps(1),
	ShiftSouthwestSteps(2),
	Jmp(["ACTION_530_shift_northwest_steps_2"])
])
