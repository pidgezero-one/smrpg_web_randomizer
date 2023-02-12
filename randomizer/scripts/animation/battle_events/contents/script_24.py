# BE0024_MACHINE_MADE_YARIDOVICH_MULTIPLIER

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ac39d"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ac3cf"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3ac40b"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=3, destinations=["queuestart_0x3ac447"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=4, destinations=["queuestart_0x3ac483"], bit_2=True, bit_4=True),
	RunSubroutine(["command_0x3a771e"]),
	Jmp(["command_0x3a7550"])
])
