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
	Db(bytearray(b' \x04')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x06\x00\x01\x00\x00\x00\x04\x80')),
	SetSequenceSpeed(speed=FAST, identifier="ACTION_533_set_animation_speed_2"),
	SetWalkingSpeed(speed=NORMAL),
	ShiftNortheastSteps(1),
	SetSequenceSpeed(speed=NORMAL),
	SetWalkingSpeed(speed=SLOW),
	ShiftNortheastSteps(1),
	SetSequenceSpeed(speed=FAST),
	SetWalkingSpeed(speed=NORMAL),
	ShiftSoutheastSteps(1),
	SetSequenceSpeed(speed=NORMAL),
	SetWalkingSpeed(speed=SLOW),
	ShiftSoutheastSteps(1),
	SetSequenceSpeed(speed=FAST),
	SetWalkingSpeed(speed=NORMAL),
	ShiftSouthwestSteps(1),
	SetSequenceSpeed(speed=NORMAL),
	SetWalkingSpeed(speed=SLOW),
	ShiftSouthwestSteps(1),
	SetSequenceSpeed(speed=FAST),
	SetWalkingSpeed(speed=NORMAL),
	ShiftNorthwestSteps(1),
	SetSequenceSpeed(speed=NORMAL),
	SetWalkingSpeed(speed=SLOW),
	ShiftNorthwestSteps(1),
	Jmp(["ACTION_533_set_animation_speed_2"])
])
