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
	SequenceLoopingOn(identifier="ACTION_699_sequence_looping_on_0"),
	SetWalkingSpeed(speed=SLOW),
	Walk1StepNortheast(),
	ShiftNorthwestSteps(3),
	Walk1StepSouthwest(),
	ShiftSoutheastSteps(3),
	Jmp(["ACTION_699_sequence_looping_on_0"])
])
