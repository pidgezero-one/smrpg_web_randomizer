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
	VisibilityOn(),
	SetWalkingSpeed(speed=FAST),
	SetSequenceSpeed(speed=FASTER),
	SequenceLoopingOn(),
	ResetProperties(),
	ShiftNortheastSteps(5),
	Pause(16),
	SetWalkingSpeed(speed=SLOW),
	SetSequenceSpeed(speed=NORMAL),
	ShiftNorthwestPixels(8),
	ShiftSouthwestSteps(3, identifier="ACTION_852_shift_southwest_steps_10"),
	Walk1StepSoutheast(),
	ShiftNortheastSteps(3),
	Walk1StepNorthwest(),
	Jmp(["ACTION_852_shift_southwest_steps_10"])
])
