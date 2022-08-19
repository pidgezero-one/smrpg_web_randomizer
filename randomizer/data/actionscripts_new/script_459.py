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
	SetWalkingSpeed(speed=SLOW),
	ShadowOff(),
	SequenceLoopingOn(),
	ShiftSouthwestSteps(4),
	ShiftSouthwestPixels(10),
	SetSpriteSequence(index=9, is_sequence=True),
	FloatingOn(),
	JumpToHeight(0),
	ShadowOn(),
	Pause(24),
	SetWalkingSpeed(speed=NORMAL),
	ResetProperties(),
	WalkToXYCoords(x=22, y=85),
	SetSpriteSequence(index=9, is_sequence=True, mirror_sprite=True),
	Db(bytearray(b' \x07')),
	Db(bytearray(b'$\x00\xff\xb0\x00'), identifier="ACTION_459_db_15"),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(30),
	Db(bytearray(b'$\x80\xfe\x00\xff')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(30),
	Db(bytearray(b'$\x80\x01\x00\x01')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(30),
	Db(bytearray(b'$\x00\x01P\xff')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(30),
	Jmp(["ACTION_459_db_15"])
])
