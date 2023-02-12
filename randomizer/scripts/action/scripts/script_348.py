#A0348_SHIP_BOSS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3),
	SetSpriteSequence(index=10, is_sequence=True, looping=True),
	SequenceLoopingOn(),
	Pause(1, identifier="ACTION_348_pause_3"),
	JmpIfBitClear(TEMP_7044_7, ["ACTION_348_pause_3"]),
	ResetProperties(),
	SequenceLoopingOff(),
	Return()
])
