#A0448_FACTORY_FOUR_SCREW_ROOM_GLUM_REAPER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOff(),
	SequenceLoopingOn(),
	SetSequenceSpeed(NORMAL),
	ShiftNortheastSteps(6, identifier="ACTION_448_shift_northeast_steps_3"),
	Pause(24),
	ShiftSouthwestSteps(6),
	Pause(24),
	Jmp(["ACTION_448_shift_northeast_steps_3"])
])
