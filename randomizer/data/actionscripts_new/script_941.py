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
	SequenceLoopingOn(),
	VisibilityOff(),
	SetPriority(3),
	Db(bytearray(b' \x04')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\x00\x00\x00\x02\x80')),
	Pause(500),
	StartLoopNTimes(9),
	VisibilityOn(),
	Pause(4),
	VisibilityOff(),
	Pause(4),
	EndLoop(),
	PlaySound(sound=S119_CZAR_DRAGON_ROAR, channel=4),
	StartLoopNTimes(9),
	VisibilityOn(),
	Pause(2),
	VisibilityOff(),
	Pause(2),
	EndLoop(),
	StartLoopNTimes(9),
	VisibilityOn(),
	Pause(1),
	VisibilityOff(),
	Pause(1),
	EndLoop(),
	VisibilityOn(),
	Jmp(["ACTION_936_pause_16"])
])
