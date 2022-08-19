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
	VisibilityOn(),
	JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	SetSolidityBits(cant_pass_walls=True),
	StartLoopNTimes(1),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Walk1StepSouthwest(),
	ShiftSouthwestPixels(14),
	Pause(2),
	BPL262728(),
	EndLoop(),
	ClearSolidityBits(cant_pass_walls=True),
	JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	Pause(20),
	VisibilityOff(),
	ClearSolidityBits(bit_4=True),
	ClearSolidityBits(cant_walk_through=True),
	Return()
])
