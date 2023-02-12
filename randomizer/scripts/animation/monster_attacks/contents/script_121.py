

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	SetOMEM60To072C(),
	DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
	PlaySound(sound=S0169_TELEPORT_ATTACK),
	RunSubroutine(["command_0x357ebe"]),
	RunBattleEvent(script_id=BE0070_JINX_USES_JINXED, offset=4),
	RunSubroutine(["command_0x3535ad"]),
	RunSubroutine(["command_0x3577f2"]),
	ReturnSubroutine()
])
