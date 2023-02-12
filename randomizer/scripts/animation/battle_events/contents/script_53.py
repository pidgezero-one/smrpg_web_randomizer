# BE0053_DOMINO_TEAMS_UP_WITH_MAD_ADDER

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ad456"], bit_2=True, bit_4=True),
	RunSubroutine(["command_0x3a7734"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=16),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ad5c1"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3ad52b"], bit_2=True, bit_4=True),
	Pause1Frame(),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ad520"], character_slot=True, bit_4=True),
	SetAMEM8BitTo7E1x(0x60, 0x7EE00A),
	JmpIfAMEMBitsClear(0x60, [0], ["command_0x3a6760"]),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ad520"], character_slot=True, bit_4=True),
	SetAMEM8BitTo7E1x(0x60, 0x7EE00A, identifier="command_0x3a6760"),
	JmpIfAMEMBitsClear(0x60, [1], ["command_0x3a676e"]),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3ad520"], character_slot=True, bit_4=True),
	ClearAMEM8Bit(0x60, identifier="command_0x3a676e"),
	SetAMEM16BitToConst(0x60, 6),
	ObjectQueueAtOffsetAndIndex(index=2, target_address=0x3A8AC0),
	RunSubroutine(["command_0x3a771e"]),
	Db(bytearray(b'\xe6')),
	Jmp(["command_0x3a7550"])
])
