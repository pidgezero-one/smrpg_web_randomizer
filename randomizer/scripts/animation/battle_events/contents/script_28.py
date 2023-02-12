# BE0028_BEAT_TENTACLES_MOVE_ON_TO_KING_CALAMARI

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	Db(bytearray(b'\x18\x00\x80')),
	SetAMEM8BitTo7E1x(0x68, 0x7EE00A),
	JmpIfAMEM8BitNotEqualsConst(0x68, 3, ["command_0x3a648e"]),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ac64c"], character_slot=True, bit_4=True),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ac69e"], character_slot=True, bit_4=True),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3ac729"], character_slot=True, bit_4=True),
	Jmp(["command_0x3a64a6"]),
	JmpIfAMEM8BitNotEqualsConst(0x68, 1, ["command_0x3a64a1"], identifier="command_0x3a648e"),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ac64c"], character_slot=True, bit_4=True),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ac729"], character_slot=True, bit_4=True),
	Jmp(["command_0x3a64a6"]),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ac69e"], character_slot=True, bit_4=True, identifier="command_0x3a64a1"),
	Pause1Frame(identifier="command_0x3a64a6"),
	ClearAMEM8Bit(0x68),
	SetAMEM8BitToConst(0x68, 1),
	Set7E1xToAMEM8Bit(0x7EE007, 0x68),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ac795"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ac7cf"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3ac7ec"], bit_2=True, bit_4=True),
	RunSubroutine(["command_0x3a771e"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
	Db(bytearray(b'\xe6')),
	Jmp(["command_0x3a7550"])
])
