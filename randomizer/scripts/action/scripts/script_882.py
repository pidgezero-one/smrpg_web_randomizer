#A0882_NIMBUS_SHAMAN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSolidityBits(cant_pass_walls=True, identifier="ACTION_882_set_solidity_bits_0"),
	SetSolidityBits(cant_pass_npcs=True, bit_7=True),
	SetWalkingSpeed(FAST, identifier="ACTION_882_set_animation_speed_2"),
	SetSequenceSpeed(VERY_FAST),
	StartLoopNTimes(1),
	FaceMario(),
	ShiftFDirectionSteps(1),
	JmpIfRandom1of2(["ACTION_882_set_animation_speed_9"]),
	Pause(30),
	SetWalkingSpeed(NORMAL, identifier="ACTION_882_set_animation_speed_9"),
	SetSequenceSpeed(NORMAL),
	EndLoop(),
	Jmp(["ACTION_882_set_animation_speed_2"])
])
