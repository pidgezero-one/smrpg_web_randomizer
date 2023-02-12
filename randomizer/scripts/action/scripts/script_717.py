#A0717_BOOSTER_HILL_BOSS_SHIFT_SIDE_COORD

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(SLOW),
	ShiftNorthwestSteps(2),
	FixedFCoordOn(),
	JmpIfRandom2of3(['ACTION_717_pause_6', 'ACTION_717_pause_9'], identifier="ACTION_717_jmp_if_random_above_66_3"),
	Pause(30),
	Jmp(["ACTION_717_jmp_if_random_above_66_3"]),
	Pause(30, identifier="ACTION_717_pause_6"),
	ShiftNortheastSteps(2),
	Jmp(["ACTION_717_jmp_if_random_above_128_12"]),
	Pause(30, identifier="ACTION_717_pause_9"),
	ShiftSouthwestSteps(2),
	Jmp(["ACTION_717_jmp_if_random_above_128_17"]),
	JmpIfRandom1of2(["ACTION_717_pause_14"], identifier="ACTION_717_jmp_if_random_above_128_12"),
	Pause(30),
	Pause(30, identifier="ACTION_717_pause_14"),
	ShiftSouthwestSteps(2),
	Jmp(["ACTION_717_jmp_if_random_above_66_3"]),
	JmpIfRandom1of2(["ACTION_717_pause_19"], identifier="ACTION_717_jmp_if_random_above_128_17"),
	Pause(30),
	Pause(30, identifier="ACTION_717_pause_19"),
	ShiftNortheastSteps(2),
	Jmp(["ACTION_717_jmp_if_random_above_66_3"])
])
