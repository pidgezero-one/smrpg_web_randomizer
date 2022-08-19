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
	BPL262728(),
	VisibilityOff(),
	TransferToXYZF(x=11, y=18, z=4, direction=EAST),
	ClearSolidityBits(bit_4=True),
	ClearSolidityBits(cant_walk_through=True),
	Walk1StepSouthwest(),
	ShiftSouthwestPixels(8),
	VisibilityOn(),
	ShiftSouthwestPixels(8),
	SetSolidityBits(bit_4=True),
	SetSolidityBits(cant_walk_through=True),
	ClearSolidityBits(cant_pass_walls=True),
	StartLoopNTimes(6),
	PlaySound(sound=S033_JUMPING_BOUNCING_FISH, channel=4),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Walk1StepSouthwest(),
	ShiftSouthwestPixels(11),
	BPL262728(),
	Pause(2),
	EndLoop(),
	SetSolidityBits(cant_pass_walls=True),
	PlaySound(sound=S033_JUMPING_BOUNCING_FISH, channel=4),
	JumpToHeight(height=108, silent=True),
	Walk1StepSouthwest(),
	ShiftSouthwestPixels(14),
	Pause(2),
	PlaySound(sound=S033_JUMPING_BOUNCING_FISH, channel=4),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Walk1StepSouthwest(),
	ShiftSouthwestPixels(11),
	BPL262728(),
	ShiftSouthwestPixels(8),
	VisibilityOff(),
	Return()
])
