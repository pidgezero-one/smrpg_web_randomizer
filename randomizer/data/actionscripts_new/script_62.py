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
	ObjectMemorySetBit(arg_1=0x0B, bits=[3], identifier="ACTION_62_object_memory_set_bit_0"),
	SetSequenceSpeed(speed=FAST),
	ShiftSoutheastSteps(2),
	ShiftSouthwestSteps(2),
	ShiftNorthwestSteps(2),
	ShiftNortheastSteps(2),
	Jmp(["ACTION_62_object_memory_set_bit_0"])
])
