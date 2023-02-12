# BE0002_BELOME_SWALLOWS_MALLOW

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SetAMEM8BitTo7E1x(0x60, 0x7EFAC3),
	JmpIfAMEM8BitNotEqualsConst(0x60, 0, ["command_0x3a6101"]),
	ClearAMEM8Bit(0x60),
	Set7E1xToAMEM8Bit(0x7EE001, 0x60),
	SetAMEM8BitToConst(0x60, 1),
	Set7E1xToAMEM8Bit(0x7EE000, 0x60),
	SetTarget(MONSTER_1_SET),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ab93d"], current_target=True),
	RunSubroutine(["command_0x3a771e"]),
	Jmp(["command_0x3a7550"], identifier="command_0x3a6101")
])
