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
	ShiftToXYCoords(x=15, y=35),
	ShiftSouthPixels(3),
	ShiftNorthwestPixels(11),
	ShiftSouthwestPixels(6),
	Db(bytearray(b'\xfd\x12')),
	VisibilityOn(),
	PlaySound(sound=S073_THWOMP_STOMP, channel=4),
	SequenceLoopingOn(),
	ObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	ShiftSouthwestSteps(10),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	VisibilityOff(),
	Return()
])
