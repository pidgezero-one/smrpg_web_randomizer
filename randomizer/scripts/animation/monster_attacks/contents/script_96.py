# GetTough

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x357b73"]),
	SetOMEM60To072C(),
	DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
	SpriteSequence(sequence=4),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=40),
	PlaySound(sound=S0037_MONSTER_ITEM_TOSS),
	SetAMEM16BitToConst(0x60, 16),
	ClearAMEM8Bit(0x6F),
	ObjectQueueAtOffsetAndIndex(index=6, target_address=0x353706),
	PauseScriptUntilSpriteSequenceDone(),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	RunSubroutine(["command_0x3577f2"]),
	RunSubroutine(["command_0x3523c4"]),
	ReturnSubroutine()
])
