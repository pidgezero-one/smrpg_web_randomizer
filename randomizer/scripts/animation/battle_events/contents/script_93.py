# BE0093_BEAM_OF_LIGHT_FORMS_AROUND_SMITHY_HEAD_BEFORE_BODY_APPEARS

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SetAMEM16BitToConst(0x60, 12),
	ObjectQueueAtOffsetAndIndex(index=4, target_address=0x3A8AC0),
	SpriteQueue(field_object=0, destinations=["queuestart_0x3ae32a"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=1, destinations=["queuestart_0x3ae2ed"], bit_2=True, bit_4=True),
	RunSubroutine(["command_0x3a771e"]),
	Jmp(["command_0x3a7550"])
])
