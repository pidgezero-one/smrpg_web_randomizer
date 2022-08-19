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
	SequenceLoopingOn(identifier="ACTION_180_sequence_looping_on_0"),
	ClearSolidityBits(cant_pass_walls=True),
	SetSequenceSpeed(speed=FAST),
	ShiftSoutheastSteps(6),
	Pause(24),
	FaceSouthwest(),
	Pause(24),
	FaceNortheast(),
	Pause(24),
	FaceSoutheast(),
	Pause(24),
	ShiftSouthwestSteps(2),
	ShiftNorthwestSteps(8),
	Walk1StepNortheast(),
	ShiftNorthwestSteps(8),
	ShiftSouthwestSteps(3),
	Pause(24),
	FaceNorthwest(),
	Pause(24),
	FaceSoutheast(),
	Pause(24),
	ShiftNortheastSteps(4),
	ShiftSoutheastSteps(10),
	Jmp(["ACTION_180_sequence_looping_on_0"])
])
