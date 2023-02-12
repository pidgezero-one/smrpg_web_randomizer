#A0949_FACTORY_2ND_ROOM_CONVEYOR_ENEMIES_BEFORE_PAINT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOff(),
	SetWalkingSpeed(SLOW),
	VisibilityOff(),
	WalkToXYCoords(x=16, y=49),
	ShiftToXYCoords(x=3, y=88),
	ShiftSoutheastSteps(3),
	ShiftToXYCoords(x=6, y=28),
	VisibilityOn(),
	Jmp(["ACTION_948_shadow_off_0"])
])
