# behaviour_0_0x3505C6

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 20, script = [
	JmpIfTargetDisabled(["command_0x350790"]),
	VisibilityOn(),
	SetAMEM8BitTo7E5x(0x60, 0x7E002E),
	ClearAMEM8Bit(0x61),
	ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x352128),
	Db(bytearray(b'\x16')),
	Db(bytearray(b'\x15'), identifier="command_0x3505d5"),
	Pause1Frame(),
	Jmp(["command_0x3505d5"])
])
