# BE0045_ZOMBONE_DIES

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ace0a"], bit_2=True, bit_4=True),
	ClearAMEM8Bit(0x60),
	SetAMEM16BitToConst(0x60, 8),
	ObjectQueueAtOffsetAndIndex(index=0, target_address=0x3A8AC0),
	RunSubroutine(["command_0x3a771e"]),
	Jmp(["command_0x3a7550"])
])
