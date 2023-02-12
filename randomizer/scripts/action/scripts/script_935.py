#A0935_EJECTING_AN_OERLIKON

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSolidityBits(cant_pass_walls=True),
	SetWalkingSpeed(FASTEST),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	ShiftZUpSteps(8),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	FloatingOff(),
	SetVarToRandom(PRIMARY_TEMP_700C, 8, identifier="ACTION_935_set_var_to_random_6"),
	FaceEast7C(),
	ShiftFDirectionSteps(2),
	JmpIfRandom1of2(["ACTION_935_set_var_to_random_6"]),
	JmpIfRandom1of2(["ACTION_935_set_var_to_random_6"]),
	VisibilityOn(),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	FloatingOn(),
	SetBit(TEMP_7043_2),
	SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetAllSpeeds(SLOW),
	JumpToHeight(height=0, silent=True),
	Pause(1, identifier="ACTION_935_pause_18"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_935_pause_18"]),
	SetWalkingSpeed(SLOW, identifier="ACTION_935_set_animation_speed_20"),
	SetSequenceSpeed(FAST),
	Walk1StepFDirection(),
	JumpToHeight(height=0, silent=True),
	TurnRandomDirection(),
	Walk1StepFDirection(),
	JmpIfRandom1of2(["ACTION_935_set_animation_speed_20"]),
	FaceMario(),
	SetWalkingSpeed(NORMAL),
	SetSequenceSpeed(VERY_FAST),
	Walk1StepFDirection(),
	Jmp(["ACTION_935_set_animation_speed_20"])
])
