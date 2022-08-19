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
	Db(bytearray(b' \x03')),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\xb4\x00 \x00\x01\x00\x00\x80\xfe\x80')),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00v\x00\x1a\x00\x01\x00\x00\x80\xfe\x80")),
	Pause(176),
	SetVarToConst(PRIMARY_TEMP_700C, 65120),
	Db(bytearray(b'5\x00\x06')),
	Db(bytearray(b'5\x01\x06')),
	Pause(240),
	SetVarToConst(PRIMARY_TEMP_700C, 64800),
	Db(bytearray(b'5\x00\x06')),
	Db(bytearray(b'5\x01\x06')),
	Pause(120),
	SetVarToConst(PRIMARY_TEMP_700C, 64512),
	Db(bytearray(b'5\x00\x06')),
	Db(bytearray(b'5\x01\x06')),
	Pause(90),
	SetVarToConst(PRIMARY_TEMP_700C, 64000),
	Db(bytearray(b'5\x00\x06')),
	Db(bytearray(b'5\x01\x06')),
	Pause(60),
	SetVarToConst(PRIMARY_TEMP_700C, 63744),
	Db(bytearray(b'5\x00\x06')),
	Db(bytearray(b'5\x01\x06')),
	Pause(30),
	SetVarToConst(PRIMARY_TEMP_700C, 63488),
	Db(bytearray(b'5\x00\x06')),
	Db(bytearray(b'5\x01\x06')),
	Pause(212),
	SetVarToConst(PRIMARY_TEMP_700C, 64256),
	Db(bytearray(b'5\x00\x06')),
	Db(bytearray(b'5\x01\x06')),
	SetWalkingSpeed(speed=NORMAL),
	ShiftZUpPixels(8),
	SetWalkingSpeed(speed=FAST),
	AddZCoord1Step(),
	SetWalkingSpeed(speed=VERY_FAST),
	ShiftZUpSteps(2),
	SetBit(TEMP_7043_3),
	ShiftZUpSteps(2),
	SetWalkingSpeed(speed=FASTEST),
	ShiftZUpSteps(8),
	BPL262728(),
	Return()
])
