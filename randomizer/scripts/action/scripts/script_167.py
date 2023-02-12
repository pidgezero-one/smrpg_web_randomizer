#A0167_SPAWN_AT_7016_701A_CALCULATED

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetVRAMPriority(PRIORITY_3),
	SetPriority(3),
	FloatingOff(),
	Db(bytearray(b'\xc8\x00')),
	AddConstToVar(X_COORD_2, 62848),
	AddConstToVar(Y_COORD_2, 1280),
	SetVarToConst(Z_COORD_2, 144),
	TransferTo70167018701A(),
	SetWalkingSpeed(FAST),
	ShiftNortheastSteps(4),
	VisibilityOn(),
	SequenceLoopingOn(),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	Pause(15),
	VisibilityOff(),
	Return()
])
