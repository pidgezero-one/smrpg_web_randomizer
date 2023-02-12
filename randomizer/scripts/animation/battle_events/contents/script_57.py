# BE0057_SHY_AWAY_WATERS_SMILAX_PART_3

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	ClearAMEM8Bit(0x60),
	SetAMEM16BitToConst(0x60, 8),
	ObjectQueueAtOffsetAndIndex(index=2, target_address=0x3A8AC0),
	RunSubroutine(["command_0x3a774a"]),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ad869"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3ad883"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=5, destinations=["queuestart_0x3ad89d"], bit_2=True, bit_4=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
	RunSubroutine(["command_0x3a757a"]),
	RunSubroutine(["command_0x3a773f"]),
	Jmp(["command_0x3a7550"])
])
