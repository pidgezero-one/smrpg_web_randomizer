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
	ObjectMemorySetBit(arg_1=0x0B, bits=[3], identifier="ACTION_432_object_memory_set_bit_0"),
	SetWalkingSpeed(speed=SLOW),
	SetPriority(2),
	StartLoopNTimes(3),
	ShiftFDirectionSteps(3),
	TurnClockwise45DegreesNTimes(2),
	Pause(6),
	TurnClockwise45DegreesNTimes(2),
	Pause(6),
	TurnClockwise45DegreesNTimes(2),
	Pause(6),
	TurnClockwise45DegreesNTimes(2),
	Pause(6),
	TurnClockwise45DegreesNTimes(2),
	EndLoop(),
	TurnClockwise45DegreesNTimes(2),
	StartLoopNTimes(3),
	ShiftFDirectionSteps(3),
	TurnClockwise45DegreesNTimes(6),
	Pause(6),
	TurnClockwise45DegreesNTimes(6),
	Pause(6),
	TurnClockwise45DegreesNTimes(6),
	Pause(6),
	TurnClockwise45DegreesNTimes(6),
	Pause(6),
	TurnClockwise45DegreesNTimes(6),
	EndLoop(),
	TurnClockwise45DegreesNTimes(6),
	Jmp(["ACTION_432_object_memory_set_bit_0"])
])
