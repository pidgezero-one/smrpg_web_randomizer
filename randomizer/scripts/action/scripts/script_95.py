#A0095_PLAYER_GAME_START

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequencePlaybackOff(identifier="ACTION_95_sequence_playback_off_0"),
	FaceNorthwest(),
	FixedFCoordOn(),
	SetWalkingSpeed(SLOW),
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
