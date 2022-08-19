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
	SequencePlaybackOff(identifier="ACTION_95_sequence_playback_off_0"),
	FaceNorthwest(),
	FixedFCoordOn(),
	SetWalkingSpeed(speed=SLOW),
	Pause(120),
	Pause(60),
	StartLoopNTimes(1),
	ShiftEastPixels(1),
	Pause(1),
	ShiftWestPixels(1),
	Pause(1),
	EndLoop(),
	Pause(120),
	Jmp(["ACTION_95_sequence_playback_off_0"])
])
