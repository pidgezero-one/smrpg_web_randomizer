# behaviour_21_0x350A38

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 6, script = [
	VisibilityOff(identifier="command_0x350a38"),
	Db(bytearray(b'O')),
	Jmp(["command_0x3509a2"])
])
