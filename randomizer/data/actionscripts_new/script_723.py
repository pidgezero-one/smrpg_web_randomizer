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
	FaceSouthwest(),
	FixedFCoordOn(),
	SequencePlaybackOn(),
	SequenceLoopingOn(),
	ShiftNortheastPixels(3),
	FaceSouthwest(identifier="ACTION_723_face_southwest_5"),
	FixedFCoordOn(),
	StartLoopNTimes(3),
	ShiftWestPixels(1),
	Pause(1),
	ShiftEastPixels(1),
	Pause(1),
	EndLoop(),
	SetWalkingSpeed(speed=SLOW),
	ShiftNortheastPixels(8),
	Pause(80),
	JmpIfRandom1of2(["ACTION_723_face_southwest_23"]),
	FixedFCoordOff(),
	FaceNorthwest(),
	JumpToHeight(40),
	Pause(16),
	JumpToHeight(40),
	Pause(64),
	FaceSouthwest(identifier="ACTION_723_face_southwest_23"),
	FixedFCoordOn(),
	ShiftSouthwestPixels(8),
	SetWalkingSpeed(speed=NORMAL),
	Jmp(["ACTION_723_face_southwest_5"])
])
