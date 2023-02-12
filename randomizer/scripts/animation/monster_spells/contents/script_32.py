# WeirdMushroom

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x35252b"]),
	SetAMEM16BitToConst(0x60, 6),
	ClearAMEM8Bit(0x6F),
	ObjectQueueAtOffsetAndIndex(index=12, target_address=0x353706),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	PlaySound(sound=S0066_RECOVER_HP),
	SetAMEM16BitToConst(0x60, 23),
	ResetSpriteSequence(),
	ClearAMEM8Bit(0x6F),
	ObjectQueueAtOffsetAndIndex(index=0, target_address=0x353706),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	ObjectQueueAtOffsetAndIndex(index=2, target_address=0x353706),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	ObjectQueueAtOffsetAndIndex(index=4, target_address=0x353706),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	ReturnSubroutine()
])
