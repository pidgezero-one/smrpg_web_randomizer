#A0292_MINES_FINAL_BOSS_ROOM_HENCHMAN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(FAST),
	SetPriority(2),
	ShiftSouthwestSteps(2),
	JmpIfRandom2of3(['ACTION_291_set_animation_speed_0', 'ACTION_291_set_animation_speed_0']),
	JmpToSubroutine(["ACTION_293_object_memory_modify_bits_0"]),
	Jmp(["ACTION_291_set_animation_speed_0"])
])
