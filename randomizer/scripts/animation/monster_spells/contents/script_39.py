# BigBang

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x35252b"]),
	RunSubroutine(["command_0x3536eb"]),
	SetAMEM16BitToConst(0x60, 11),
	ClearAMEM8Bit(0x6F),
	ObjectQueueAtOffsetAndIndex(index=10, target_address=0x353706),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	VisibilityOff(),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	Db(bytearray(b'\x8c')),
	ReturnSubroutine()
])
