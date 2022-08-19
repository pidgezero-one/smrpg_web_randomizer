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
	ShadowOff(),
	VisibilityOff(),
	Pause(128),
	VisibilityOn(),
	SetWalkingSpeed(speed=SLOW),
	SequenceLoopingOn(),
	ShiftSouthwestSteps(6),
	ShiftSouthwestPixels(10),
	SetSpriteSequence(index=9, is_sequence=True),
	FloatingOn(),
	JumpToHeight(0),
	ShadowOn(),
	Pause(24),
	SetWalkingSpeed(speed=NORMAL),
	SetSpriteSequence(index=9, is_sequence=True, mirror_sprite=True),
	Db(bytearray(b' \x07')),
	StartLoopNTimes(2),
	Db(bytearray(b'$\xc0\x00\xa0\x00')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(30),
	EndLoop(),
	StartLoopNTimes(1, identifier="ACTION_481_start_loop_n_times_21"),
	Db(bytearray(b'$\xa0\xff@\x00')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(30),
	EndLoop(),
	StartLoopNTimes(1),
	Db(bytearray(b'$\xa0\xff\xc0\xff')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(30),
	EndLoop(),
	StartLoopNTimes(1),
	Db(bytearray(b'$`\x00\xc0\xff')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(30),
	EndLoop(),
	StartLoopNTimes(1),
	Db(bytearray(b'$`\x00@\x00')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(30),
	EndLoop(),
	Jmp(["ACTION_481_start_loop_n_times_21"])
])
