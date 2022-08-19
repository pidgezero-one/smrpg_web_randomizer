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
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	Db(bytearray(b'\xfd\xf2')),
	VisibilityOff(),
	ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	EndAll(),
	SetPaletteRow(253),
	RemoveFromLevel(DUMMY_0X06, R001_____BLUE_BG_NOTHING_THERE),
	SummonObjectAt70A8ToCurrentLevel(),
	EndAll(),
	Pause(64),
	BPL262728(),
	VisibilityOff(),
	EndAll(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	Db(bytearray(b'\xfd\xf2')),
	VisibilityOff(),
	ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
])
