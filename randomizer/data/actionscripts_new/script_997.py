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
	SequencePlaybackOn(identifier="ACTION_997_sequence_playback_on_0"),
	SetSequenceSpeed(speed=VERY_FAST),
	SetWalkingSpeed(speed=FAST),
	ShiftNortheastSteps(13),
	JumpToHeight(height=21, silent=True),
	SequencePlaybackOff(),
	ShiftNortheastSteps(3),
	SetWalkingSpeed(speed=NORMAL),
	ShiftNortheastSteps(1),
	SetWalkingSpeed(speed=SLOW),
	ShiftNortheastSteps(1),
	Pause(15),
	FaceSouthwest(),
	Pause(15),
	SequencePlaybackOn(),
	SetSequenceSpeed(speed=VERY_FAST),
	SetWalkingSpeed(speed=FAST),
	ShiftSouthwestSteps(13),
	JumpToHeight(height=21, silent=True),
	SequencePlaybackOff(),
	ShiftSouthwestSteps(3),
	SetWalkingSpeed(speed=NORMAL),
	ShiftSouthwestSteps(1),
	SetWalkingSpeed(speed=SLOW),
	ShiftSouthwestSteps(1),
	Pause(15),
	FaceNortheast(),
	Pause(15),
	Jmp(["ACTION_997_sequence_playback_on_0"])
])
