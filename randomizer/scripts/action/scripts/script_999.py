#A0999_KEEP_ORIGINAL_THRONE_ROOM_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceNorthwest(),
	SetSequenceSpeed(NORMAL),
	SequenceLoopingOn(),
	Pause(1, identifier="ACTION_999_pause_3"),
	JmpIfBitSet(TEMP_7043_0, ["ACTION_999_clear_solidity_bits_6"]),
	Jmp(["ACTION_999_pause_3"]),
	ClearSolidityBits(cant_pass_walls=True, identifier="ACTION_999_clear_solidity_bits_6"),
	SequenceLoopingOn(),
	SetSequenceSpeed(VERY_FAST),
	SetWalkingSpeed(FAST),
	JumpToHeight(height=96, silent=True),
	ShiftNorthwestSteps(2),
	SequenceLoopingOff(),
	Pause(30),
	Jmp(["ACTION_997_sequence_playback_on_0"])
])
