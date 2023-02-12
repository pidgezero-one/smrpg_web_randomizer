# BE0058_THRAX_IS_THERE

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	ClearAMEM8Bit(0x60),
	SetAMEM16BitToConst(0x60, 8),
	ObjectQueueAtOffsetAndIndex(index=4, target_address=0x3A8AC0),
	RunSubroutine(["command_0x3a771e"]),
	Jmp(["command_0x3a7550"])
])
