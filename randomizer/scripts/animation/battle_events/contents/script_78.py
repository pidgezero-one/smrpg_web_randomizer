# BE0078_DODO_FLUTTERS_AND_EXITS_BATTLE

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3adf08"], bit_2=True, bit_4=True),
	RunSubroutine(["command_0x3a771e"]),
	Jmp(["command_0x3a7550"])
])
