# PetalBlast

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x3536f8"]),
	RunSubroutine(["command_0x35252b"]),
	RunSubroutine(["command_0x3536eb"]),
	PlaySound(sound=S0188_PETAL_BLAST),
	ClearAMEM8Bit(0x6F),
	SetAMEM16BitToConst(0x60, 26),
	ObjectQueueAtOffsetAndIndex(index=6, target_address=0x353706),
	ObjectQueueAtOffsetAndIndex(index=8, target_address=0x353706),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	ObjectQueueAtOffsetAndIndex(index=4, target_address=0x353706),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	PlaySound(sound=S0115_TRANSFORM),
	Db(bytearray(b'\x8c')),
	RunSubroutine(["command_0x3536ff"]),
	ReturnSubroutine()
])
