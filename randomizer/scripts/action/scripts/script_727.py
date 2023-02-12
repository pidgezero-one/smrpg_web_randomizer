#A0727_MAGMITES

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	JmpIfVarEqualsConst(CURRENT_OVERWORLD_MARKER_ID, 50, ["ACTION_727_set_animation_speed_11"], identifier="ACTION_727_jmp_if_var_equals_const_0"),
	Pause(40, identifier="ACTION_727_pause_1"),
	JmpIfRandom1of2(["ACTION_727_pause_1"]),
	SetSequenceSpeed(VERY_FAST),
	SetWalkingSpeed(SLOW),
	JmpIfBitSet(TEMP_7043_0, ["ACTION_727_pause_1"]),
	Walk1StepFDirection(),
	FaceMario(),
	Walk1StepFDirection(),
	FaceMario(),
	Jmp(["ACTION_727_pause_1"]),
	SetSequenceSpeed(FASTEST, identifier="ACTION_727_set_animation_speed_11"),
	SetWalkingSpeed(NORMAL),
	Walk1StepFDirection(),
	JumpToHeight(height=0, silent=True),
	FaceMario(),
	JmpIfRandom2of3(['ACTION_727_turn_clockwise_45_degrees_n_times_18', 'ACTION_727_turn_clockwise_45_degrees_n_times_20']),
	Jmp(["ACTION_727_pause_1"]),
	TurnClockwise45DegreesNTimes(1, identifier="ACTION_727_turn_clockwise_45_degrees_n_times_18"),
	Jmp(["ACTION_727_pause_1"]),
	TurnClockwise45DegreesNTimes(7, identifier="ACTION_727_turn_clockwise_45_degrees_n_times_20"),
	Jmp(["ACTION_727_pause_1"])
])
