#A0458_NIMBUS_POST_THRONE_BIRD

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequenceLoopingOn(),
	SetSolidityBits(cant_pass_walls=True),
	SetSolidityBits(cant_pass_npcs=True, bit_7=True),
	SetWalkingSpeed(NORMAL, identifier="ACTION_458_set_animation_speed_2"),
	SetSequenceSpeed(FAST),
	StartLoopNTimes(1),
	FaceMario(),
	ShiftFDirectionSteps(1),
	JmpIfRandom1of2(["ACTION_458_set_animation_speed_9"]),
	Pause(30),
	SetWalkingSpeed(SLOW, identifier="ACTION_458_set_animation_speed_9"),
	SetSequenceSpeed(NORMAL),
	EndLoop(),
	Jmp(["ACTION_458_set_animation_speed_2"])
])
