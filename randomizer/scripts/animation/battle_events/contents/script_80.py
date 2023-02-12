# BE0080_EXOR_FIGHT_BEGINS

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	RunSubroutine(["command_0x3a7531"]),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3ae098"], bit_2=True, bit_4=True),
	SpriteQueue(field_object=3, destinations=["queuestart_0x3ae0b2"], bit_2=True, bit_4=True),
	Db(bytearray(b'\x18\x00\x80')),
	RunSubroutine(["command_0x3a756c"]),
	RunSubroutine(["command_0x3a771e"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=40),
	Jmp(["command_0x3a7550"])
])
