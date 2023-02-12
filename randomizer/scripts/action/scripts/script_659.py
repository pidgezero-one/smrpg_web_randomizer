#A0659_PIPE_VAULT_THWOMP_ROOM_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(SLOW, identifier="ACTION_659_set_animation_speed_0"),
	SetSequenceSpeed(FAST),
	StartLoopNTimes(3),
	ShiftNortheastSteps(2),
	JmpIfObjectWithinRange(object=MARIO, usually=0, tiles=4, destinations=["ACTION_659_set_animation_speed_11"]),
	EndLoop(),
	StartLoopNTimes(3),
	ShiftSouthwestSteps(2),
	JmpIfObjectWithinRange(object=MARIO, usually=0, tiles=4, destinations=["ACTION_659_set_animation_speed_11"]),
	EndLoop(),
	Jmp(["ACTION_659_set_animation_speed_0"]),
	SetSequenceSpeed(VERY_FAST, identifier="ACTION_659_set_animation_speed_11"),
	SetWalkingSpeed(NORMAL),
	FaceMario(),
	ShiftFDirectionSteps(2),
	Jmp(["ACTION_659_set_animation_speed_0"])
])
