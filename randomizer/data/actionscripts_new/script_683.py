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
	SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
	SetSolidityBits(cant_walk_through=True),
	SetSolidityBits(bit_4=True),
	SetSequenceSpeed(speed=NORMAL),
	FaceSouthwest(),
	SetWalkingSpeed(speed=SLOW),
	ShiftSouthwestSteps(20),
	FaceNortheast(),
	Pause(60),
	Jmp(["ACTION_676_set_object_memory_bits_0"])
])
