#A0475_CHOW_UNKNOWN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65517),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(2),
	EndLoop(),
	VisibilityOn(),
	SetSequenceSpeed(NORMAL),
	SetWalkingSpeed(SLOW),
	Jmp(["ACTION_714_turn_clockwise_45_degrees_12"])
])
