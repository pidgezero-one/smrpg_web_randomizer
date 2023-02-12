# BE0025_DRILL_BIT

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ac4c3"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ac4da"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3ac4da"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=3, destinations=["queuestart_0x3ac4da"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=4, destinations=["queuestart_0x3ac4ec"], bit_2=True, bit_4=True),
	RunSubroutine(["command_0x3a77c3"]),
	RunSubroutine(["command_0x3a771e"]),
	Jmp(["command_0x3a7550"])
])
