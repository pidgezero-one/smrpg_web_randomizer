#A0606_MIDAS_1ST_TUNNEL_FISH

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3, identifier="ACTION_606_set_priority_0"),
	ShiftFDirectionSteps(3),
	SetAllSpeeds(FAST),
	ShiftZDownPixels(8),
	AddZCoord1Step(),
	DecZCoord1Step(),
	ShiftZUpPixels(8),
	SetAllSpeeds(NORMAL),
	TurnClockwise45DegreesNTimes(4),
	ShiftFDirectionSteps(3),
	TurnClockwise45DegreesNTimes(4),
	Jmp(["ACTION_606_set_priority_0"])
])
