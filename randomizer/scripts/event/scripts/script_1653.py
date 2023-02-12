# E1653_EXIT_BARREL_COUNT_TIMER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(1, identifier="EVENT_1653_wait"),
	Set7000ToTappedButton(),
	Mem7000AndConst(0x00F0),
	CompareVarToConst(PRIMARY_TEMP_7000, 16),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1653_zero"]),
	Set7000ToPressedButton(),
	Mem7000AndConst(0x00F0),
	CompareVarToConst(PRIMARY_TEMP_7000, 16),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1653_zero"]),
	Jmp(["EVENT_1653_wait"]),
	SetVarToConst(SECONDARY_TEMP_7024, 0, identifier="EVENT_1653_zero"),
	Return()
])
