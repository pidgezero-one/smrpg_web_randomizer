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
	SetPriority(3, identifier="ACTION_604_set_priority_0"),
	SetAllSpeeds(speed=NORMAL),
	Walk1StepSouthwest(),
	Walk1StepNorthwest(),
	Pause(20),
	SetAllSpeeds(speed=FAST),
	Walk1StepEast(),
	Pause(13),
	Jmp(["ACTION_604_set_priority_0"])
])
