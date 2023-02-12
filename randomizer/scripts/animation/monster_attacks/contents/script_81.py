# PhysicalAttack89

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x353437"]),
	SpriteQueue(field_object=2, destinations=["queuestart_0x3536d0"], bit_2=True, bit_4=True),
	RunSubroutine(["command_0x357f08"]),
	RunSubroutine(["command_0x35313b"]),
	PlaySound(sound=S0111_SLEDGE),
	SetAMEM16BitToConst(0x60, 4),
	RunSubroutine(["command_0x35249d"]),
	RunSubroutine(["command_0x3577f2"]),
	RunSubroutine(["command_0x35336f"]),
	PlaySound(sound=S0012_BOMB_EXPLOSION),
	RunSubroutine(["command_0x3523df"]),
	ReturnSubroutine()
])
