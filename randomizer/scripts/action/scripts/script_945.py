#A0945_FACTORY_1ST_ROOM_CONVEYOR_ENEMIES

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOff(identifier="ACTION_945_shadow_off_0"),
	SetWalkingSpeed(SLOW),
	WalkToXYCoords(x=16, y=49),
	ShiftToXYCoords(x=3, y=88),
	ShiftSoutheastSteps(3),
	ShiftToXYCoords(x=6, y=28),
	Jmp(["ACTION_945_shadow_off_0"])
])
