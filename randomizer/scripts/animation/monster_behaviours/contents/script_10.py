# behaviour_10_0x350830

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 58, script = [
	SetOMEM60To072C(),
	JmpIfAMEM16BitEqualsConst(0x60, 0, ["command_0x353219"]),
	JmpIfAMEM16BitEqualsConst(0x60, 1, ["command_0x353461"]),
	JmpIfAMEM16BitEqualsConst(0x60, 2, ["command_0x353445"]),
	JmpIfAMEM16BitEqualsConst(0x60, 3, ["command_0x3505e8"]),
	JmpIfAMEM16BitEqualsConst(0x60, 4, ["command_0x3531ff"]),
	JmpIfAMEM16BitEqualsConst(0x60, 6, ["command_0x353185"]),
	JmpIfAMEM16BitEqualsConst(0x60, 7, ["command_0x3535ba"]),
	JmpIfAMEM16BitEqualsConst(0x60, 8, ["command_0x3535c8"]),
	JmpIfAMEM16BitEqualsConst(0x60, 9, ["command_0x35360b"]),
	Jmp(["command_0x3505d5"])
])
