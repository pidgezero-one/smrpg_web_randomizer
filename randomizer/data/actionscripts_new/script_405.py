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
	SequenceLoopingOn(identifier="ACTION_405_sequence_looping_on_0"),
	SetSequenceSpeed(speed=NORMAL),
	JmpIfRandom1of2(["ACTION_405_walk_1_step_southeast_20"]),
	ShiftNortheastSteps(2),
	Pause(8),
	Walk1StepSoutheast(),
	Pause(8),
	Walk1StepSouthwest(),
	Pause(8),
	Walk1StepSoutheast(),
	Pause(8),
	Walk1StepNortheast(),
	Pause(8),
	Walk1StepNorthwest(),
	Pause(8),
	ShiftSouthwestSteps(2),
	Pause(8),
	Walk1StepNorthwest(),
	Pause(8),
	Jmp(["ACTION_405_sequence_looping_on_0"]),
	Walk1StepSoutheast(identifier="ACTION_405_walk_1_step_southeast_20"),
	Pause(8),
	Walk1StepNortheast(),
	Pause(8),
	Walk1StepNorthwest(),
	Pause(8),
	ShiftSoutheastSteps(2),
	Pause(8),
	Walk1StepNortheast(),
	Pause(8),
	ShiftNorthwestSteps(2),
	Pause(8),
	ShiftSouthwestSteps(2),
	Pause(8),
	Jmp(["ACTION_405_sequence_looping_on_0"])
])
