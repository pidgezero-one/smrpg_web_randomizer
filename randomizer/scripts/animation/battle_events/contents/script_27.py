# BE0027_BEAT_TENTACLES_MOVE_ON_TO_NEXT

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	Db(bytearray(b'\x18\x00\x80')),
	SetAMEM8BitTo7E1x(0x68, 0x7EE00A),
	JmpIfAMEM8BitNotEqualsConst(0x68, 3, ["command_0x3a642c"]),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ac5b0"], character_slot=True, bit_4=True),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ac5f8"], character_slot=True, bit_4=True),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3ac604"], character_slot=True, bit_4=True),
	Jmp(["command_0x3a6444"]),
	JmpIfAMEM8BitNotEqualsConst(0x68, 1, ["command_0x3a643f"], identifier="command_0x3a642c"),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ac5b0"], character_slot=True, bit_4=True),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ac604"], character_slot=True, bit_4=True),
	Jmp(["command_0x3a6444"]),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ac5f8"], character_slot=True, bit_4=True, identifier="command_0x3a643f"),
	Pause1Frame(identifier="command_0x3a6444"),
	ClearAMEM8Bit(0x60),
	SetAMEM16BitToConst(0x60, 6),
	ObjectQueueAtOffsetAndIndex(index=0, target_address=0x3A8AC0),
	Pause1Frame(),
	SpriteQueue(field_object=3, destinations=["queuestart_0x3ac556"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=4, destinations=["queuestart_0x3ac573"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=5, destinations=["queuestart_0x3ac590"], bit_2=True, bit_4=True),
	RunSubroutine(["command_0x3a771e"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
	Db(bytearray(b'\xe6')),
	Jmp(["command_0x3a7550"])
])
