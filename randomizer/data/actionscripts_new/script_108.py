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
	StartLoopNTimes(2),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Walk1StepSouthwest(),
	ShiftSouthwestPixels(11),
	BPL262728(),
	Pause(2),
	EndLoop(),
	SetSolidityBits(cant_pass_walls=True),
	JumpToHeight(height=108, silent=True),
	Walk1StepSouthwest(),
	ShiftSouthwestPixels(14),
	Pause(2),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Walk1StepSouthwest(),
	ShiftSouthwestPixels(11),
	BPL262728(),
	ShiftSouthwestPixels(8),
	ClearSolidityBits(cant_pass_walls=True),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	VisibilityOff(),
	Return()
])
