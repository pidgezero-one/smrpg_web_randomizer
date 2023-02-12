# BE0095_BOMBS_EXPLODE

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3aba9e"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3aba9e"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=3, destinations=["queuestart_0x3aba9e"], bit_2=True, bit_4=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	RunSubroutine(["command_0x3a771e"]),
	Jmp(["command_0x3a7550"])
])
