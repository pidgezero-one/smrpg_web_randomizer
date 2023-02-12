# behaviour_24_0x350A9C

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 33, script = [
	ClearAMEM8Bit(0x60),
	SetOMEM60To072C(),
	JmpIfAMEM16BitEqualsConst(0x60, 77, ["command_0x35116a"]),
	ResetObjectMappingMemory(),
	SpriteSequence(sequence=4),
	PauseScriptUntilSpriteSequenceDone(),
	ClearAMEM8Bit(0x60),
	SetOMEM60To072C(),
	DecAMEM16BitByConst(0x60, 64),
	ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x351026),
	AttackTimerBegins(),
	Db(bytearray(b'<\x00\x08')),
	ResetTargetMappingMemory(),
	ResetObjectMappingMemory(),
	ResetSpriteSequence(),
	Jmp(["command_0x3509ae"])
])
