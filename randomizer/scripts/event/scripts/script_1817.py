# E1817_TROOPA_CLIFF_FALL

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(1, identifier="EVENT_1817_pause_0"),
	JmpIfMarioInAir(["EVENT_1817_pause_0"]),
	EnableControlsUntilReturn([]),
	Db(bytearray(b'\xc7\x80')),
	SetVarToConst(TEMP_70AB, 21),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	SetVarToConst(TEMP_70AB, 0),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7044_1),
	Return()
])
