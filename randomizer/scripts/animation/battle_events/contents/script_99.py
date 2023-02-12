# BE0099_UNKNOWN

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	RunSubroutine(["command_0x3a756c"]),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3ad7dd"], bit_2=True, bit_4=True),
	RunSubroutine(["command_0x3a771e"]),
	Jmp(["command_0x3a7550"])
])
