# MegaRecover

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x35252b"]),
	PlaySound(sound=S0066_RECOVER_HP),
	SetAMEM16BitToConst(0x60, 23),
	ClearAMEM8Bit(0x6F),
	ObjectQueueAtOffsetAndIndex(index=6, target_address=0x353706),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	ObjectQueueAtOffsetAndIndex(index=8, target_address=0x353706),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	ObjectQueueAtOffsetAndIndex(index=10, target_address=0x353706),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	ReturnSubroutine()
])
