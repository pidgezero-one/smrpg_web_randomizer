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
	SetPriority(3, identifier="ACTION_606_set_priority_0"),
	ShiftFDirectionSteps(3),
	SetAllSpeeds(speed=FAST),
	ShiftZDownPixels(8),
	AddZCoord1Step(),
	DecZCoord1Step(),
	ShiftZUpPixels(8),
	SetAllSpeeds(speed=NORMAL),
	TurnClockwise45DegreesNTimes(4),
	ShiftFDirectionSteps(3),
	TurnClockwise45DegreesNTimes(4),
	Jmp(["ACTION_606_set_priority_0"])
])
