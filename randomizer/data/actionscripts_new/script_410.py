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
	SetPriority(3),
	SetSequenceSpeed(speed=NORMAL),
	SequenceLoopingOn(),
	Db(bytearray(b' \x07')),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00@\x00\x10\x00\x01\x00\x00\x00\x02\x80')),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\xc0\x00\x18\x00\x01\x00\x00\x00\x02\x80")),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x80\x00\x10\x00\x01\x00\x00\x00\x04\x80')),
	Pause(1, identifier="ACTION_410_pause_7"),
	Jmp(["ACTION_410_pause_7"])
])
