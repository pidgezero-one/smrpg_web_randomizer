#A0307_WHIRLPOOL

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOff(),
	ShiftSoutheastPixels(8),
	SetSequenceSpeed(VERY_SLOW),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 25, ["ACTION_307_jmp_to_subroutine_6"]),
	Pause(80),
	JmpToSubroutine(["ACTION_306_visibility_on_9"], identifier="ACTION_307_jmp_to_subroutine_6"),
	TransferXYZFSteps(x=0, y=0, z=10, direction=EAST),
	Pause(40),
	Jmp(["ACTION_307_jmp_to_subroutine_6"])
])
