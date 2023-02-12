#A0934_CORKPEDITE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequencePlaybackOff(identifier="ACTION_934_sequence_playback_off_0"),
	SequenceLoopingOff(),
	Pause(2, identifier="ACTION_934_pause_2"),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_934_pause_2"]),
	SequenceLoopingOn(),
	FloatingOff(),
	SetWalkingSpeed(FAST),
	ShiftZUpPixels(16),
	SetWalkingSpeed(NORMAL),
	ShiftZUpPixels(8),
	SetWalkingSpeed(SLOW),
	ShiftZUpPixels(4),
	SetWalkingSpeed(VERY_SLOW),
	ShiftZUpPixels(2),
	Pause(12),
	FloatingOn(),
	ClearBit(TEMP_7043_0),
	Jmp(["ACTION_934_sequence_playback_off_0"])
])
