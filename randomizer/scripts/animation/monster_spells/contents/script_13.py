# Escape

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	SetAMEM16BitToAMEM(amem=0x68, source_amem=0x9A),
	JmpIfAMEM16BitNotEqualsConst(0x68, 0, ["command_0x351179"]),
	RunSubroutine(["command_0x35322b"]),
	Db(bytearray(b'\x16')),
	Db(bytearray(b'\x02')),
	RunSubroutine(["command_0x353274"], identifier="command_0x351179"),
	Db(bytearray(b'\x16')),
	Db(bytearray(b'\x02'))
])
