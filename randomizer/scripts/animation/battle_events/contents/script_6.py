# BE0006_BELOME_SPITS_OUT_MALLOW

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SetTarget(MONSTER_1_SET),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ab96c"], current_target=True),
	RunSubroutine(["command_0x3a771e"]),
	Jmp(["command_0x3a7550"])
])
