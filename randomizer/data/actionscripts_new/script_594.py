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
	SetAllSpeeds(speed=FAST),
	ShiftSouthwestSteps(11),
	SetBit(TEMP_7044_5),
	ShiftSouthwestSteps(2),
	ClearBit(TEMP_7044_5),
	SetBit(TEMP_7044_7),
	Pause(2),
	Walk1StepNorthwest(),
	Walk1StepNorthwest(),
	Walk1StepSouthwest(identifier="ACTION_594_walk_1_step_southwest_9"),
	Jmp(["ACTION_594_walk_1_step_southwest_9"])
])
