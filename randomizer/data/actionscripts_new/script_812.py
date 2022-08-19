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
	SetSequenceSpeed(speed=SLOW),
	SetWalkingSpeed(speed=VERY_SLOW),
	Db(bytearray(b' \x04')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
	SetVarToConst(PRIMARY_TEMP_700C, 2, identifier="ACTION_812_set_14"),
	ShiftZ20Steps(),
	TurnClockwise45DegreesNTimes(6),
	Pause(4),
	TurnClockwise45DegreesNTimes(6),
	Pause(4),
	TurnClockwise45DegreesNTimes(6),
	JmpIfRandom1of2(["ACTION_812_pause_23"]),
	Pause(30),
	Pause(10, identifier="ACTION_812_pause_23"),
	Jmp(["ACTION_812_set_14"])
])
