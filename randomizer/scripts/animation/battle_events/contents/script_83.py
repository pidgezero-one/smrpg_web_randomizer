# BE0083_SCREEN_FLASHES_WHITE

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	Db(bytearray(b'\xba\x01\x03\x00')),
	ScreenEffect(SEF0016_UNKNOWN),
	Jmp(["command_0x3a7550"])
])
