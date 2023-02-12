#A0130_HENCHMAN_TERRORIZING_EAST_GUARD

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3, identifier="ACTION_130_set_priority_0"),
	JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_107_set_animation_speed_0"]),
	ClearBit(TEMP_7044_3),
	SetBit(TEMP_7044_4),
	JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	ClearBit(TEMP_7044_4),
	SetBit(TEMP_7044_3),
	Jmp(["ACTION_130_set_priority_0"])
])
