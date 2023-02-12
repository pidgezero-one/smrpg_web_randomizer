#A0134_HENCHMAN_TERRORIZING_WALLET_GUY

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3, identifier="ACTION_134_set_priority_0"),
	JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
	ClearBit(TEMP_7044_5),
	JmpToSubroutine(["ACTION_106_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_106_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	SetBit(TEMP_7044_5),
	Jmp(["ACTION_134_set_priority_0"])
])
