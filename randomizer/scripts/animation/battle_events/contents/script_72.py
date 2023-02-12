# BE0072_JINX_USES_QUICKSILVER

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ade50"], bit_2=True, bit_4=True),
	Db(bytearray(b'\x18\x00\x80')),
	Jmp(["command_0x3a7550"])
])
