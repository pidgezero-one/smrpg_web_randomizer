# BE0034_BLOW_THOSE_CANDLES_OUT

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3acc59"], bit_2=True, bit_4=True),
	Jmp(["command_0x3a7550"])
])
