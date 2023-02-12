# BE0048_VALENTINA_SUMMONS_DODO_DODO_CARRIES_OFF_MIDDLE_CHARACTER

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ad15a"], bit_2=True, bit_4=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3acf5b"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3acf74"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ad040"], character_slot=True, bit_4=True),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ad07e"], character_slot=True, bit_4=True),
	SetAMEM8BitTo7E1x(0x60, 0x7EE00A),
	JmpIfAMEMBitsClear(0x60, [1], ["command_0x3a66e4"]),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3ad11c"], character_slot=True, bit_4=True),
	RunSubroutine(["command_0x3a771e"], identifier="command_0x3a66e4"),
	Jmp(["command_0x3a7550"])
])
