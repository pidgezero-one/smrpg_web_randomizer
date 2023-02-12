# BreakerBeam

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x3536f8"]),
	RunSubroutine(["command_0x35252b"]),
	SpriteSequence(sequence=3),
	PauseScriptUntilSpriteSequenceDone(),
	ClearAMEM8Bit(0x6F),
	SetAMEM16BitToConst(0x60, 28),
	ObjectQueueAtOffsetAndIndex(index=6, target_address=0x353706),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	RunSubroutine(["command_0x3536ff"]),
	ReturnSubroutine()
])
