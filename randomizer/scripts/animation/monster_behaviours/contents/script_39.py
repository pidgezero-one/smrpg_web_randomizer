# behaviour_39_0x350D9D

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 6, script = [
	VisibilityOff(identifier="command_0x350d9d"),
	Db(bytearray(b'O')),
	Jmp(["command_0x350d25"])
])
