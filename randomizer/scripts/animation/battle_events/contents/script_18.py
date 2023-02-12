# BE0018_KNIFE_GUY_GRATE_GUY_PAIR_UP_PIGGY_BACK

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3abf13"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3abf52"], bit_2=True, bit_4=True),
	RunSubroutine(["command_0x3a771e"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
	Jmp(["command_0x3a7550"])
])
