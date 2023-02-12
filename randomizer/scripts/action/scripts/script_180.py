#A0180_FOREST_1ST_UNDERGROUND_RAT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequenceLoopingOn(identifier="ACTION_180_sequence_looping_on_0"),
	ClearSolidityBits(cant_pass_walls=True),
	SetSequenceSpeed(FAST),
	ShiftSoutheastSteps(6),
	Pause(24),
	FaceSouthwest(),
	Pause(24),
	FaceNortheast(),
	Pause(24),
	FaceSoutheast(),
	Pause(24),
	ShiftSouthwestSteps(2),
	ShiftNorthwestSteps(8),
	Walk1StepNortheast(),
	ShiftNorthwestSteps(8),
	ShiftSouthwestSteps(3),
	Pause(24),
	FaceNorthwest(),
	Pause(24),
	FaceSoutheast(),
	Pause(24),
	ShiftNortheastSteps(4),
	ShiftSoutheastSteps(10),
	Jmp(["ACTION_180_sequence_looping_on_0"])
])
