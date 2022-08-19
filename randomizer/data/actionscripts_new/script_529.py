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
	ShiftSouthwestSteps(1, identifier="ACTION_529_shift_southwest_steps_2"),
	ShiftSoutheastSteps(4),
	ShiftSouthwestSteps(6),
	ShiftNorthwestSteps(1),
	ShiftSouthwestSteps(3),
	ShiftNorthwestSteps(8),
	ShiftSouthwestSteps(1),
	ShiftNorthwestSteps(6),
	ShiftSouthwestSteps(2),
	ShiftNorthwestSteps(7),
	VisibilityOff(),
	ShiftToXYCoords(x=12, y=11),
	VisibilityOn(),
	ClearSolidityBits(cant_pass_walls=True),
	ShiftSouthwestSteps(4),
	ShiftSoutheastSteps(2),
	ShiftSouthwestSteps(1),
	ShiftSoutheastSteps(4),
	ShiftSouthwestSteps(1),
	ShiftSoutheastSteps(4),
	ShiftNortheastSteps(1),
	SetSolidityBits(cant_pass_walls=True),
	ShiftSoutheastSteps(6),
	Jmp(["ACTION_529_shift_southwest_steps_2"])
])
