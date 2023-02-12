# behaviour_29_0x350BF3

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 6, script = [
	VisibilityOff(identifier="command_0x350bf3"),
	Db(bytearray(b'O')),
	Jmp(["command_0x350afa"])
])
