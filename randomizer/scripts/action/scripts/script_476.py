#A0476_BANDITS_WAY_SPINY

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequenceLoopingOn(),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(1),
	EndLoop(),
	SetAllSpeeds(NORMAL, identifier="ACTION_476_set_animation_speed_6"),
	StartLoopNTimes(2),
	TurnClockwise45DegreesNTimes(2),
	Pause(5),
	EndLoop(),
	Pause(16),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=5, destinations=["ACTION_476_set_animation_speed_17"]),
	Walk1StepFDirection(),
	Pause(16),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=5, destinations=["ACTION_476_set_animation_speed_17"]),
	Jmp(["ACTION_476_set_animation_speed_6"]),
	SetAllSpeeds(FAST, identifier="ACTION_476_set_animation_speed_17"),
	StartLoopNTimes(1),
	FaceMario(),
	ShiftFDirectionSteps(2),
	EndLoop(),
	Jmp(["ACTION_476_set_animation_speed_6"])
])
