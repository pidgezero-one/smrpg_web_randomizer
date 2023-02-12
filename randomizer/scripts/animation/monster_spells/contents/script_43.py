# ChestPoison

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	SpriteSequence(sequence=6),
	PauseScriptUntilSpriteSequenceDone(),
	RunSubroutine(["command_0x3536eb"]),
	PlaySound(sound=S0000_SILENCE),
	ClearAMEM8Bit(0x6F),
	SetAMEM8BitToConst(0x6E, 3),
	SetAMEM16BitToConst(0x60, 0),
	ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35C686),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	Db(bytearray(b'\x8c')),
	ResetSpriteSequence(),
	ReturnSubroutine()
])
