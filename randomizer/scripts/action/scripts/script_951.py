#A0951_FACTORY_2ND_ROOM_CONVEYOR_ENEMIES_AFTER_PAINT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOff(),
	SetWalkingSpeed(SLOW),
	WalkToXYCoords(x=16, y=49),
	ShiftToXYCoords(x=3, y=88),
	ShiftSoutheastSteps(3),
	VisibilityOff(),
	ShiftToXYCoords(x=6, y=28),
	Jmp(["ACTION_950_shadow_off_0"])
])
