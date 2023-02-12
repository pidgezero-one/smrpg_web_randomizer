#A0701_BOOSTER_PASS_SECRET_SPINY

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequenceLoopingOn(),
	SetWalkingSpeed(FASTEST),
	ShiftSoutheastPixels(2),
	ShiftSouthwestPixels(9),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_701_face_southeast_11"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_701_face_southeast_11"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 25, ["ACTION_701_face_southeast_11"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 27, ["ACTION_701_face_southeast_11"]),
	FaceSouthwest(),
	Return(),
	FaceSoutheast(identifier="ACTION_701_face_southeast_11"),
	Return()
])
