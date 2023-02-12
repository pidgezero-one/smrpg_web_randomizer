#A1003_KEEP_ORIGINAL_THRONE_ROOM_TROOPA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(FAST, identifier="ACTION_1003_set_animation_speed_0"),
	SetWalkingSpeed(FAST),
	ShiftSoutheastPixels(8),
	ShiftSoutheastSteps(2),
	SetSequenceSpeed(NORMAL),
	SetWalkingSpeed(NORMAL),
	ShiftSoutheastSteps(1),
	FaceNorthwest(),
	Pause(10),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(FAST),
	ShiftNorthwestSteps(2),
	ShiftNorthwestPixels(8),
	SetSequenceSpeed(NORMAL),
	SetWalkingSpeed(NORMAL),
	ShiftNorthwestSteps(1),
	FaceSoutheast(),
	Pause(10),
	Jmp(["ACTION_1003_set_animation_speed_0"])
])
