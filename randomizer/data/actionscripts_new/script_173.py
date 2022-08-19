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
	TransferTo70167018701A(),
	ShadowOff(),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	StartLoopNTimes(3),
	VisibilityOff(),
	Pause(1),
	VisibilityOn(),
	Pause(1),
	EndLoop(),
	Jmp(["ACTION_163_set_700C_to_current_level_0"])
])
