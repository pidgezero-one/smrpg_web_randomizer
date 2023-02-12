#A0927_SEA_ESCAPE_BUBBLE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOff(),
	ShiftSoutheastPixels(8),
	SetSequenceSpeed(VERY_SLOW),
	JmpToSubroutine(["ACTION_304_visibility_on_21"], identifier="ACTION_927_jmp_to_subroutine_3"),
	TransferXYZFSteps(x=0, y=0, z=20, direction=NORTHEAST),
	Pause(40),
	Jmp(["ACTION_927_jmp_to_subroutine_3"])
])
