# referenced by items MukuCookie

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 20, script = [
	ClearAMEM16Bit(0x60, identifier="queuestart_0x35dce9"),
	ClearAMEM8Bit(0x6E),
	ObjectQueueAtOffsetAndIndex(index=2, target_address=0x35DCD5),
	PauseScriptUntilAMEMBitsSet(0x6E, [0]),
	SetAMEM8BitToConst(0x6F, 1),
	SetOMEMMainToAMEM8Bit(omem=0x6F, amem=0x6F),
	ReturnObjectQueue()
])
