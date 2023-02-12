#A0950_FACTORY_2ND_ROOM_CONVEYOR_ENEMIES_AFTER_PAINT_BASE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOff(identifier="ACTION_950_shadow_off_0"),
	SetWalkingSpeed(SLOW),
	WalkToXYCoords(x=11, y=38),
	ShiftSoutheastPixels(11),
	SetBit(TEMP_7043_1),
	WalkToXYCoords(x=11, y=39),
	VisibilityOn(),
	WalkToXYCoords(x=16, y=49),
	ShiftToXYCoords(x=3, y=88),
	ShiftSoutheastSteps(3),
	VisibilityOff(),
	ShiftToXYCoords(x=6, y=28),
	Jmp(["ACTION_950_shadow_off_0"])
])
