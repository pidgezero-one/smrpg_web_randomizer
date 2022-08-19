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
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	SetSpriteSequence(index=2, looping_off=True, is_sequence=True),
	IncPaletteRowBy(1),
	SetPriority(3),
	SetWalkingSpeed(speed=VERY_FAST),
	ShiftSouthwestPixels(10),
	ObjectMemorySetBit(arg_1=0x0D, bits=[6]),
	SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetWalkingSpeed(speed=NORMAL),
	Return()
])
