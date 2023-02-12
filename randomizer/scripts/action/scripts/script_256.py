#A0256_NIMBUS_SHY_GUY_LEFT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 117, ["ACTION_256_reset_properties_8"]),
	ResetProperties(),
	FaceNortheast(),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(NORMAL),
	WalkToXYCoords(x=5, y=109),
	Return(),
	ResetProperties(identifier="ACTION_256_reset_properties_8"),
	FaceNortheast(),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(NORMAL),
	WalkToXYCoords(x=25, y=78),
	FaceNortheast(),
	Return()
])
