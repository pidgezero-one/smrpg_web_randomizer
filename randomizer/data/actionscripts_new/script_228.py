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
	Db(bytearray(b' \x07')),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00<\x00\x1c\x00\x01\x00\x00\x80\xfe\x80')),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\xfc\x00\x15\x00\x01\x00\x00\x80\xfe\x80")),
	Pause(150),
	SetVarToConst(PRIMARY_TEMP_700C, 65024),
	Db(bytearray(b'5\x00\x06')),
	Db(bytearray(b'5\x01\x06')),
	SetVarToConst(PRIMARY_TEMP_700C, 257),
	Db(bytearray(b'5\x00\x04')),
	Db(bytearray(b'5\x01\x04')),
	Db(bytearray(b'% \x00\x00\x00')),
	Pause(180),
	SetVarToConst(PRIMARY_TEMP_700C, 258),
	Db(bytearray(b'5\x00\x04')),
	Db(bytearray(b'5\x01\x04')),
	SetVarToConst(PRIMARY_TEMP_700C, 64768),
	Db(bytearray(b'5\x00\x06')),
	Db(bytearray(b'5\x01\x06')),
	Db(bytearray(b'%\x00\x00\x00\x00')),
	Pause(120),
	SetWalkingSpeed(speed=FASTEST),
	ShiftZUpSteps(20),
	Return()
])
