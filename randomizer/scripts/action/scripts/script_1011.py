#A1011_KEEP_DARK_ROOM_JUMPING_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FixedFCoordOn(),
	JumpToHeight(64),
	SetWalkingSpeed(FAST),
	ShiftSoutheastSteps(1),
	ShiftSoutheastPixels(8),
	Pause(30),
	FixedFCoordOff(),
	Jmp(["ACTION_1012_face_mario_0"])
])
