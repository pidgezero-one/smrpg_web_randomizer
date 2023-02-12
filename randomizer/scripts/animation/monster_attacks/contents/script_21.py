# PhysicalAttack27

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x357b73"]),
	RunSubroutine(["command_0x353148"]),
	PlaySound(sound=S0125_SPIKE_SHOT),
	SetAMEM16BitToConst(0x60, 2),
	ClearAMEM8Bit(0x6F),
	ObjectQueueAtOffsetAndIndex(index=16, target_address=0x353706),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	RunSubroutine(["command_0x3577f2"]),
	RunSubroutine(["command_0x3523c4"]),
	ReturnSubroutine()
])
