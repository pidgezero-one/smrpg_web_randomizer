# BE0075_FORMLESS_CHANGES_INTO_MOKURA

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3adeec"], bit_2=True, bit_4=True),
	Jmp(["command_0x3a7550"])
])
