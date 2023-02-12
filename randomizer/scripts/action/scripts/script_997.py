#A0997_KEEP_ORIGINAL_THRONE_ROOM_RUNNING_GOOMBAS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequencePlaybackOn(identifier="ACTION_997_sequence_playback_on_0"),
	SetSequenceSpeed(VERY_FAST),
	SetWalkingSpeed(FAST),
	ShiftNortheastSteps(13),
	JumpToHeight(height=21, silent=True),
	SequencePlaybackOff(),
	ShiftNortheastSteps(3),
	SetWalkingSpeed(NORMAL),
	ShiftNortheastSteps(1),
	SetWalkingSpeed(SLOW),
	ShiftNortheastSteps(1),
	Pause(15),
	FaceSouthwest(),
	Pause(15),
	SequencePlaybackOn(),
	SetSequenceSpeed(VERY_FAST),
	SetWalkingSpeed(FAST),
	ShiftSouthwestSteps(13),
	JumpToHeight(height=21, silent=True),
	SequencePlaybackOff(),
	ShiftSouthwestSteps(3),
	SetWalkingSpeed(NORMAL),
	ShiftSouthwestSteps(1),
	SetWalkingSpeed(SLOW),
	ShiftSouthwestSteps(1),
	Pause(15),
	FaceNortheast(),
	Pause(15),
	Jmp(["ACTION_997_sequence_playback_on_0"])
])
