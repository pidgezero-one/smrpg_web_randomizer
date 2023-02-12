# BE0061_ONLY_MARIO_IS_THERE

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a69a6"]),
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3add44"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3adaea"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3adb04"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=3, destinations=["queuestart_0x3adb1e"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=4, destinations=["queuestart_0x3adb38"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=5, destinations=["queuestart_0x3adb52"], bit_2=True, bit_4=True),
	Db(bytearray(b'\x18\x00\x80')),
	Jmp(["command_0x3a7550"])
])
