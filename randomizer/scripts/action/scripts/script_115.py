#A0115_MK_THRONE_ANTECHAMBER_HENCHMAN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpIfRandom2of3(['ACTION_115_jmp_to_subroutine_4', 'ACTION_115_jmp_to_subroutine_7'], identifier="ACTION_115_jmp_if_random_above_66_0"),
	JmpToSubroutine(["ACTION_106_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	Jmp(["ACTION_115_jmp_if_random_above_66_0"]),
	JmpToSubroutine(["ACTION_107_set_animation_speed_0"], identifier="ACTION_115_jmp_to_subroutine_4"),
	JmpToSubroutine(["ACTION_105_set_animation_speed_0"]),
	Jmp(["ACTION_115_jmp_if_random_above_66_0"]),
	JmpToSubroutine(["ACTION_104_set_animation_speed_0"], identifier="ACTION_115_jmp_to_subroutine_7"),
	JmpToSubroutine(["ACTION_106_set_animation_speed_0"]),
	Jmp(["ACTION_115_jmp_if_random_above_66_0"])
])
