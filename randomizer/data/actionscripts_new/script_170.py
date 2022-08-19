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
	FaceSouthwest(),
	FixedFCoordOn(),
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	SetPriority(3),
	SequenceLoopingOn(),
	AddConstToVar(Z_COORD_2, 2),
	Db(bytearray(b'\x9a')),
	SetWalkingSpeed(speed=VERY_FAST),
	ShiftEastPixels(4),
	SetObjectMemoryBits(arg_1=0x0E, bits=[3]),
	VisibilityOn(),
	Return()
])
