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
	PlaySound(sound=S027_FOUND_AN_ITEM, channel=4),
	ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	JumpToHeight(height=160, silent=True),
	Pause(13),
	FloatingOff(),
	StartLoopNTimes(7),
	VisibilityOff(),
	Pause(2),
	VisibilityOn(),
	Pause(2),
	EndLoop(),
	VisibilityOff(),
	Return()
])
