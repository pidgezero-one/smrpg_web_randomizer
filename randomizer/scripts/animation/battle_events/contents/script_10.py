# BE0010_PUNCHINELLO_INTERLUDES_AND_PREPARES_TO_SUMMON_MEZZO_BOMBS

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3abadd"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3aba0b"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3aba25"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=3, destinations=["queuestart_0x3aba3f"], bit_2=True, bit_4=True),
	RunSubroutine(["command_0x3a771e"]),
	Jmp(["command_0x3a7550"])
])
