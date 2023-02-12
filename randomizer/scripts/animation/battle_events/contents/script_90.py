# BE0090_SMITHY_TRANSFORMS_INTO_BOX_HEAD

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3ae2cd"], bit_2=True, bit_4=True),
	SetAMEMToRandom(amem=0x60, upper_bound=4),
	JmpIfAMEM8BitEqualsConst(0x60, 0, ["command_0x3a6ebf"]),
	JmpIfAMEM8BitEqualsConst(0x60, 1, ["command_0x3a6ec7"]),
	JmpIfAMEM8BitEqualsConst(0x60, 2, ["command_0x3a6ecf"]),
	JmpIfAMEM8BitEqualsConst(0x60, 3, ["command_0x3a6ed7"]),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ae20e"], bit_2=True, bit_4=True, identifier="command_0x3a6ebf"),
	Jmp(["command_0x3a6edc"]),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ae231"], bit_2=True, bit_4=True, identifier="command_0x3a6ec7"),
	Jmp(["command_0x3a6edc"]),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ae254"], bit_2=True, bit_4=True, identifier="command_0x3a6ecf"),
	Jmp(["command_0x3a6edc"]),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ae277"], bit_2=True, bit_4=True, identifier="command_0x3a6ed7"),
	RunSubroutine(["command_0x3a771e"], identifier="command_0x3a6edc"),
	Jmp(["command_0x3a7550"])
])
