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
	Pause(64),
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
	Db(bytearray(b' \x07')),
	Db(bytearray(b'$\x00\x02\x00\x02')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(30),
	Db(bytearray(b'$\x80\xfbp\xfe'), identifier="ACTION_463_db_18"),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(30),
	Db(bytearray(b'$\x00\x01\x80\x03')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(30),
	Db(bytearray(b'$\x80\xfcp\xfe')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(30),
	BPL262728(),
	ResetProperties(),
	WalkToXYCoords(x=17, y=92),
	Pause(16),
	SetSpriteSequence(index=9, is_sequence=True),
	Db(bytearray(b' \x07')),
	Db(bytearray(b'$\x80\x03\x90\x01')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(30),
	Db(bytearray(b'$\x00\xff\x00\xfd')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(30),
	Db(bytearray(b'$\x80\x04\x90\x01')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(32),
	BPL262728(),
	ResetProperties(),
	WalkToXYCoords(x=23, y=91),
	SetSpriteSequence(index=9, is_sequence=True),
	Db(bytearray(b' \x07')),
	Jmp(["ACTION_463_db_18"])
])
